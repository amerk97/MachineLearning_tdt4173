import pandas as pd
import numpy as np

#Find average score and remove the three score columns. Also, label scores above or below average for out binary classification
#(might be more elegant solutions to theses scripts)

df1 = pd.read_csv('StudentsPerformance_1.csv')
df1.rename(columns={'parental level of education': 'parent edu', 'test preparation course': 'prep course'}, inplace=True)
print(df1.head(10))

df2 = df1

avg_score = []
for row in df2.itertuples():
    score = (row._6 + row._7 + row._8) / 3   #row.COLUMNNAME. For some reason the column names were returned as _6, _7 and _8
    score = np.round(score, 3)
    avg_score.append(score)

df2['score'] = avg_score  # Add list as a column in dataframe with colname "score"

del df2['math score']
del df2['reading score']
del df2['writing score']

print(df2.head(10))

def mean_value(lst):
    return sum(lst) / len(lst)

mean_score = np.round(mean_value(avg_score), 3)
print('Mean score for all 1000 students is ' + str(mean_score) + '\n')
#Or just use df2.describe. Either way, mean score is 67.771
mean = 67.771

df3 = df2

scoreclass = []
for row in df3.itertuples():
    if (row.score >= mean):
        scoreclass.append('above avg')
    else:
        scoreclass.append('below avg')

df3['scoreclf'] = scoreclass  # Add list as a column in dataframe
print(df3.head(10))

df3 = df3.drop('score', axis=1)
print(df3.head(10))


#Create a new CSV file for encoding scripts
#df3.to_csv('Initial.csv', na_rep='UNKNOWN', index=False)
