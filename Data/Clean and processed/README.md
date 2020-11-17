"StudentsPerformance_1" is the exact same as the original dataset, so this is just the raw data used to derive our new CSVs. 

Not much cleaning of the data is required for this dataset This is looked further at in the "stats" notebook under "Notebooks" directory.

As for preprocessing, the first step is combining the scores into an aggregated score, which will be used as our target variable in score prediction. The target variable is then made binary, marked as "above average score" and "below average score".

Furthermore, encoding is performed on the data to fit the models. Here, 2 CSV files are included, derived from Initial.csv the following:
* OnehotAll: All variables are one hot encoded.
* OnehotOrd: All variables are one hot encoded, except parental education which is ordinal encoded. 

The python files containing the scripts for the preprocessing and CSV file creation are also in this directory, some other scripts/notebooks may be included.
