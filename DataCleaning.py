#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 12:38:06 2021

@author: roywong

"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Top News dataset
df = pd.read_csv("/Users/roywong//Desktop/Work_Stuff/PythonPortfolio/12.StockNews/Combined_News_DJIA.csv")


# Dow Jones Industrial Average Stock prices dataset
df_price = pd.read_csv("/Users/roywong//Desktop/Work_Stuff/PythonPortfolio/12.StockNews/upload_DJIA_table.csv")


# Merging the 2 dataframe
df_merge = df.merge(df_price, how='inner', on='Date')



# Combining the top news headlines
headlines = []

for row in range(0, len(df_merge.index)):
    headlines.append(' '.join( str(x) for x in df_merge.iloc[row, 2:27]) )



# cleaning the new headlines 
import re

clean_headlines = []

# removing b'
for i in range(0, len(headlines)):
    
    # removing b'
    clean_headlines.append(re.sub("b[(')]", '', headlines[i]))
    
    # removing b"
    clean_headlines[i] = re.sub('b[(")]', '', clean_headlines[i])
    
    # removing \'
    clean_headlines[i] = re.sub("\'", '', clean_headlines[i])
    
    

# add the clean headlines to the df_merge
df_merge['Combined_News'] = clean_headlines


# save the new dataset
df_merge.to_csv("combinedData.csv", index=False)

