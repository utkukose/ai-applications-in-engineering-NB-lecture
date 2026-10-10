# Syllabus: Artificial Intelligence Applications in Engineering

**MUH-920 Mühendislikte Yapay Zeka Uygulamaları. Undergraduate faculty-wide common elective course, Süleyman Demirel University, Faculty of Engineering and Natural Sciences**

Instructor: Prof. Dr. Utku Kose, Department of Computer Engineering, Süleyman Demirel University. Contact: utkukose@sdu.edu.tr, utkukose@gmail.com. Last update: October 2026.

## Course information

Course code: MUH-920. Type: Faculty-wide common elective course of the Faculty of Engineering and Natural Sciences, Süleyman Demirel University, open to students of all departments of the faculty. The course is designed in line with the accreditation system of [MÜDEK](https://www.mudek.org.tr), the Association for Evaluation and Accreditation of Engineering Programs: Its learning outcomes are stated explicitly and linked to weekly activities and assessments, the projects are evaluated with published criteria, and student work is documented in reports and learning logs. Within the programme outcomes defined by MÜDEK, the course contributes mainly to the use of modern techniques and computational tools, the analysis and interpretation of data, design under realistic constraints, written communication, and the ethical and societal responsibilities of engineering.

## Course description

Artificial intelligence has become a working tool in every branch of engineering and the natural sciences: It plans routes, encodes standards, controls processes, optimises designs, predicts material properties, detects faults, reads images and signals, and drafts text and code [1, 2]. This undergraduate course introduces the full toolbox in fourteen weeks, from intelligent agents and search to fuzzy logic, evolutionary and swarm optimisation, machine learning, deep learning, language models, reinforcement learning, physics-informed learning and digital twins [3, 4, 5, 6, 7, 8]. Every week connects the methods to problems of the nineteen departments of the Faculty of Engineering and Natural Sciences of Süleyman Demirel University and to engineering fields worldwide. Students without programming experience learn Python along the way: Each new construct appears in the notebooks exactly where an engineering task needs it.

## Prerequisites

First-year mathematics: functions, derivatives, vectors and matrices at an introductory level, and elementary probability and statistics. No programming experience is required; the optional warm-up in `start-here/` introduces Colab and the first Python steps.

## Learning outcomes

1. Describe an engineering system as an intelligent agent and choose a suitable family of artificial intelligence techniques for a given problem.
2. Formulate and solve search, planning and optimisation problems with systematic search, evolutionary algorithms and swarm intelligence.
3. Represent expert knowledge as rules and fuzzy sets and build rule-based and fuzzy systems for classification and control.
4. Carry out the machine learning workflow on engineering data, including honest validation, baselines, metrics and leakage checks.
5. Build and evaluate regression, classification, clustering and anomaly detection models with scikit-learn.
6. Train neural networks, convolutional networks and sequence models in PyTorch and interpret their behaviour.
7. Explain transformers, large language models, retrieval-augmented generation and generative models, and use them with verification.
8. Apply reinforcement learning, physics-informed learning and digital twin ideas, and assess AI systems against safety, standards and regulation.
9. Write, run and adapt Python programs in Google Colab for engineering data analysis and simulation.

## Weekly plan

| Week | Topic | Python step |
|---|---|---|
| 1 | Artificial Intelligence in Engineering: Agents and First Steps in Python | Step 1: Values, variables and decisions |
| 2 | Problem Solving by Search: Routes, Plans and Paths | Step 2: Lists, tuples and loops |
| 3 | Knowledge, Rules and Expert Systems | Step 3: Dictionaries and functions |
| 4 | Fuzzy Logic and Fuzzy Control | Step 4: NumPy arrays and first plots |
| 5 | Evolutionary Computation for Engineering Design | Step 5: Random numbers, arrays and genetic operators |
| 6 | Swarm Intelligence: Particles, Ants and Bees | Step 6: Classes, objects and probabilistic choice |
| 7 | Learning from Data: The Machine Learning Workflow and Regression | Step 7: Tables with pandas and honest evaluation with scikit-learn |
| 8 | Classification and Evaluation: Defects, Failures and Grades | Step 8: Grouping, counting and evaluation functions |
| 9 | Patterns without Labels: Clustering, Signals and Anomaly Detection | Step 9: Signals, features and clustering with NumPy |
| 10 | Neural Networks: From the Perceptron to Deep Learning | Step 10: Matrices, shapes and tensors |
| 11 | Seeing with Networks: Convolutional Neural Networks and Computer Vision | Step 11: Images, batches and network classes |
| 12 | Learning from Sequences: Time Series, Forecasting and Recurrent Networks | Step 12: Time-indexed data, baselines and exceptions |
| 13 | Attention, Transformers and Generative AI | Step 13: Text, vectors and attention |
| 14 | Learning to Act, Respecting Physics and Engineering Responsibly | Step 14: Environments, learning and organised code |

The midterm project is released in Week 6 and due at the end of Week 7; the final project is released in Week 12 and due at the end of Week 14. Exact dates are announced by the instructor during active semesters.

## Learning activities and workload

Each week combines a lecture page with knowledge checks, animations and review cards, also available as printable lecture notes, an interactive lab with a self-assessment and reflection prompts, and a Colab notebook that opens with the Python step of the week and continues with hands-on exercises. A discipline challenge for every department, a weekly task and an optional research assignment complete the week; the overview page of each week lists them together with the study path. The expected workload is eight to twelve hours per week, including class sessions when the course is taught in person.

## Assessment

Assessment rests on two projects. The midterm project at the end of Week 7 and the final project at the end of Week 14 each consist of a coding application and a short technical report: Students choose one of three project options, extend the starter notebook and report the results with the common template. The midterm component counts 40 percent of the course grade and the final project 60 percent. Each week also offers an optional task that builds a personal portfolio, an optional research and report assignment and a self-assessment in the lab. The optional assignments carry no separate weight. They are combined with the midterm component, and the instructor may take them into account as a discretionary adjustment. During active semesters, the deadlines are announced by the instructor.

| Component | Weight |
|---|---|
| Midterm project, end of Week 7, with the optional weekly tasks and research assignments as a discretionary adjustment | 40 % |
| Final project, end of Week 14 | 60 % |

Reports use the Word template `exams/REPORT_TEMPLATE.docx`, cite their sources in square brackets and include executed notebooks. During an active semester, optional work can be sent to utkukose@sdu.edu.tr or utkukose@gmail.com, the weekly task together with the learning log exported from the lab. Unless an assignment states otherwise, a research report has 1500 to 2500 words, follows the structure of an academic paper and cites at least six scholarly or official sources.

## Policy on generative AI tools

Generative AI tools may be used as assistants for explanation, debugging and drafting, under four conditions. Students state in every submission which tools were used and for what. Students verify every factual, numerical and code claim themselves and remain fully responsible for correctness. Students cite the primary sources that support their work, not the tool. And students do not enter confidential, personal or unpublished data into external services. Submissions that present unverified generated content as the student's own analysis are treated as academic misconduct [9, 10].

## Academic integrity

Collaboration in discussing ideas is encouraged; code, reports and reflections are individual unless a task states otherwise. Code taken from other sources, including the reference solutions of the notebooks, must be acknowledged.

## Accessibility

The lecture pages and labs are designed for keyboard use, readable fonts, sufficient contrast and reduced motion when the operating system requests it. Students who need other adjustments can contact the instructor.

## Main textbooks and open resources

Russell and Norvig for artificial intelligence [3], Ross for fuzzy logic [11], Eiben and Smith for evolutionary computing [12], James and colleagues for statistical learning [13], Goodfellow, Bengio and Courville for deep learning [14], Sutton and Barto for reinforcement learning [7], Hyndman and Athanasopoulos for forecasting [15], and Brunton and Kutz for data-driven engineering [16]. The Python tutorial of the Python Software Foundation is the reference for the language [17].

## References

[1] Jordan, M. I., & Mitchell, T. M. (2015). Machine learning: Trends, perspectives, and prospects. *Science*, *349*(6245), 255-260. <https://doi.org/10.1126/science.aaa8415>

[2] LeCun, Y., Bengio, Y., & Hinton, G. (2015). Deep learning. *Nature*, *521*(7553), 436-444. <https://doi.org/10.1038/nature14539>

[3] Russell, S., & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson.

[4] Zadeh, L. A. (1965). Fuzzy sets. *Information and Control*, *8*(3), 338-353. <https://doi.org/10.1016/S0019-9958(65)90241-X>

[5] Kennedy, J., & Eberhart, R. (1995). Particle swarm optimization. In *Proceedings of ICNN'95, International Conference on Neural Networks*, Vol. 4 (pp. 1942-1948). IEEE. <https://doi.org/10.1109/ICNN.1995.488968>

[6] Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. In *Advances in Neural Information Processing Systems 30* (pp. 5998-6008). <https://arxiv.org/abs/1706.03762>

[7] Sutton, R. S., & Barto, A. G. (2018). *Reinforcement Learning: An Introduction* (2nd ed.). MIT Press.

[8] Raissi, M., Perdikaris, P., & Karniadakis, G. E. (2019). Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations. *Journal of Computational Physics*, *378*, 686-707. <https://doi.org/10.1016/j.jcp.2018.10.045>

[9] Ji, Z., Lee, N., Frieske, R., et al. (2023). Survey of hallucination in natural language generation. *ACM Computing Surveys*, *55*(12), 248. <https://doi.org/10.1145/3571730>

[10] Kose, U. (2018). Are we safe enough in the future of artificial intelligence? A discussion on machine ethics and artificial intelligence safety. *BRAIN. Broad Research in Artificial Intelligence and Neuroscience*, *9*(2), 184-197.

[11] Ross, T. J. (2017). *Fuzzy Logic with Engineering Applications* (4th ed.). Wiley.

[12] Eiben, A. E., & Smith, J. E. (2015). *Introduction to Evolutionary Computing* (2nd ed.). Springer. <https://doi.org/10.1007/978-3-662-44874-8>

[13] James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning* (2nd ed.). Springer. <https://doi.org/10.1007/978-1-0716-1418-1>

[14] Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press.

[15] Hyndman, R. J., & Athanasopoulos, G. (2021). *Forecasting: Principles and Practice* (3rd ed.). OTexts. <https://otexts.com/fpp3/>

[16] Brunton, S. L., & Kutz, J. N. (2022). *Data-Driven Science and Engineering: Machine Learning, Dynamical Systems, and Control* (2nd ed.). Cambridge University Press. <https://doi.org/10.1017/9781009089517>

[17] Python Software Foundation (2026). *The Python Tutorial (Python 3 documentation)*. <https://docs.python.org/3/tutorial/>
