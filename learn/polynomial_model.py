from copy import deepcopy
import numpy as np
import learn.matrix_poly as mp
from learn.gauss import gauss


class PolynomialRegression:

    def __init__(self, X_train=[], y_train=[], poly=2, copy=True):
        self.__copy = copy
        self.__poly = poly
        self.__copy_data(X_train, y_train)

    def __copy_data(self, X_train, y_train):
        if self.__copy is True:
            self.__X_train = deepcopy(X_train)
            self.__y_train = deepcopy(y_train)
        else:
            self.__X_train = X_train
            self.__y_train = y_train

    def fit_data(self, X_train, y_train, poly=2):
        self.__copy_data(np.array(X_train), np.array(y_train))
        self.__poly = poly

        self.__calc()
        self.__train()

    def __calc(self):
        X = self.__X_train
        y = self.__y_train

        data_length = len(X)
        poly = self.__poly

        sums_data = self.__regPoly(X, y, poly)
        matrix = mp.create_matrix(sums_data, data_length)
        self.coef = gauss(matrix)

    def __regPoly(self, X_data, y_data, poly):
        sums_data = []
        sums_data.append(sum(X_data))
        sums_data.append(sum(y_data))

        '''
        sums Exponentiation of x 
        " x^2, x^3, ..., x^n "
        n = number of polynomial
        '''
        for i in range(1, poly*2):
            sums_data.append(sum(X_data**(i+1)))

        '''
        sums Exponentiation of x and y
        " x*y, x^2*y, ..., x^n*y "
        n = number of polynomial
        '''
        for i in range(1, poly+1):
            sums_data.append(sum((X_data**i)*y_data))

        return sums_data

    def __train(self):
        X = self.__X_train
        y = self.__y_train
        coef = self.coef
        
        X_result, y_result = [], []
        self.errortrain = []
        
        data_length = len(X)
        
        for i in range(data_length):
            y_predic = self.__poly_nth(coef, X[i])
            y_actual = y[i]
            
            self.errortrain.append( (y_actual - y_predic)**2 )
            
            y_result.append(y_predic)
            X_result.append(X[i])
            
        self.__X_result = X_result
        self.__y_result = y_result
        
    def __poly_nth(self, coef, X):
        y = 0
        exp = len(coef) - 1
        for i in range(len(coef)):
            y = y + (coef[i] * (X**exp))
            exp -= 1
            
        return y

    def trained(self):
        return self.__X_result, self.__y_result
    
    
    def predic(self, X):
        coef = self.coef
        if type(X) != type(np.array([])):
            X = np.array(X)
        result = self.__poly_nth(coef, X)
        return result.tolist()
