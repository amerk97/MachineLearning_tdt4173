import pandas as pd
import numpy as np

#Read the csv "Initial.csv" created by running the script "initialpre.py"
df1 = pd.read_csv('Initial.csv')
print(df1.head())

#One hot encode all feature variables except parent edu:
enc_race = pd.get_dummies(df1['race/ethnicity'], prefix = 'race')
enc_gend = pd.get_dummies(df1['gender'], prefix = 'gender')
enc_lunch = pd.get_dummies(df1['lunch'], prefix = 'lunch')
enc_course = pd.get_dummies(df1['prep course'], prefix = 'course')

#Concatenate the dummy variables to df1, creating a new dataframe df2
df2 = pd.concat((df1, enc_race, enc_gend, enc_lunch, enc_course), axis=1)

#Drop the original columns from the raw data
df2 = df2.drop(['gender', 'race/ethnicity', 'lunch', 'prep course'], axis=1)

#drop the extra variables added due to dummy creation, for the binary variables
#Note that dummy creation makes one binary column for each category. We can remove one of the new
#columns, as it is redundant. E.g. since we remove race E, we know that if all other races are 0
#then it must mean that race E is 1, even though there is no own column for it.
df2 = df2.drop(['gender_male', 'lunch_free/reduced', 'course_none', 'race_group E'], axis=1)

#Rename some for simplicity
df2.rename(columns={'gender_female': 'gender', 'lunch_standard': 'standard lunch', 'course_completed': 'completed course'}, inplace=True)
df2.rename(columns={'race_group A': 'race A', 'race_group B': 'race B', 'race_group C': 'race C', 'race_group D': 'race D'}, inplace=True)

#do the same procedure for target variable, one-hot encoding:
enc_target = pd.get_dummies(df2['scoreclf'], prefix = 'course')
df2 = pd.concat((df2, enc_target), axis=1)
df2 = df2.drop(['scoreclf', 'course_below avg'], axis=1)
df2.rename(columns={'course_above avg': 'above avg score'}, inplace=True)

#Ordinal encode parental eduction using Pandas mapping. Could also have used sklearn's labelencoder or ordinalencoder.
mapping = {"some high school": 0, "high school": 1, "some college": 2, "associate's degree": 3, "bachelor's degree": 4, "master's degree": 5}
df2['parent edu'] = df2['parent edu'].map(lambda x: mapping[x])

#The data should be processed, where everything is one-hot encoded except parental education, which is ordinal encoded:
#df.head was used throughout the code simply to check if everything was executed as expected.
print(df2.head(20))

#And write to a new csv file, called "OnehotOrd.csv", for use in our model implementation:
df2.to_csv('OnehotOrd.csv', na_rep='UNKNOWN', index=False)
