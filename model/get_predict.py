# Standard python libraries
import warnings
import os
warnings.filterwarnings('ignore')
# Essential DS libraries
import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
import torch

# LightAutoML presets, task and report generation
from lightautoml.automl.presets.tabular_presets import TabularAutoML, TabularUtilizedAutoML
from lightautoml.tasks import Task
from lightautoml.report.report_deco import ReportDeco

import io
import pickle

N_THREADS = 4
N_FOLDS = 5
RANDOM_STATE = 42
TEST_SIZE = 0.2
TIMEOUT = 300
TARGET_NAME = '1'

def main():
    
    np.random.seed(RANDOM_STATE)
    torch.set_num_threads(N_THREADS)
    
    with open("../../model/model.pkl", "rb") as file:
        model = pickle.load(file)
    
    with open("row.txt", "r") as file:
        data = file.readline().strip()
    
    
    df = pd.read_csv(io.StringIO(data), header=None)
    
    df.columns = pd.Index(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13',
       '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25',
       '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37',
       '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49',
       '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61',
       '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73',
       '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85',
       '86', '87', '88', '89', '90'],
      dtype='object')
    result = model.predict(df)        
    print(result[0])

if __name__ == '__main__':
    main()