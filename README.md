# TDT4173 Project

## Project structure
The project is simply split in two directories, "Data" and "Notebooks". 

### "Data" directory
This directory contains two sub-directories:
* "Raw data", which simply contains the raw data file from our chosen dataset for the project.
* "Clean and processed", which contains three scripts for processing, and generated CSV-files. 

Go to this directory for the preprocessing scripts necessary in order to run the notebook kernels. 

Furthermore, there is a README containing instructions on the processing scripts.

### "Notebooks" directory
This directory contains all notebooks with model implementations, as well as the required CSV-files:
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

The core of our project is comparing machine learning methods performing binary classification on students performance on exams. The dataset we have used is taken from the public data repository of Kaggle: https://www.kaggle.com/spscientist/students-performance-in-exams. We will attempt to create models that can do binary classification on student performances, based on the feature variables, such as gender and lunch type. The methods that are used are
* Support Vector Machine (SVM)
* K-Nearest Neighbors (KNN)
* Decision Trees (DT)
* Random Forests (RF)

These will be evalueted using metric scores such as accuracy, f1-score, precision-recall and (Stratified) K-fold cross-validation. 

## Contributors
@amerk97
@3mlyh
@magdalenatran
