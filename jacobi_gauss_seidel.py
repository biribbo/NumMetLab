import numpy as np

def jacobi(A, b, x0, tol, max_iter):
    n = len(b)
    x = x0.copy()
    x_new = np.zeros_like(x0)
    
    for itgs in range(max_iter):
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
        
        if np.linalg.norm(A @ x_new - b) <= tol:
            return x_new, itgs + 1
        
        x = x_new.copy()
    
    return x, max_iter

def gauss_seidel(A, b, x0, tol, max_iter):
    n = len(b)
    x = x0.copy()
    
    for itgs in range(max_iter):
        for i in range(n):
            s1 = sum(A[i][j] * x[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x[i] = (b[i] - s1 - s2) / A[i][i]
        
        if np.linalg.norm(A @ x - b) <= tol:
            return x, itgs + 1
    
    return x, max_iter

# Przykładowe dane wejściowe
A = np.array([[3, 1, 1], 
              [-1, 4, -1], 
              [0.5, 0.5, 2]], dtype=float)

b = np.array([5, 2, 3], dtype=float)

x0 = np.zeros(len(b))
tol = 1e-5
max_iter = 100

# Metoda Jacobi'ego
x_jacobi, iters_jacobi = jacobi(A, b, x0, tol, max_iter)
print(f'Metoda Jacobi\'ego: x = {x_jacobi}, liczba iteracji = {iters_jacobi}')

# Metoda Gaussa-Seidla
x_gauss_seidel, iters_gauss_seidel = gauss_seidel(A, b, x0, tol, max_iter)
print(f'Metoda Gaussa-Seidla: x = {x_gauss_seidel}, liczba iteracji = {iters_gauss_seidel}')
