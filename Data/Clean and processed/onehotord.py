import pandas as pd
import numpy as np

from sklearn.preprocessing import OrdinalEncoder, LabelEncoder

df1 = pd.read_csv('Initial.csv')
print(df1.head())

#One hot encode all except parent edu:
enc_race = pd.get_dummies(df1['race/ethnicity'], prefix = 'race')
enc_gend = pd.get_dummies(df1['gender'], prefix = 'gender')
enc_lunch = pd.get_dummies(df1['lunch'], prefix = 'lunch')
enc_course = pd.get_dummies(df1['prep course'], prefix = 'course')

df2 = pd.concat((df1, enc_race, enc_gend, enc_lunch, enc_course), axis=1)

df2 = df2.drop(['gender', 'race/ethnicity', 'lunch', 'prep course'], axis=1)

#drop the extra variables added due to dummy creation, for the binary variables, and rename
df2 = df2.drop(['gender_male', 'lunch_free/reduced', 'course_none'], axis=1)
df2.rename(columns={'gender_female': 'gender', 'lunch_standard': 'standard lunch', 'course_completed': 'completed course'}, inplace=True)
df2.rename(columns={'race_group A': 'race A', 'race_group B': 'race B', 'race_group C': 'race C', 'race_group D': 'race D', 'race_group E': 'race E'}, inplace=True)

#do the same for target variable
enc_target = pd.get_dummies(df2['scoreclf'], prefix = 'course')
df2 = pd.concat((df2, enc_target), axis=1)
df2 = df2.drop(['scoreclf', 'course_below avg'], axis=1)
df2.rename(columns={'course_above avg': 'above avg score'}, inplace=True)

#Ordinl encode parent edu:
#enc = OrdinalEncoder()
#enc.fit(df2[['parent edu']])
#df2[['parent edu']] = enc.transform(df2[['parent edu']])

#Ordinal encode using pandas mapping:
mapping = {"some high school": 0, "high school": 1, "some college": 2, "associate's degree": 3, "bachelor's degree": 4, "master's degree": 5}
df2['parent edu'] = df2['parent edu'].map(lambda x: mapping[x])

print(df2.head(20))

#Write to CSV V1:
#df2.to_csv('OnehotOrd_1.csv', na_rep='UNKNOWN', index=False)


#Remove the redundant race column (race E)
df3 = df2.drop('race E', axis=1)
print(df3.head())

#And write to CSV V2:
#df3.to_csv('OnehotOrd_2.csv', na_rep='UNKNOWN', index=False)