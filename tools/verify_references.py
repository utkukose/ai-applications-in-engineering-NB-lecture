#!/usr/bin/env python3
"""Independent check of the course bibliography against Crossref, arXiv and OpenAlex.

Each entry in references/references.json is checked as follows:
  DOI entries    -> Crossref record: title similarity and publication year.
  arXiv entries  -> arXiv API record: title similarity.
  other entries  -> Crossref bibliographic search, then OpenAlex search.
Books, standards, laws and web pages that are not indexed are listed for manual confirmation.
Usage: python tools/verify_references.py [--report references/VERIFICATION_REPORT.md]
"""
import argparse
import difflib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

UA = "course-reference-check/1.0 (mailto:utkukose@sdu.edu.tr)"


def get(url, attempts=4):
    for i in range(attempts):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            if e.code not in (429, 500, 502, 503, 504) or i == attempts - 1:
                raise
        except urllib.error.URLError:
            if i == attempts - 1:
                raise
        time.sleep(3 * 2 ** i)


def norm(s):
    return re.sub(r"[^a-z0-9 ]", "", re.sub(r"<[^>]+>", "", s.lower())).strip()


def sim(a, b):
    a, b = norm(a), norm(b)
    if not a or not b:
        return 0.0
    if a in b or b in a:
        return 1.0
    return difflib.SequenceMatcher(None, a, b).ratio()


def check_doi(r):
    d = json.loads(get("https://api.crossref.org/works/" + urllib.parse.quote(r["doi"])))["message"]
    title = (d.get("title") or [""])[0]
    year = None
    for k in ("published-print", "published-online", "issued"):
        if d.get(k, {}).get("date-parts"):
            year = d[k]["date-parts"][0][0]
            break
    s = sim(r["title"], title)
    ok = s >= 0.8 and (year is None or abs(int(year) - int(r["year"])) <= 1)
    return ok, f"Crossref title similarity {s:.2f}, year {year}", title


def check_arxiv(r):
    x = get("https://export.arxiv.org/api/query?id_list=" + r["arxiv"])
    ns = {"a": "http://www.w3.org/2005/Atom"}
    e = ET.fromstring(x).find("a:entry", ns)
    title = " ".join(e.find("a:title", ns).text.split()) if e is not None and e.find("a:title", ns) is not None else ""
    s = sim(r["title"], title)
    return s >= 0.8, f"arXiv title similarity {s:.2f}", title


def search(r):
    q = urllib.parse.quote(f"{r['title']} {r['authors']} {r['year']}")
    try:
        items = json.loads(get(f"https://api.crossref.org/works?rows=5&query.bibliographic={q}"))["message"]["items"]
        best = max(((sim(r["title"], (i.get("title") or [""])[0]), (i.get("title") or [""])[0]) for i in items), default=(0, ""))
        if best[0] >= 0.85:
            return True, f"Crossref search match {best[0]:.2f}", best[1]
    except Exception:
        pass
    try:
        res = json.loads(get("https://api.openalex.org/works?per-page=5&search=" + urllib.parse.quote(r["title"])))["results"]
        best = max(((sim(r["title"], i.get("title") or ""), i.get("title") or "") for i in res), default=(0, ""))
        if best[0] >= 0.85:
            return True, f"OpenAlex search match {best[0]:.2f}", best[1]
    except Exception:
        pass
    return None, "Not found in Crossref or OpenAlex: confirm manually (common for standards, laws, web pages and some books)", ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--refs", default="references/references.json")
    ap.add_argument("--report", default="references/VERIFICATION_REPORT.md")
    ap.add_argument("--strict", action="store_true", help="exit with status 1 when a mismatch is found")
    a = ap.parse_args()
    refs = json.load(open(a.refs, encoding="utf-8"))
    rows, fails, manual = [], 0, 0
    for k, r in refs.items():
        try:
            if r.get("doi"):
                ok, note, found = check_doi(r)
            elif r.get("arxiv"):
                ok, note, found = check_arxiv(r)
            else:
                ok, note, found = search(r)
        except Exception as e:
            ok, note, found = None, f"Lookup failed ({e}): confirm manually", ""
        if ok is False:
            fails += 1
        if ok is None:
            manual += 1
        status = {True: "verified", False: "MISMATCH", None: "manual"}[ok]
        rows.append(f"| `{k}` | {status} | {note} | {found.replace('|', '/')[:120]} |")
        print(f"{status:9s} {k}: {note}")
        time.sleep(0.25)
    with open(a.report, "w", encoding="utf-8") as f:
        f.write("# Reference verification report\n\n")
        f.write(f"Checked {len(refs)} entries: {len(refs) - fails - manual} verified automatically, {manual} for manual confirmation, {fails} mismatches.\n\n")
        f.write("| Key | Status | Evidence | Title found |\n|---|---|---|---|\n" + "\n".join(rows) + "\n")
    print(f"\n{len(refs)} entries, {fails} mismatches, {manual} manual. Report: {a.report}")
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as f:
            f.write(f"### Reference verification\n\n{len(refs)} entries: {len(refs) - fails - manual} verified automatically, "
                    f"{manual} for manual confirmation, {fails} to review. The full report is attached as an artifact.\n")
            if fails:
                f.write("\n| Key | Status | Evidence |\n|---|---|---|\n" + "\n".join(r.rsplit(" | ", 1)[0] + " |" for r in rows if "| MISMATCH |" in r) + "\n")
    return 1 if (fails and a.strict) else 0


if __name__ == "__main__":
    sys.exit(main())
