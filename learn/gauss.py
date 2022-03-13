import numpy as np

def gauss(matrix):
    n = len(matrix)
    
    for i in range(n):
        if matrix[i][i] == 0.0:
            pass
            
        for j in range(i+1, n):
            ratio = matrix[j][i]/matrix[i][i]
            
            for k in range(n+1):
                matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]

    x = np.zeros(n)
    
    # Back Substitution
    x[n-1] = matrix[n-1][n] / matrix[n-1][n-1]

    for i in range(n-2,-1,-1):
        x[i] = matrix[i][n]
        
        for j in range(i+1, n):
            x[i] = x[i] - matrix[i][j] * x[j]
        
        x[i] = x[i] / matrix[i][i]
        
    return np.flip(x)