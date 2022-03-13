import numpy as np

def create_matrix(items, data_length):
    # get polynomial of matrix
    x = len(items)
    n = int((x - 1) / 3)
    
    # filter items X
    dataX = items.copy()
    dataX.pop(1)
    del dataX[-n:]
    
    # filter items Y
    dataY = items.copy()
    dataY.pop(0)
    del dataY[1:-n]
    
    # create zeros matrix
    rows = n + 1
    cols = n + 2
    # matrix = np.zeros((rows, cols))
    
    matrix = np.zeros((rows, cols))
    # matrix = matrix.tolist()
    
    matrix[0][0] = data_length
    
    # insert items X
    _c = 0
    for i in range(rows):
        c = _c
        for j in range(cols-1):
            if(matrix[i][j] == 0):
                matrix[i][j] = dataX[c]
                c += 1
        if i != 0:
            _c += 1
    
    # insert items Y
    for i in range(rows):
        matrix[i][-1] = dataY[i]
    
    return matrix


'''
x = (n * 3) + 1
n = (x - 1) / 3

x = length list sums of data with 'n' polynom
n = polynom degree

[x, y, x^2, x^3, x^4, x*y, x^2*y] -> 7
polynom 2 ==> 2 x 3 + 1 = 7
reverse = (7 - 1) / 3 = 2
MATRIX = [
    [ jumlah_data , SUM(x)   , SUM(x^2) , SIGMA(y)     ],
    [ SUM(x)      , SUM(x^2) , SUM(x^3) , SIGMA(x.y)   ],
    [ SUM(x^2)    , SUM(x^3) , SUM(X^4) , SIGMA(x^2.y) ]
]

[x, y, x^2, x^3, x^4, x^5, x^6, x*y, x^2*y, x^3*y] -> 10
polynom 3 ==> 3 x 3 + 1 = 10
reverse = (10 - 1) / 3 = 3
MATRIX = [
    [ jumlah_data , SUM(x)   , SUM(x^2) , SUM(x^3) , SIGMA(y)     ],
    [ SUM(x)      , SUM(x^2) , SUM(x^3) , SUM(x^4) , SIGMA(x.y)   ],
    [ SUM(x^2)    , SUM(x^3) , SUM(X^4) , SUM(x^5) , SIGMA(x^2.y) ]
    [ SUM(x^3)    , SUM(x^4) , SUM(X^5) , SUM(x^6) , SIGMA(x^3.y) ]
]

[x, y, x^2, x^3, x^4, x^5, x^6, x^7, x^8, x*y, x^2*y, x^3*y, x^4*y] -> 13
polynom 4 ==> 4 x 3 + 1 = 13
reverse = (13 - 1) / 3 = 4
MATRIX = [
    [ jumlah_data , SUM(x)   , SUM(x^2) , SUM(x^3) , SUM(x^4) , SIGMA(y)     ],
    [ SUM(x)      , SUM(x^2) , SUM(x^3) , SUM(x^4) , SUM(x^5) , SIGMA(x.y)   ],
    [ SUM(x^2)    , SUM(x^3) , SUM(X^4) , SUM(x^5) , SUM(x^6) , SIGMA(x^2.y) ]
    [ SUM(x^3)    , SUM(x^4) , SUM(X^5) , SUM(x^6) , SUM(x^7) , SIGMA(x^3.y) ]
    [ SUM(x^4)    , SUM(x^5) , SUM(X^6) , SUM(x^7) , SUM(x^8) , SIGMA(x^4.y) ]
]

'''