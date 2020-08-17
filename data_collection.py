# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 18:09:16 2020

@author: Jen butt
"""


import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/Jen butt/Desktop/R and Python/Glassdoor job/chromedriver"

df = gs.get_jobs('data scientist', 'Columbus, OH', 39, False, path, 15)

df.to_csv('C:/Users/Jen butt/Desktop/R and Python/Glassdoor job/DS-job-decision-tree/Jobs_list.csv')

