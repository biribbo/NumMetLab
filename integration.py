import numpy as np

def polynomial_function(x, coeffs):
    return np.polyval(coeffs, x)

x = np.array([1, 1.5, 2, 2.5, 3])
y = np.array([2, 5.75, 11, 17.75, 26])

# Złożona metoda trapezów
def trapezoidal_rule(x, y):
    n = len(x) - 1
    h = (x[-1] - x[0]) / n
    I = 0.5 * h * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
    return I

# Złożona metoda Simpsona
def simpsons_rule(x, y):
    n = len(x) - 1
    h = (x[-1] - x[0]) / n
    I = h / 3 * (y[0] + 2 * np.sum(y[2:n-1:2]) + 4 * np.sum(y[1:n:2]) + y[n])
    return I

trapezoidal_rule = trapezoidal_rule(x, y)
simpsons_rule = simpsons_rule(x, y)
print (trapezoidal_rule)
print (simpsons_rule)