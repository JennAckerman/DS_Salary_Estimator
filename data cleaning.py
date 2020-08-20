# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 18:01:58 2020

@author: Jen butt
"""


import pandas as pd
import re


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
skills = ['python','sql','excel','aws','spark','nlp','r studio']
for skill in skills:
    df[skill + '_yn'] = df['Job Description'].apply(lambda x: 1 if skill in x.lower() else 0)   

#Minimum Degree Requirements
    
def min_degree(desc):
    if 'bach' in desc.lower() or 'bs' in desc.lower() or 'b.s' in desc.lower():
        return 'Bachelors'
    elif 'master' in desc.lower() or 'ms' in desc.lower() or 'm.s'in desc.lower():
        return 'Masters'
    elif 'doctor' in desc.lower() or 'phd' in desc.lower() or 'ph.d' in desc.lower():
        return 'PH.d'
    else:
        return 'na'
    
df['min_degree'] = df['Job Description'].apply(min_degree)

#Simplifying Job Titles
def title_simplifier(title):
    if 'data scientist' in title.lower():
        return 'data scientist'
    elif 'data engineer' in title.lower():
        return 'data engineer'
    elif 'analyst' in title.lower():
        return 'analyst'
    elif 'machine learning' in title.lower():
        return 'ML Engineer'
    elif 'manager' in title.lower():
        return 'manager'
    elif 'director' in title.lower():
        return 'director'
    else:
        return 'na'
    
df['job_simp'] = df['Job Title'].apply(title_simplifier)

#Seniority in Job Titles

def seniority(title):
    if 'sr' in title.lower() or 'senior' in title.lower() or 'sr' in title.lower() or 'lead' in title.lower() or 'principal' in title.lower() or 'vice' in title.lower():
        return 'senior'
    elif 'junior' in title.lower() or 'jr.' in title.lower() or 'jr' in title.lower():
        return 'junior'
    else:
        return 'na'
df['job_sin'] = df['Job Title'].apply(seniority)

df.columns

df = df[['Unnamed: 0', 'company_txt', 'job_simp','Job Description',
       'Salary Estimate', 'Rating', 'Location','job_state', 'Size', 'Founded',
       'Type of ownership', 'Industry', 'Sector', 'Revenue', 'hourly',
       'employer provided', 'min_salary', 'max_salary', 'avg_salary',
        'min_degree', 'age', 'python_yn', 'sql_yn', 'excel_yn',
       'aws_yn', 'spark_yn', 'nlp_yn', 'r studio_yn',
       'job_sin', 'Company Name', 'Job Title']]
      
df_out = df.drop(['Unnamed: 0'], axis = 1)
df_out.to_csv('Salary_data_cleaned.csv', index = False)

pd.read_csv('Salary_data_cleaned.csv')