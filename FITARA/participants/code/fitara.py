# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 17:29:22 2019

@author: Alex Sherman (alsherman@deloitte.com)
"""

import os
import pandas as pd

ROOT_DIR = r'C:\Users\alsherman\Desktop\FITARA\competition_assets\participants'
TRAIN_LABELS = os.path.join(ROOT_DIR, r'train\labels\labels.csv')
TRAIN_TEXT = os.path.join(ROOT_DIR, r'train\extracted_data\extract_combined.csv')
TEST_TEXT = os.path.join(ROOT_DIR, r'test\extracted_data\extract_combined.csv')

# read in training and testing data
# one dataframe for labels another for text features
train_labels_df = pd.read_csv(TRAIN_LABELS, usecols=['document_name','is_fitara'])
train_text_df = pd.read_csv(TRAIN_TEXT)
test_df = pd.read_csv(TEST_TEXT)

# combine labels with text features
train_df = pd.merge(
    train_labels_df, 
    train_text_df, 
    on='document_name', 
    how='inner'
)

# remove dataframes that are no longer needed from memory 
del train_labels_df
del train_text_df

# confirm class distribution
# is_fitara - yes: ~29%; no: ~71%
train_df['is_fitara'].value_counts(normalize=True)
