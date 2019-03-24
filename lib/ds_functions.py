#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 16:59:04 2019

@author: paulburgoine
"""

import pandas as pd
import numpy as np

### Function to provide an overview of a dataframe

def describe_data(df, head = 5):
    
    # df   = pandas datframe
    # head = no of rows to display in head
    
    pd.options.display.float_format = "{:.2f}".format
    
    # head
    print('Head:')
    display(df.head(head))
    print('')
    
    # num rows
    print('Num Rows: ', df.index.size)
    print('')
    
    # data types
    print('Data Types:')
    print('')
    print(df.dtypes)
    print('')
    
    # describe columns
    print('Categorical Columns (type = object):')
    #display(df.select_dtypes('object').describe().T.round(2))
    print('')
    print('Numeric Columns:')
    display(df.describe().T.round(2))
    print('')
    
    # missing values - counts missing values by column
    print('Missing Values: ')
    print('')
    n_nulls = df.isnull().sum()
    mask = n_nulls > 0
    print(n_nulls[mask])