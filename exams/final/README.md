<div align="center">

# Final project: A learning system for an engineering problem

**Artificial Intelligence Applications in Engineering (MUH-920 Mühendislikte Yapay Zeka Uygulamaları)**  
Prof. Dr. Utku Kose, Süleyman Demirel University

</div>

## Overview

The final project applies the learning methods of the second half of the course to a problem of the student's department and assesses the result as an engineer would: against baselines, beyond the training conditions and with its risks in view [11, 12]. Timing: released in Week 12, due at the end of Week 14. Choose one of the three options below, extend its starter notebook, and write a technical report of 1500 to 2500 words with the structure of [REPORT_TEMPLATE.md](../REPORT_TEMPLATE.md). The final project counts 60 percent of the course grade.

## Learning outcomes assessed

Course learning outcomes 4 to 9 (see the course README).

## Options

### Final option 1: A predictive model for an engineering dataset

Build a regression or classification model for a public dataset of your field, following the full workflow of Weeks 7 to 10: data provenance and limits, chronological or grouped splits where needed, baselines, at least four model families including a neural network, cross-validation, one final test, explanation of the model, and leakage checks. Close with a responsible-AI assessment with the NIST AI RMF functions [1, 2, 3].

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/utkukose/ai-applications-in-engineering-NB-lecture/blob/main/exams/final/FIN1_predictive_model.ipynb) Starter notebook: `FIN1_predictive_model.ipynb`
### Final option 2: Perception or forecasting with deep learning

Train a convolutional network on images or a sequence model on a time series of your field (Weeks 11 and 12). For images, compare training from scratch with transfer learning and inspect the model with Grad-CAM. For time series, split chronologically, report seasonal naive and regression baselines, and evaluate with rolling origins. In both cases, discuss how the model would behave on data from a new site, camera or period [4, 5, 6].

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/utkukose/ai-applications-in-engineering-NB-lecture/blob/main/exams/final/FIN2_perception_or_forecast.ipynb) Starter notebook: `FIN2_perception_or_forecast.ipynb`
### Final option 3: Learning to act or respecting physics

Either train a reinforcement learning controller in a simulation of a process from your field and compare it with a rule-based or PID controller, with explicit safety limits on actions; or build a physics-informed network or a digital twin with system identification for a physical system of your field and compare it with a data-only model outside the range of the data (Week 14). Include a risk assessment of the approach [7, 8, 9, 10].

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/utkukose/ai-applications-in-engineering-NB-lecture/blob/main/exams/final/FIN3_act_or_physics.ipynb) Starter notebook: `FIN3_act_or_physics.ipynb`

## Proposal

The final project starts with a proposal of about 600 words, written in Week 12: The engineering problem, the data or simulator, the techniques from the course to be compared, the evaluation plan with baselines, and a short risk assessment that places the system within the EU AI Act categories and names one activity for each NIST AI RMF function [3, 13]. During active semesters, the proposal can be sent to utkukose@sdu.edu.tr or utkukose@gmail.com for early feedback.

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

[1] Wirth, R., & Hipp, J. (2000). CRISP-DM: Towards a standard process model for data mining. In *Proceedings of the 4th International Conference on the Practical Applications of Knowledge Discovery and Data Mining* (pp. 29-39).

[2] Kaufman, S., Rosset, S., Perlich, C., & Stitelman, O. (2012). Leakage in data mining: Formulation, detection, and avoidance. *ACM Transactions on Knowledge Discovery from Data*, *6*(4), 15. <https://doi.org/10.1145/2382577.2382579>

[3] National Institute of Standards and Technology (2023). *Artificial Intelligence Risk Management Framework (AI RMF 1.0), NIST AI 100-1*. NIST. <https://doi.org/10.6028/NIST.AI.100-1>

[4] He, K., Zhang, X., Ren, S., & Sun, J. (2016). Deep residual learning for image recognition. In *2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)* (pp. 770-778). <https://doi.org/10.1109/CVPR.2016.90>

[5] Selvaraju, R. R., Cogswell, M., Das, A., Vedantam, R., Parikh, D., & Batra, D. (2017). Grad-CAM: Visual explanations from deep networks via gradient-based localization. In *2017 IEEE International Conference on Computer Vision (ICCV)* (pp. 618-626). <https://doi.org/10.1109/ICCV.2017.74>

[6] Hyndman, R. J., & Athanasopoulos, G. (2021). *Forecasting: Principles and Practice* (3rd ed.). OTexts. <https://otexts.com/fpp3/>

[7] Sutton, R. S., & Barto, A. G. (2018). *Reinforcement Learning: An Introduction* (2nd ed.). MIT Press.

[8] Raissi, M., Perdikaris, P., & Karniadakis, G. E. (2019). Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations. *Journal of Computational Physics*, *378*, 686-707. <https://doi.org/10.1016/j.jcp.2018.10.045>

[9] Grieves, M., & Vickers, J. (2017). Digital twin: Mitigating unpredictable, undesirable emergent behavior in complex systems. In *Transdisciplinary Perspectives on Complex Systems (F.-J. Kahlen, S. Flumerfelt, & A. Alves, Eds.)* (pp. 85-113). Springer. <https://doi.org/10.1007/978-3-319-38756-7_4>

[10] Amodei, D., Olah, C., Steinhardt, J., Christiano, P., Schulman, J., & Mané, D. (2016). Concrete problems in AI safety. arXiv preprint arXiv:1606.06565. <https://arxiv.org/abs/1606.06565>

[11] Jordan, M. I., & Mitchell, T. M. (2015). Machine learning: Trends, perspectives, and prospects. *Science*, *349*(6245), 255-260. <https://doi.org/10.1126/science.aaa8415>

[12] LeCun, Y., Bengio, Y., & Hinton, G. (2015). Deep learning. *Nature*, *521*(7553), 436-444. <https://doi.org/10.1038/nature14539>

[13] European Parliament and Council of the European Union (2024). *Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act)*. Official Journal of the European Union, L series, 12 July 2024. <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>
