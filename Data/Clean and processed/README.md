Not much cleaning of the data is required for this dataset.
As for preprocessing, the first step is combining the scores into an aggregated score, which will be used as our target variable in score prediction.

Other than this, encoding to fit our models is also done, as for example for the decision tree, one-hot encoding is required because the sklearn implementation does not handle categorical values. Here, all data is one-hot encoded, and may be reused for later model building.

Otherwise, the folder may contain some simple scripts used for processing, and CSV files with processed data for several uses.
