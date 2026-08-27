
import numpy as np

def gauss_elimination(a_matrix, b_matrix):
    if a_matrix.shape[0] != a_matrix.shape[1]:
        print("Matrix is not a square matrix")
        return
    
    
    n = len(b_matrix)
    x = np.zeros(n)
    
    
    augmented_matrix = np.concatenate((a_matrix.astype(float), b_matrix.reshape(n, 1).astype(float)), axis=1)
    
    '''Forward elimination'''
    for i in range(n):
        if augmented_matrix[i][i] == 0.0:
            print("Divide by zero error")
            return
            
        for j in range(i + 1, n):
            s_f = augmented_matrix[j][i] / augmented_matrix[i][i]
            augmented_matrix[j] = augmented_matrix[j] - (s_f * augmented_matrix[i])
    
    

    '''Backward Substitution'''
    
    x[n-1] = augmented_matrix[n-1][n] / augmented_matrix[n-1][n-1]
    
    
    for k in range(n-1, -1, -1):
        x[k] = augmented_matrix[k][n]
        for j in range(k+1, n):
            x[k] = x[k] - augmented_matrix[k][j] * x[j]
        x[k] = x[k] / augmented_matrix[k][k]
    
    for ans in range(n):
        print(f"x{ans} is {x[ans]}")
    
    return x
    
A=np.array([[3,2,-1], [2,-2,4],[-1,0.5,-1]])
B=np.array([1,-2,0])
gauss_elimination(A,B)