import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

df = pd.read_csv('indians-diabetes.csv', names=names)

def stratified_split(y, proportion=0.8):
    y = np.array(y)

    train_inds = np.zeros(len(y), dtype=bool)
    test_inds = np.zeros(len(y), dtype=bool)

    values = np.unique(y)
    for value in values:
        value_inds = np.nonzero(y == value)[0]
        np.random.shuffle(value_inds)

        n = int(proportion * len(value_inds))

        train_inds[value_inds[:n]] = True
        test_inds[value_inds[n:]] = True

    return train_inds, test_inds

train, test = stratified_split(df['class'])

X_train = df.iloc[train, 0:8]
X_test = df.iloc[test, 0:8]

y_train = df['class'][train]
y_test = df['class'][test]

logreg = LogisticRegression()

logreg.fit(X_train,y_train)

def accuracy(y_test, y_pred):
    return 1 - sum(abs(y_test - y_pred)/len(y_test))



y_pred=logreg.predict(X_test)

print(accuracy(y_test, y_pred))
