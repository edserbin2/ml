#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 22:06:46 2019

@author: ed
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv('Data.csv')
# X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, -1].values
print(Y)