### Running the prepocessing scripts

To run the scripts, you need Numpy and Pandas libraries installed.

1. Make sure you have the CSV-file "StudentsPerformance_1.csv" in the same directory as the scripts.
2. Run the script "initialpre.py", which takes in "StudentsPerformance_1.csv" and does initial processing. A file "Initial.csv" should be created.
Now, make sure that "Initial.csv" is in the same directory as the scripts. The following two steps can be done in any order:
3. Run the script "onehot_all.py", which takes in "Initial.csv". A file "OnehotAll.csv" should be created.
4. Run the script "onehotord.py", which takes in "Initial.csv". A file "OnehotOrd.csv" should be created. 

You should now have two CSV-files:
* "OnehotAll.csv", where all variables are one-hot encoded.
* "OnehotOrd.csv", where all variables are one-hot encoded, except parental education which is ordinal encoded.
These two files should be copied and moved to the same directory as the notebooks implementing the ML-models, with the same naming. 

NOTE: "StudentsPerformance_1.csv" is the exact same as the original dataset but renamed, so this is just the raw data used to derive our new CSVs. 

