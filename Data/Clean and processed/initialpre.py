import pandas as pd
import numpy as np

#Find mean score and remove the three score columns. Then, label scores above or below average for binary classification

#Read csv, and rename columns for simplicity
df1 = pd.read_csv('StudentsPerformance_1.csv')
df1.rename(columns={'parental level of education': 'parent edu', 'test preparation course': 'prep course'}, inplace=True)
print(df1.head(10))

#Iterate through the data, and find mean of the three scores in the row. Append the mean to avg_score list.
#Although one should not iterate through a dataframe, it is fine here as the dataset is small.
df2 = df1
avg_score = []
for row in df2.itertuples():
    score = (row._6 + row._7 + row._8) / 3   #row.COLUMNNAME is used to access the right column. For some reason, these column names were returned as _6, _7 and _8.
    score = np.round(score, 3)
    avg_score.append(score)

df2['score'] = avg_score  # Add list as a column in dataframe with column name "score", which is our new score metric.

#We remove the original scores from the dataframe, as we don't need them anymore.
del df2['math score']
del df2['reading score']
del df2['writing score']

print(df2.head(10))


#find the mean score for the whole dataset
def mean_value(lst):
    return sum(lst) / len(lst)

mean_score = np.round(mean_value(avg_score), 3)
print('Mean score for all 1000 students is ' + str(mean_score) + '\n')
#Or just use df2.describe. Either way, mean score is 67.771
mean = 67.771


#To turn all scores to binary categories:
#Iterate through the rows in the dataframe. If the score is above or equal to mean, "above avg" is appended to our new list.
#Opposite if the score is below the mean value found above.
df3 = df2
scoreclass = []
for row in df3.itertuples():
    if (row.score >= mean):
        scoreclass.append('above avg')
    else:
        scoreclass.append('below avg')

df3['scoreclf'] = scoreclass  #The list is appended to our dataframe
print(df3.head(10))

df3 = df3.drop('score', axis=1) #We drop the numeric score variable, as we no longer need it
#df.head() is used throughout the code to check how the dataframe looks. All numeric scores should now
#be replaced with one column stating whether the combined score (total student performance) is below or average.
print(df3.head(10))


#Create a new CSV file called "Initial.csv" for further processing (the encoding scripts)
df3.to_csv('Initial.csv', na_rep='UNKNOWN', index=False)
