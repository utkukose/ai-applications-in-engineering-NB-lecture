<div align="center">

# Midterm project: Search, knowledge and optimisation in practice

**Artificial Intelligence Applications in Engineering (MUH-920 Mühendislikte Yapay Zeka Uygulamaları)**  
Prof. Dr. Utku Kose, Süleyman Demirel University

</div>

## Overview

The midterm project applies the methods of the first half of the course, search and planning, knowledge-based and fuzzy systems, and evolutionary and swarm optimisation, to a problem of the student's department [8, 9]. Timing: released in Week 6, due at the end of Week 7. Choose one of the three options below, extend its starter notebook, and write a technical report of 1500 to 2500 words with the structure of [REPORT_TEMPLATE.md](../REPORT_TEMPLATE.md). The midterm project counts 40 percent of the course grade. The optional weekly tasks and research and report assignments carry no separate weight. The instructor may take them into account as a discretionary adjustment of this component, as the [syllabus](../../SYLLABUS.md#assessment) explains.

## Learning outcomes assessed

Course learning outcomes 1, 2, 3 and 9 (see the course README).

## Options

### Midterm option 1: Routes and sequences

Plan a route across terrain and a visiting sequence for the same engineering operation, for example a haul truck that serves several loading points or an inspection drone that visits towers. Combine the A* planner of Week 2 for the legs between points with a genetic algorithm or an ant colony for the order of the points (Weeks 5 and 6), and compare with a nearest-neighbour baseline over at least ten seeds [1, 2].

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/utkukose/ai-applications-in-engineering-NB-lecture/blob/main/exams/midterm/MID1_route_and_sequence.ipynb) Starter notebook: `MID1_route_and_sequence.ipynb`
### Midterm option 2: From a standard to a controller

Turn the knowledge of your department into software twice. First, encode a classification procedure, a design check or a diagnostic guideline as a rule base with at least twelve rules and an explanation facility (Week 3). Second, design a fuzzy controller or fuzzy assessment model with at least two inputs for a process of your field and test it in a simulation over its operating range, compared with a simple baseline such as on-off control (Week 4) [3, 4].

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/utkukose/ai-applications-in-engineering-NB-lecture/blob/main/exams/midterm/MID2_standard_to_controller.ipynb) Starter notebook: `MID2_standard_to_controller.ipynb`
### Midterm option 3: Constrained design with evolution and swarms

Choose a design problem of your field with at least three variables and two constraints, derive or look up the governing formulas, and solve it with a genetic algorithm, differential evolution and particle swarm optimisation under the same budget of evaluations over at least ten seeds (Weeks 5 and 6). If the problem has two natural objectives, build a Pareto front [5, 6, 7].

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/utkukose/ai-applications-in-engineering-NB-lecture/blob/main/exams/midterm/MID3_constrained_design.ipynb) Starter notebook: `MID3_constrained_design.ipynb`

## Deliverables

An executed notebook with all outputs, the report as a PDF, and any additional data or code needed to reproduce the results. File names start with the student number.

## Evaluation

| Criterion | Weight |
|---|---|
| Problem formulation and relevance to the student's discipline | 15 % |
| Correctness and quality of the implementation | 25 % |
| Experimental design: baselines, seeds, splits, fair comparisons | 20 % |
| Analysis, interpretation and honest discussion of limitations | 20 % |
| Report quality, figures and references | 15 % |
| Statement on tools and responsible use | 5 % |

## Submission

During active semesters, the deadline and the submission channel are announced by the instructor; reports and notebooks can be sent to utkukose@sdu.edu.tr or utkukose@gmail.com. Self-learners are welcome to complete the projects for their own portfolios. The course policy on generative AI tools in `SYLLABUS.md` applies.

## References

[1] Hart, P. E., Nilsson, N. J., & Raphael, B. (1968). A formal basis for the heuristic determination of minimum cost paths. *IEEE Transactions on Systems Science and Cybernetics*, *4*(2), 100-107. <https://doi.org/10.1109/TSSC.1968.300136>

[2] Dorigo, M., Maniezzo, V., & Colorni, A. (1996). Ant system: Optimization by a colony of cooperating agents. *IEEE Transactions on Systems, Man, and Cybernetics, Part B*, *26*(1), 29-41. <https://doi.org/10.1109/3477.484436>

[3] Giarratano, J. C., & Riley, G. D. (2005). *Expert Systems: Principles and Programming* (4th ed.). Thomson Course Technology.

[4] Mamdani, E. H., & Assilian, S. (1975). An experiment in linguistic synthesis with a fuzzy logic controller. *International Journal of Man-Machine Studies*, *7*(1), 1-13. <https://doi.org/10.1016/S0020-7373(75)80002-2>

[5] Storn, R., & Price, K. (1997). Differential evolution: A simple and efficient heuristic for global optimization over continuous spaces. *Journal of Global Optimization*, *11*(4), 341-359. <https://doi.org/10.1023/A:1008202821328>

[6] Kennedy, J., & Eberhart, R. (1995). Particle swarm optimization. In *Proceedings of ICNN'95, International Conference on Neural Networks*, Vol. 4 (pp. 1942-1948). IEEE. <https://doi.org/10.1109/ICNN.1995.488968>

[7] Deb, K., Pratap, A., Agarwal, S., & Meyarivan, T. (2002). A fast and elitist multiobjective genetic algorithm: NSGA-II. *IEEE Transactions on Evolutionary Computation*, *6*(2), 182-197. <https://doi.org/10.1109/4235.996017>

[8] Russell, S., & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson.

[9] Eiben, A. E., & Smith, J. E. (2015). *Introduction to Evolutionary Computing* (2nd ed.). Springer. <https://doi.org/10.1007/978-3-662-44874-8>
