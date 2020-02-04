# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 16:03:51 2020

@author: DIPAK
"""

import pandas as pd

housing_dataframe = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv", sep=",")
housing_dataframe.describe()

