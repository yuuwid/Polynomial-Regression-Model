import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from learn.split_data import split
from learn.polynomial_model import PolynomialRegression
import learn.error_score as score


df = pd.read_csv('data/data1.csv')
X = df['x'].values
y = df['y'].values
X2 = df.iloc[:, :-1].values
y2 = df.iloc[:, 1].values

test_size = 0.2
data_length = len(X)
data_test_length = np.floor(data_length * test_size)
data_train_length = np.ceil(data_length - data_test_length)

X_train, X_test, y_train, y_test = split(X, y, test_size=test_size, 
                                         shuffle=True, sort=True)

polynom = 6
poly = PolynomialRegression()
poly.fit_data(X_train, y_train, poly=polynom)

print()
print('Data Train : ' + str(int(data_train_length)))
print('Data Test  : ' + str(int(data_test_length)))
print()
print('Coef       : ' + str(poly.coef))
print()

y_pred = poly.predic(X_test)
print('MAE score  : ' + str(score.mae_score(y_test, y_pred)))
print('MSE score  : ' + str(score.mse_score(y_test, y_pred)))
print('R2 Score   : ' + str(score.r2_score(y_test, y_pred)))
print()

df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df.head())

X_res, y_res = poly.trained()

plt.title('Student Scores')
plt.xlabel('Hours')
plt.ylabel('Scores')
plt.scatter(X2, y2, c='b', label='Data Train')
plt.scatter(X_test, y_test, c='g', label='Data Test')
plt.scatter(X_test, y_pred, c='y', label='Data Predic')

plt.plot(X_res, y_res, c='r', label='Polynomial')

plt.legend()
plt.show()