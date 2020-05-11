from pyspark.ml import Pipeline
import numpy as np
import pandas as pd

def read_data(user):
    
    if user == 'Brian':
    
        datadir = '/Users/BrianTCook/Desktop/quora-question-pairs/'
    
    train_df = pd.read_csv(datadir+'train.csv')
    test_1_df = pd.read_csv(datadir+'test.csv')
    test_2_df = pd.read_csv(datadir+'test_2.csv')
    
    return train_df, test_1_df, test_2_df

if __name__ in '__main__':
    
    user = 'Brian' #'Yuchi', 'Murad'
    train, test_1, test_2 = read_data(user)
    
    print('hello, world!')
