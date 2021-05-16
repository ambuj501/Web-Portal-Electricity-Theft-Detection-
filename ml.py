
import sys
#x = int(sys.argv[1])

import pandas as pd
import numpy as np
import pickle
from sklearn import svm
import warnings
from joblib import dump, load

data = pd.read_csv('data_final.csv')


data.drop(['Unnamed: 0'],axis=1,inplace=True)
#print(data)
YY = data['OutPut']

data.drop(['OutPut'],axis=1,inplace=True)
#print(data)
XX = np.array(data)
YY = np.array(YY)
#print(XX.shape)
#print(YY.shape)


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(XX, YY, test_size=0.1)

clf = load('CNN.joblib')

y_pred = clf.predict(x_test)

c = 0
for i in y_pred:
  c = c+1
  if(i==1):
    print(c, end = " ")
    print(round(i), end = " ")
    
