<div align="center">

# Final project: A learning system for an engineering problem

**Artificial Intelligence Applications in Engineering (MUH-920 Mühendislikte Yapay Zeka Uygulamaları)**  
Prof. Dr. Utku Kose, Süleyman Demirel University

</div>

## Overview

The final project applies the learning methods of the second half of the course to a problem of the student's department and assesses the result as an engineer would: against baselines, beyond the training conditions and with its risks in view [11, 12]. Timing: released in Week 12, due at the end of Week 14. Choose one of the three options below, extend its starter notebook, and write a technical report of 1500 to 2500 words with the Word template [REPORT_TEMPLATE.docx](../REPORT_TEMPLATE.docx). The final project counts 60 percent of the course grade.

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

## Example proposals

Two example proposals show the expected scope and level of detail, one for Option 1 and one for Option 2. Each follows the five parts of the proposal above and has about 600 words. Students write their own proposals in the same way for a problem of their department.

### Example 1: Valve degradation on a hydraulic test rig (Option 1, Mechanical Engineering)

**The engineering problem.** Hydraulic power units drive presses, injection moulding machines and mobile machinery, and their components degrade gradually: Coolers lose efficiency, valves switch with a lag, pumps develop internal leakage and accumulators lose pressure. Maintenance on a fixed schedule replaces some parts too early and misses others. The project asks whether the condition of the valve can be classified from the process sensors of a single load cycle, so that maintenance can be planned from routine measurements, and how far such a classifier can be trusted when the operating conditions change.

**The data.** The dataset *Condition monitoring of hydraulic systems* of the UCI repository contains 2205 load cycles of 60 seconds, recorded on a hydraulic test rig whose cooler, valve, pump and accumulator conditions were varied in several grades [14, 15]. Each cycle provides 17 signals: six pressures and the motor power sampled at 100 Hz, two volume flows at 10 Hz, and four temperatures, a vibration velocity, the cooling efficiency, the cooling power and an efficiency factor at 1 Hz. The label of interest is the valve condition, with the grades 100 % for optimal switching, 90 % for a small lag, 80 % for a severe lag and 73 % for a valve close to total failure. A further flag marks cycles in which static conditions may not have been reached yet, and these cycles are analysed separately. The data are licensed under CC BY 4.0.

**The techniques.** Every signal is summarised per cycle by its mean, standard deviation, minimum, maximum and the slope of a fitted line, which gives 85 features. Four model families are compared on these features (Weeks 8 and 10): multinomial logistic regression, a random forest, gradient boosting and a PyTorch network with two hidden layers. Scaling is fitted on the training folds only. The conditions of the other components are labels as well and never serve as inputs, because they would not be known in operation [2].

**The evaluation plan.** The cycles were recorded one after another on a single rig, so neighbouring cycles can share their conditions and their thermal state. The plan therefore compares a random split with a split into blocks of consecutive cycles, and keeps the blocks whole in five-fold cross-validation. A block of about 20 % of the cycles that contains every grade is held out for the single final test. The baselines are the most frequent class and a decision stump on the best single feature. The main metric is the macro-averaged F1 score, reported together with the recall of the 73 % grade, whose misses matter most, as mean and standard deviation over five random seeds. Permutation importance shows which sensors drive the decisions, and the report checks them against the hydraulic circuit. A second test trains on the cycles with full cooler efficiency and tests on those with reduced efficiency, a stand-in for a warmer oil in operation.

**The risk assessment.** As a tool that suggests maintenance to a technician, the classifier is not a safety component and is not high-risk under the EU AI Act. If its output stopped the machine as a safety function, it could become a safety component of machinery, which the Act treats as high-risk when the machinery requires a third-party conformity assessment [13]. For the NIST AI RMF, Govern leaves the final decision with the maintenance engineer and records the model versions; Map states the intended use and the conditions not covered, such as other rigs, oils and load cycles; Measure tracks the recall of the severe grades and the drift of the sensor statistics; and Manage returns to the fixed maintenance schedule when the inputs drift or the classifier is uncertain [3].

### Example 2: Motorway traffic for maintenance planning (Option 2, Civil Engineering)

**The engineering problem.** Lane closures for road maintenance are placed in hours of low traffic, which limits queues and the exposure of the work zone. A traffic engineer who plans the closures of the next day needs a forecast of the hourly volume. The project forecasts the hourly traffic volume of a motorway section 24 hours ahead and asks whether a deep sequence model improves on the patterns that a calendar already captures.

**The data.** The dataset *Metro Interstate Traffic Volume* of the UCI repository records the hourly westbound volume on Interstate 94 at station 301 of the Minnesota Department of Transportation, roughly midway between Minneapolis and St Paul, from 2012 to 2018 [16]. Its 48,204 records also carry the national holidays and the Minnesota State Fair, and hourly weather observations: the temperature in kelvin, rain and snow in the hour, the cloud cover and a short description of the weather. The data are licensed under CC BY 4.0. Before any modelling, the series is checked for missing hours and repeated timestamps and turned into one value per hour, with long gaps marked rather than filled.

**The techniques.** Three baselines come from Week 12: the naive forecast, the seasonal naive forecast with periods of 24 and 168 hours, and a linear regression on indicators of the hour of the week and a holiday flag [6]. The deep models are a recurrent network with LSTM cells and a one-dimensional convolutional network, both of which read the past 168 hours together with the calendar inputs and predict the next 24 hours at once (Weeks 11 and 12).

**The evaluation plan.** The split follows time, with training until the end of 2016, validation in 2017 and the single test in 2018. In the test period, a forecast is made every day at midnight from the data available at that moment, which is a rolling origin. The errors are reported per horizon as MAE and RMSE and as MASE relative to the weekly seasonal naive forecast, as mean and standard deviation over five seeds [6]. Holidays and days with snow are analysed separately. The weather columns are observations of the forecast hours and would not be known a day ahead, so the main models use them only as past values. A clearly labelled second experiment adds the observed weather as if it were a perfect forecast and reports its value as an upper bound [2]. The report discusses how the model would behave at another station or after a lasting change of commuting patterns.

**The risk assessment.** As a planning aid whose forecasts a traffic engineer reviews, the system is not a safety component and is not high-risk under the EU AI Act. If its forecasts set ramp meters or variable speed limits directly, it could become a safety component in the management and operation of road traffic, a high-risk use listed in Annex III of the Act [13]. For the NIST AI RMF, Govern leaves the closure decision and its documentation with the traffic engineer; Map records the intended use and the limits of the data, one station and one direction from 2012 to 2018; Measure tracks the error per horizon, on holidays and against the seasonal naive forecast; and Manage returns to the seasonal naive plan whenever the model is worse than it over a week of operation [3].

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

[14] Helwig, N., Pignanelli, E., & Schütze, A. (2015). *Condition monitoring of hydraulic systems [Dataset]. UCI Machine Learning Repository, ID 447*. <https://doi.org/10.24432/C5CW21>

[15] Helwig, N., Pignanelli, E., & Schütze, A. (2015). Condition monitoring of a complex hydraulic system using multivariate statistics. In *2015 IEEE International Instrumentation and Measurement Technology Conference (I2MTC) Proceedings* (pp. 210-215). <https://doi.org/10.1109/I2MTC.2015.7151267>

[16] Hogue, J. (2019). *Metro Interstate Traffic Volume [Dataset]. UCI Machine Learning Repository, ID 492*. <https://doi.org/10.24432/C5X60B>
