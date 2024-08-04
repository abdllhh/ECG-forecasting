!pip install darts
import numpy as np
import pandas as pd
from darts import TimeSeries
from darts.ad import ForecastingAnomalyModel, NormScorer
from darts.models import TCNModel

df_train = pd.read_csv('ECG5000_TRAIN.txt')
print(df_train)
shape_train = df_train.shape
print(shape_train)

df_test = pd.read_csv('ECG5000_TEST.txt')
shape_test = df_test.shape
print(shape_test)
print(df_test)
null_values = df_test.isnull()
print("Null values in each column:")
print(null_values.sum())


print("Summary statistics for Training Data:")
print(df_train.describe())
