# Datasets

All datasets used in the course are public or generated in the notebooks. The `Check` column marks sources confirmed online during preparation. UCI datasets are loaded with the `ucimlrepo` package; the other sources are read directly from their services. Whenever a source cannot be reached, the notebook switches to a synthetic stand-in with the same structure, documented in the notebook, so that every cell still runs. Synthetic numbers are illustrative and must not be reported as measurements.

| Dataset | Source | Licence | Weeks | Departments | Reference | Check |
|---|---|---|---|---|---|---|
| Isparta hourly weather, ERA5 reanalysis | Open-Meteo Historical Weather API | CC BY 4.0 (Open-Meteo) | 1, 12 | All | [1, 2] | web |
| Elevation near Isparta, Copernicus GLO-90 | Open-Meteo Elevation API | Copernicus DEM licence, CC BY 4.0 (Open-Meteo) | 2 | Civil, Mining, Geology | [1, 3] | web |
| Concrete Compressive Strength | UCI ML Repository, ID 165 | CC BY 4.0 | 7, 10 | Civil | [4, 5] | web |
| Combined Cycle Power Plant | UCI ML Repository, ID 294 | CC BY 4.0 | 7, 10 | Mechanical, Electrical | [6] | web |
| Energy Efficiency (building loads) | UCI ML Repository, ID 242 | CC BY 4.0 | 7, 10 | Civil, Physics | [7] | web |
| Airfoil Self-Noise | UCI ML Repository, ID 291 | CC BY 4.0 | 7 | Automotive, Mechanical, Aerospace | [8] | web |
| Gas Turbine CO and NOx Emission | UCI ML Repository, ID 551 | CC BY 4.0 | 7, 10 | Environmental, Chemical | [9] | web |
| Superconductivity | UCI ML Repository, ID 464 | CC BY 4.0 | 7, 10 | Physics, Chemistry | [10, 11] | web |
| Productivity Prediction of Garment Employees | UCI ML Repository, ID 597 | CC BY 4.0 | 7 | Industrial, Textile | [12] | web |
| Wine Quality | UCI ML Repository, ID 186 | CC BY 4.0 | 7, 8 | Food, Chemical | [13, 14] | web |
| Dry Bean | UCI ML Repository, ID 602 | CC BY 4.0 | 8, 10 | Food, Biology | [15, 16] | web |
| Rice (Cammeo and Osmancik) | UCI ML Repository, ID 545 | CC BY 4.0 | 8 | Food, Biology | [17, 18] | web |
| AI4I 2020 Predictive Maintenance | UCI ML Repository, ID 601 | CC BY 4.0 | 8, 10 | Mechanical, Industrial | [19, 20] | web |
| Steel Plates Faults | UCI ML Repository, ID 198 | CC BY 4.0 | 8 | Mechanical, Textile | [21] | web |
| seismic-bumps | UCI ML Repository, ID 266 | CC BY 4.0 | 8 | Mining, Geophysics | [22, 23] | web |
| MAGIC Gamma Telescope | UCI ML Repository, ID 159 | CC BY 4.0 | 8 | Physics | [24] | web |
| QSAR Biodegradation | UCI ML Repository, ID 254 | CC BY 4.0 | 8 | Chemistry, Environmental | [25] | web |
| Electrical Grid Stability Simulated Data | UCI ML Repository, ID 471 | CC BY 4.0 | 8 | Electrical | [26] | web |
| Well-log facies, SEG 2016 contest | github.com/seg/2016-ml-contest | See the repository | 9 | Geology, Geophysics, Earth Sciences, Mining | [27] | web |
| Earthquake catalogue | USGS FDSN Event Web Service | U.S. government data, public domain | 9, 12 | Geophysics, Earth Sciences | [28] | web |
| Mauna Loa monthly CO2 | NOAA Global Monitoring Laboratory | Free use with citation | 12 | Environmental, Earth Sciences | [29, 30] | web |
| Fashion-MNIST | torchvision / Zalando Research | MIT | 11 | All | [31] | - |
| ImageNet-pretrained ResNet-18 weights | torchvision | See the torchvision documentation | 11 | All | [32, 33] | - |
| CartPole-v1 environment | Gymnasium | MIT | 14 | Mechanical, Electrical, Computer | [34, 35] | - |
| Generated data: concrete crack images, bearing vibration, winter days, oscillator, synthetic stand-ins | Generated in the notebooks | MIT (code) | 1 to 14 | All |  | - |

## Adding a dataset for your own department

Prefer sources with a clear licence and a persistent identifier, such as a DOI. Record the version or download date, the units of every variable and the conditions under which the data were collected. Split the data before any fitting, as Week 7 explains, and check whether any column would be unavailable at prediction time. Portals worth searching include the UCI Machine Learning Repository [36], national open data portals and the data services of scientific agencies.

## References

[1] Open-Meteo (2026). *Open-Meteo free weather API: Historical Weather API and Elevation API (data licensed under CC BY 4.0)*. <https://open-meteo.com>

[2] Hersbach, H., Bell, B., Berrisford, P., et al. (2020). The ERA5 global reanalysis. *Quarterly Journal of the Royal Meteorological Society*, *146*(730), 1999-2049. <https://doi.org/10.1002/qj.3803>

[3] European Space Agency (2021). *Copernicus Global Digital Elevation Model (GLO-90)*. <https://doi.org/10.5270/ESA-c5d3d65>

[4] Yeh, I.-C. (1998). *Concrete Compressive Strength [Dataset]. UCI Machine Learning Repository, ID 165*. <https://doi.org/10.24432/C5PK67>

[5] Yeh, I.-C. (1998). Modeling of strength of high-performance concrete using artificial neural networks. *Cement and Concrete Research*, *28*(12), 1797-1808. <https://doi.org/10.1016/S0008-8846(98)00165-3>

[6] Tüfekci, P. (2014). Prediction of full load electrical power output of a base load operated combined cycle power plant using machine learning methods. *International Journal of Electrical Power & Energy Systems*, *60*, 126-140. <https://doi.org/10.1016/j.ijepes.2014.02.027>

[7] Tsanas, A., & Xifara, A. (2012). Accurate quantitative estimation of energy performance of residential buildings using statistical machine learning tools. *Energy and Buildings*, *49*, 560-567. <https://doi.org/10.1016/j.enbuild.2012.03.003>

[8] Brooks, T. F., Pope, D. S., & Marcolini, M. A. (1989). *Airfoil Self-Noise and Prediction (NASA Reference Publication 1218)*. NASA.

[9] Kaya, H., Tüfekci, P., & Uzun, E. (2019). Predicting CO and NOx emissions from gas turbines: Novel data and a benchmark PEMS. *Turkish Journal of Electrical Engineering and Computer Sciences*, *27*(6), 4783-4796. <https://doi.org/10.3906/elk-1807-87>

[10] Hamidieh, K. (2018). *Superconductivty Data [Dataset]. UCI Machine Learning Repository, ID 464*. <https://doi.org/10.24432/C53P47>

[11] Hamidieh, K. (2018). A data-driven statistical model for predicting the critical temperature of a superconductor. *Computational Materials Science*, *154*, 346-354. <https://doi.org/10.1016/j.commatsci.2018.07.052>

[12] Imran, A. A., Rahim, M. S., & Ahmed, T. (2020). *Productivity Prediction of Garment Employees [Dataset]. UCI Machine Learning Repository, ID 597*. <https://archive.ics.uci.edu/dataset/597>

[13] Cortez, P., Cerdeira, A., Almeida, F., Matos, T., & Reis, J. (2009). *Wine Quality [Dataset]. UCI Machine Learning Repository, ID 186*. <https://doi.org/10.24432/C56S3T>

[14] Cortez, P., Cerdeira, A., Almeida, F., Matos, T., & Reis, J. (2009). Modeling wine preferences by data mining from physicochemical properties. *Decision Support Systems*, *47*(4), 547-553. <https://doi.org/10.1016/j.dss.2009.05.016>

[15] Koklu, M., & Ozkan, I. A. (2020). *Dry Bean [Dataset]. UCI Machine Learning Repository, ID 602*. <https://doi.org/10.24432/C50S4B>

[16] Koklu, M., & Ozkan, I. A. (2020). Multiclass classification of dry beans using computer vision and machine learning techniques. *Computers and Electronics in Agriculture*, *174*, 105507. <https://doi.org/10.1016/j.compag.2020.105507>

[17] Cinar, I., & Koklu, M. (2019). *Rice (Cammeo and Osmancik) [Dataset]. UCI Machine Learning Repository, ID 545*. <https://doi.org/10.24432/C5MW4Z>

[18] Cinar, I., & Koklu, M. (2019). Classification of rice varieties using artificial intelligence methods. *International Journal of Intelligent Systems and Applications in Engineering*, *7*(3), 188-194. <https://doi.org/10.18201/ijisae.2019355381>

[19] Matzka, S. (2020). *AI4I 2020 Predictive Maintenance Dataset [Dataset]. UCI Machine Learning Repository, ID 601*. <https://doi.org/10.24432/C5HS5C>

[20] Matzka, S. (2020). Explainable artificial intelligence for predictive maintenance applications. In *2020 Third International Conference on Artificial Intelligence for Industries (AI4I)* (pp. 69-74). IEEE. <https://doi.org/10.1109/AI4I49448.2020.00023>

[21] Buscema, M., Terzi, S., & Tastle, W. (2010). *Steel Plates Faults [Dataset]. UCI Machine Learning Repository, ID 198*. <https://doi.org/10.24432/C5J88N>

[22] Sikora, M., & Wróbel, Ł. (2010). *seismic-bumps [Dataset]. UCI Machine Learning Repository, ID 266*. <https://doi.org/10.24432/C5W902>

[23] Sikora, M., & Wróbel, Ł. (2010). Application of rule induction algorithms for analysis of data collected by seismic hazard monitoring systems in coal mines. *Archives of Mining Sciences*, *55*(1), 91-114.

[24] Bock, R. (2004). *MAGIC Gamma Telescope [Dataset]. UCI Machine Learning Repository, ID 159*. <https://doi.org/10.24432/C52C8B>

[25] Mansouri, K., Ringsted, T., Ballabio, D., Todeschini, R., & Consonni, V. (2013). *QSAR biodegradation [Dataset]. UCI Machine Learning Repository, ID 254*. <https://doi.org/10.24432/C5H60M>

[26] Arzamasov, V. (2018). *Electrical Grid Stability Simulated Data [Dataset]. UCI Machine Learning Repository, ID 471*. <https://doi.org/10.24432/C5PG66>

[27] Hall, B. (2016). Facies classification using machine learning. *The Leading Edge*, *35*(10), 906-909. <https://doi.org/10.1190/tle35100906.1>

[28] U.S. Geological Survey (2026). *Earthquake Catalog API (FDSN Event Web Service)*. <https://earthquake.usgs.gov/fdsnws/event/1/>

[29] Lan, X., & Keeling, R. (2026). *Trends in atmospheric carbon dioxide: Mauna Loa CO2 monthly mean data. NOAA Global Monitoring Laboratory and Scripps Institution of Oceanography*. <https://gml.noaa.gov/ccgg/trends/>

[30] Keeling, C. D., Bacastow, R. B., Bainbridge, A. E., Ekdahl, C. A., Guenther, P. R., Waterman, L. S., & Chin, J. F. S. (1976). Atmospheric carbon dioxide variations at Mauna Loa Observatory, Hawaii. *Tellus*, *28*(6), 538-551. <https://doi.org/10.1111/j.2153-3490.1976.tb00701.x>

[31] Xiao, H., Rasul, K., & Vollgraf, R. (2017). Fashion-MNIST: A novel image dataset for benchmarking machine learning algorithms. arXiv preprint arXiv:1708.07747. <https://arxiv.org/abs/1708.07747>

[32] He, K., Zhang, X., Ren, S., & Sun, J. (2016). Deep residual learning for image recognition. In *2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)* (pp. 770-778). <https://doi.org/10.1109/CVPR.2016.90>

[33] Deng, J., Dong, W., Socher, R., Li, L.-J., Li, K., & Fei-Fei, L. (2009). ImageNet: A large-scale hierarchical image database. In *2009 IEEE Conference on Computer Vision and Pattern Recognition* (pp. 248-255). <https://doi.org/10.1109/CVPR.2009.5206848>

[34] Towers, M., Kwiatkowski, A., Terry, J., et al. (2024). Gymnasium: A standard interface for reinforcement learning environments. arXiv preprint arXiv:2407.17032. <https://arxiv.org/abs/2407.17032>

[35] Barto, A. G., Sutton, R. S., & Anderson, C. W. (1983). Neuronlike adaptive elements that can solve difficult learning control problems. *IEEE Transactions on Systems, Man, and Cybernetics*, *SMC-13*(5), 834-846. <https://doi.org/10.1109/TSMC.1983.6313077>

[36] Kelly, M., Longjohn, R., & Nottingham, K. (2026). *The UCI Machine Learning Repository*. <https://archive.ics.uci.edu>
