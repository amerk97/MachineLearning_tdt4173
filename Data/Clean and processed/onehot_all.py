import pandas as pd
import numpy as np

#All variables shall be one-hot encoded, with no redundant columns
#Pandas approach will be used instead of OneHotEncoder from sklearn library

#Read the CSV created from the "initialpre.py" script
df1 = pd.read_csv('Initial.csv')
print(df1.head())

#Create dummy variables for all feature variables.
enc_edu = pd.get_dummies(df1['parent edu'], prefix = 'parent')
enc_race = pd.get_dummies(df1['race/ethnicity'], prefix = 'race')
enc_gend = pd.get_dummies(df1['gender'], prefix = 'gender')
enc_lunch = pd.get_dummies(df1['lunch'], prefix = 'lunch')
enc_course = pd.get_dummies(df1['prep course'], prefix = 'course')

#Concatenate dummy variables to our dataframe, to form a new dataframe df2
df2 = pd.concat((df1, enc_edu, enc_race, enc_gend, enc_lunch, enc_course), axis=1)

#drop the original columns, as we no longer need them
df2 = df2.drop(['gender', 'race/ethnicity', 'parent edu', 'lunch', 'prep course'], axis=1)

#drop the extra variables added due to dummy creation, for the binary variables
#Note that dummy creation makes one binary column for each category. We can remove one of the new
#columns, as it is redundant. E.g. since we remove race E, we know that if all other races are 0
#then it must mean that race E is 1, even though there is no own column for it.
df2 = df2.drop(['gender_male', 'lunch_free/reduced', 'course_none', 'parent_some high school', 'race_group E'], axis=1)

#Rename some columns for simplicity
df2.rename(columns={'gender_female': 'gender', 'lunch_standard': 'standard lunch', 'course_completed': 'completed course'}, inplace=True)
df2.rename(columns={'race_group A': 'race A', 'race_group B': 'race B', 'race_group C': 'race C', 'race_group D': 'race D'}, inplace=True)

#Do the same procedure for the target variable, "scoreclf"
enc_target = pd.get_dummies(df2['scoreclf'], prefix = 'course')
df2 = pd.concat((df2, enc_target), axis=1)
df2 = df2.drop(['scoreclf', 'course_below avg'], axis=1)
df2.rename(columns={'course_above avg': 'above avg score'}, inplace=True)

#The data should now be one-hot encoded:
print(df2.head())

#And write to a new CSV file named "OnehotAll.csv", which will be used in our model implementations:
df2.to_csv('OnehotAll.csv', na_rep='UNKNOWN', index=False)
