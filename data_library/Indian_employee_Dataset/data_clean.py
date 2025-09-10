import numpy as np
import pandas as pd

df = pd.read_csv("indian_employees_unrealistic.csv")
print(df.head())


#checking the missing value
print("\n\nMissing values in each column")
print(df.isnull().sum())


#fill salary values which is missing
df['salary(INR)'].fillna(df['salary(INR)'].mean()) 
df['age'].fillna(df['age'].mean()) 
df['experience(Years)'].fillna(df['experience(Years)'].median()) 
df['performance_rating(5)'].fillna(df['performance_rating(5)'].median())
    

#infinite values replace with nan then fill with their average
df.replace([np.inf, -np.inf], np.nan, inplace=True)

df.fillna(df.mean(numeric_only=True))

#remove duplicate records
df.drop_duplicates()


#remove negative salaries
df['salary(INR)'] = np.where(df['salary(INR)'] < 0, df['salary(INR)'].mean(), df['salary(INR)'])

salary_mean = df['salary(INR)'].mean()
salary_std = df['salary(INR)'].std()
lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)

#remove rows where salary is too high or too low

df = df[(df['salary(INR)'] >= lower_bound) & (df['salary(INR)'] <= upper_bound)]

df.to_csv('cleaned_indian_employee_data.csv', index=False)

print("Data cleaning completed saved as 'cleaned_indian_employee_data.csv'")

