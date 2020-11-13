import pandas as pd
import numpy as np

#All variables shall be one-hot encoded.
#Pandas approach will be used here instead of OneHotEncoder from sklearn.

df1 = pd.read_csv('Initial.csv')
print(df1.head())

#Simply create dummies for all columns. Extra columns that are redundant are removed.
#Note that the redundant race and education columns are left on purpose here for testing.

enc_edu = pd.get_dummies(df1['parent edu'], prefix = 'parent')
enc_race = pd.get_dummies(df1['race/ethnicity'], prefix = 'race')
enc_gend = pd.get_dummies(df1['gender'], prefix = 'gender')
enc_lunch = pd.get_dummies(df1['lunch'], prefix = 'lunch')
enc_course = pd.get_dummies(df1['prep course'], prefix = 'course')

df2 = pd.concat((df1, enc_edu, enc_race, enc_gend, enc_lunch, enc_course), axis=1)

#drop the original columns
df2 = df2.drop(['gender', 'race/ethnicity', 'parent edu', 'lunch', 'prep course'], axis=1)

#drop the extra variables added due to dummy creation, for the binary variables, and rename
df2 = df2.drop(['gender_male', 'lunch_free/reduced', 'course_none'], axis=1)
df2.rename(columns={'gender_female': 'gender', 'lunch_standard': 'standard lunch', 'course_completed': 'completed course'}, inplace=True)
df2.rename(columns={'race_group A': 'race A', 'race_group B': 'race B', 'race_group C': 'race C', 'race_group D': 'race D', 'race_group E': 'race E'}, inplace=True)

#do the same for target variable
enc_target = pd.get_dummies(df2['scoreclf'], prefix = 'course')
df2 = pd.concat((df2, enc_target), axis=1)
df2 = df2.drop(['scoreclf', 'course_below avg'], axis=1)
df2.rename(columns={'course_above avg': 'above avg score'}, inplace=True)

print(df2.head())


#Write to CSV V1:
#df2.to_csv('OnehotAll_1.csv', na_rep='UNKNOWN', index=False)

#Now, also remove the redundant race and education columns (any of the columns). This removes the dependency
#between the variables, i.e. the variables can be inferred through the other variables, creates correlation:
df3 = df2.drop(['race E', 'parent_some high school'], axis=1)
print(df3.head())

#And write to CSV V2:
#df3.to_csv('OnehotAll_2.csv', na_rep='UNKNOWN', index=False)
