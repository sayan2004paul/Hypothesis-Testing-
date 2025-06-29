# -*- coding: utf-8 -*-
"""Untitled24.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IJYzU2Cblx6rsmxRmZ-175tEWWSTpFXY
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

train=pd.read_csv('/content/train.csv').drop(columns=['Survived'])
test=pd.read_csv('/content/test.csv')

final_df=pd.concat([train,test]).sample(1309)

pop=final_df['Age'].dropna()

pop.mean()

sample_age

sample_age=pop.sample(25).values

# H0- the mean age is 35
# H1 - the mean age is less than 35

# checking for normality using shapiro wilk

from scipy.stats import shapiro

shapiro_age=shapiro(sample_age)
shapiro_age

pop_mean=29

from scipy.stats import stats

t_statistics,p_value=stats.ttest_1samp(sample_age,pop_mean)

t_statistics,p_value

alpha=0.05


if (p_value/2)<alpha:
  print('reject the null hypothesis ')
else:
  print('fail to reject H0')

