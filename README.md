# TDT4173 Project

## Project structure
The project is simply split in two directories, "Data" and "Notebooks". 

The "Data" directory, contains two sub-directories: 
* "Raw data", which simply contains the raw data from our chosen dataset for the project.
* "Clean and processed", which contains three scripts for processing, and generated CSV-files. Furthermore, there is a README containing instructions on the processing scripts.

The "Notebooks" directory contains all notebooks with model implementations, as well as the required CSV-files:
* Decision tree classifier notebook
* Support vector classifier notebook
* K-nearest neighbor classifier notebook
* Random forest classifier notebook

* Data exploration notebook

* "OnehotAll.csv" - CSV used in the notebooks
* "OnehotOrd.csv" - CSV used in the notebooks
* "StudentsPerformance.csv" - CSV used in the notebooks
Furthermore, the notebook directory contains a README with instructions.


## Project introduction
Closing project for the course TDT4173, for the fall semester of 2020. The purpose of the project is to gain hands on experience and experiment with implementing and using machine learning models from the course syllabus. The goal is not only to implement, but also understand how and why models perform as they do. A project report will be added when the project is finished.

## Description
The following is the project proposal:

" For the project, the task of supervised classification to predict a student’s performance is addressed. The problem is a binary classification one, where the objective is to predict whether a student will get an exam score below or over a chosen threshold based on different attributes that describe the student’s background. 

The dataset for the project is ”Students Performance in Exams” from Kaggle. The data set has 1000 instances with 8 attributes. The first three attributes are integer values indicating thestudent’s score in math, writing and reading. The remaining five attributes are categorical and contain information about the student that can affect school performance, and include gender, ethnicity, parental level of education, lunch, and test preparation. 

The objective of the project is to evaluate a set of supervised learning algorithms based on the chosen data set. The supervised learning classifiers used for this task are:
* Support Vector Machine (SVM)
* K-Nearest Neighbors (KNN)
* Decision Trees (DT)
* Random Forests (RF)

In order to evaluate and compare each algorithm’s performance, the following performance metricsare used:
* F1-Score
* Confusion Matrix
* Precision-Recall
* Specificity-Sensitivity
* K-Fold Cross-Validation

After comparing the algorithms according to the different evaluation methods, the best fitted algorithm will be tuned to best fit the data set. "

## Contributors
@amerk97
@3mlyh
@magdalenatran
