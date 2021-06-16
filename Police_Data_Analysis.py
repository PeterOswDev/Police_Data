import pandas as pd
import numpy as np

desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',20) # Shows all columns
data = pd.read_csv(r"E:\3. Police Data.csv")
print(data)
print(data.isnull())
print(data.isnull().sum())
print(data.drop(columns = 'country_name'))# df = data frame, remove the column that only contains missing values
print(data)
print(data.drop(columns = 'country_name', inplace=True)) #Permanent remove
print(data)
#For speeding, were men or Women stopped more often
print(data.head())
print(data[data.violation=='Speeding'])
print(data[data.violation=='Speeding'].driver_gender.value_counts())
#Does gender affect who gets searched during the stop
print(data.head())
print(data.groupby('driver_gender').search_conducted.sum())
print(data.search_conducted.value_counts())
#What is the mean stop_duration?
print(data.head())
print(data.stop_duration.value_counts())
#print(  data['stop_duration'].map( {'0-15 Min' : 7.5, '16-30 Min' : 24, '30+ Min' : 45 }))
#print(data['stop_duration'] = data['stop_duration'].map( {'0-15 Min' : 7.5, '16-30 Min' : 24, '30+ Min' : 45 }))#check it
print(data)
#print(data['stop_duration'].mean()) #check it
#Compare the age distributions for each violation
print(data.head())
print(data.groupby('violation').driver_age.describe())