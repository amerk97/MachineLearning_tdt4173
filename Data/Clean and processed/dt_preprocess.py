#Cleaning and preprocessing of the students dataset for use in sklearn decision tree implementation

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder


######## Aggregated score calculation ###############
#Be wary of overwriting dataframes, things might get messed up as you progress in f.ex. Jupyter

#Reading csv file, some small modifications and other useful functions:
df = pd.read_csv('StudentsPerformance_1.csv')
df.rename(columns={'parental level of education': 'parental education', 'test preparation course': 'prep course'}, inplace=True) #just renaming to shorter column names for ease
#df.head(10) #prints 10 first csv rows from top
#df.tail(10) Pring 10 last rows from bottom

#Shape of dataset, checking for null/NaN values, which should return 0 as the dataset is complete
print('The dataset consists of ' + str(df.shape[0]) + ' rows, and ' + str(df.shape[1]) + ' columns.')
missing = df.isnull().sum().sum()
print('Missing (null/NaN) values in dataframe: ' + str(missing))


# Aggregate the three scores into one overall performance indicator for students.
# find the mean of the three summed:
#There is likely a more elegant solution to this:
avg_score = []
for row in df.itertuples():
    score = (row._6 + row._7 + row._8) / 3   #row.COLUMNNAME. For some reason the column names were returned as _6, _7 and _8
    score = np.round(score, 3) #rounded to 3 decimals for simplicity
    avg_score.append(score)

dn = df
dn['score'] = avg_score  # Add list as a column in dataframe with colname "score"

# Remove attributes not needed / columns not needed: (could also use df.drop)
del dn['math score']
del dn['reading score']
del dn['writing score']

# Mean score, which will be used for our classification. E.g. above or below average students:
def mean_value(lst):
    return sum(lst) / len(lst)

mean_score = np.round(mean_value(avg_score), 3)
print('The mean score for all 1000 students is ' + str(mean_score) + '\n\n')

#Also, neat function to return statistical data about dataset. It also returns mean value, so code above is redundant
dn.describe()

# Checking how it looks
#dn.head(100)




####### One hot encoding ##############

#There are several approaches to this, like using the OneHotEncoder from sklearn.
#I have used the pandas approach here, using dummies and dataframe manipulation

# Pandas approach:
enc_edu = pd.get_dummies(dn['parental education'], prefix = 'parent')
enc_race = pd.get_dummies(dn['race/ethnicity'], prefix = 'race')
enc_gend = pd.get_dummies(dn['gender'], prefix = 'gender')
enc_lunch = pd.get_dummies(dn['lunch'], prefix = 'lunch')
enc_course = pd.get_dummies(dn['prep course'], prefix = 'course')

#For the variables with two categories, we do not want another column as it can just be made binary.
#Concatenate the dummies, and remove the default columns. Furthermore, we remove the extras and rename the 2-dimensioned columns so it is binary

#e.g. gender: 1-female, 0-male,  lunch: 1-standard, 0-free/reduced,  prep course: 1-completed, 0-none
#for the others we will keep all as new variables.

df2 = pd.concat((dn, enc_edu, enc_race, enc_gend, enc_lunch, enc_course), axis=1)

#drop the original columns, no longer need them,
df2 = df2.drop(['gender', 'race/ethnicity', 'parental education', 'lunch', 'prep course'], axis=1)

#drop the extra variables added due to dummy creation, for the binary variables, and rename
df2 = df2.drop(['gender_male', 'lunch_free/reduced', 'course_none'], axis=1)
df2.rename(columns={'gender_female': 'gender', 'lunch_standard': 'standard lunch', 'course_completed': 'completed course'}, inplace=True)
df2.rename(columns={'race_group A': 'race A', 'race_group B': 'race B', 'race_group C': 'race C', 'race_group D': 'race D', 'race_group E': 'race E'}, inplace=True)

#Thus, we end up with the one-hot encoded feature variables in the dataset:

#df2.head(10)



#### Encoding the target variable:'
# Mean is already found to be 67.771, all below are noted below avg and other above avg

mean = 67.771

scoreclass = []
for row in df2.itertuples():
    if (row.score >= mean):
        scoreclass.append('above avg')
    else:
        scoreclass.append('below avg')

df2['score'] = scoreclass  # Add list as a column in dataframe

enc_target = pd.get_dummies(df2['score'], prefix='course')
df2 = pd.concat((df2, enc_target), axis=1)
df2 = df2.drop(['score', 'course_below avg'], axis=1)
df2.rename(columns={'course_above avg': 'above avg score'}, inplace=True)

#df2.head(20)

#Now, the data should be ready to be used for the decision tree model.

#Make a csv file:
#df2.to_csv('dt_processed.csv', na_rep='UNKNOWN', index=False)
