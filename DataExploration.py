#!/usr/bin/env python
# coding=utf8
#########################################
# Date: April 25th 2018
# Author: Huang Zhiyong
# Description: explore train data with pandas module

import pandas as pd

# Data import
data_path = "train.csv"
train_data = pd.read_table(data_path, sep=",")

# Data description
print