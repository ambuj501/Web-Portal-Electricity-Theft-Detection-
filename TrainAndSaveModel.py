import sys
#x = int(sys.argv[1])
x = int(20)
import pandas as pd
import numpy as np
import pickle
from sklearn import svm
import warnings
data = pd.read_csv('data_final.csv')

data.drop(['Unnamed: 0'],axis=1,inplace=True)
#print(data)
YY = data['OutPut']

data.drop(['OutPut'],axis=1,inplace=True)
#print(data)
XX = np.array(data)
YY = np.array(YY)
print(XX.shape)
print(YY.shape)
#print(YY)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(XX, YY, test_size=0.1)
print("Data spilted")
clf = svm.SVC()
clf.fit(x_train, y_train)

print("MOdel Fitted")
from joblib import dump, load
dump(clf, 'SVM.joblib')

print("model saved")
clf = load('SVM.joblib')

y_pred = clf.predict(x_test)
print(y_pred)


