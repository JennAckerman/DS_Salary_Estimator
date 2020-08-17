# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 18:01:58 2020

@author: Jen butt
"""


import pandas as pd

df = pd.read_csv('Jobs_list.csv')

#salary parsing


df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided' in x.lower() else 0)


df = df[df['Salary Estimate']!= '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

min_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary',''))

df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary+df.max_salary)/2

#company name text only
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating']<0 else x['Company Name'][:-3], axis = 1)

#state field

df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])


#age of company
df['age'] = df.Founded.apply(lambda x: x if x<1 else 2020-x)

#parsing of job description (python, etc.)
skills = ['python','sql','excel','aws','spark','nlp','R']
for skill in skills:
    df[skill + '_yn'] = df['Job Description'].apply(lambda x: 1 if skill in x.lower() else 0)
    
df.columns
df_out = df.drop(['Unnamed: 0'], axis = 1)
df_out.to_csv('Salary_data_cleaned.csv', index = False)

pd.read_csv('Salary_data_cleaned.csv')