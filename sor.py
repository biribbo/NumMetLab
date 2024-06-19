import numpy as np

def sor(A, b, omega, tol=1e-10, max_iterations=1000):
    """
    Successive Over-Relaxation (SOR) method to solve Ax = b.
    
    Parameters:
        A : 2D numpy array
            Coefficient matrix.
        b : 1D numpy array
            Right-hand side vector.
        omega : float
            Relaxation parameter.
        tol : float, optional
            Tolerance for convergence.
        max_iterations : int, optional
            Maximum number of iterations.

    Returns:
        x : 1D numpy array
            Solution vector.
        iterations : int
            Number of iterations performed.
    """
    n = len(b)
    x = np.zeros_like(b)
    
    for k in range(max_iterations):
        x_new = np.copy(x)
        
        for i in range(n):
            sigma = np.dot(A[i, :i], x_new[:i]) + np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (1 - omega) * x[i] + (omega / A[i, i]) * (b[i] - sigma)
        
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, k
        
        x = x_new
    
    raise Exception("SOR did not converge")

def opt_omega(matrix):
    D = np.diag(np.diag(A))
    L = np.tril(A, -1)
    U = np.triu(A, 1)
    
    T_gs = np.linalg.inv(D + L) @ (-U)  # Iteration matrix for Gauss-Seidel
    
    eigenvalues = np.linalg.eigvals(T_gs)
    lambda_max = max(abs(eigenvalues))
    
    omega_opt = 2 / (1 + np.sqrt(1 - lambda_max**2))
    
    return omega_opt

# Example usage
A = np.array([[4, -1, 0],
              [-1, 4, -1],
              [0, -1, 4]], dtype=float)

b = np.array([2, 6, 2], dtype=float)

omega = opt_omega(A)
tol = 1e-10
max_iterations = 1000

solution, iterations = sor(A, b, omega, tol, max_iterations)
print("Solution:", solution)
print("Iterations:", iterations)
print("Omega:", omega)