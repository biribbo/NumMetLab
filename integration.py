import numpy as np

def polynomial_function(x, coeffs):
    return np.polyval(coeffs, x)

x = np.array([0, 0.25, 0.5, 0.75, 1])
y = np.array([1, 1.015625, 1.125, 1.421875, 2])

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

trapezoidal_rule = round(trapezoidal_rule(x, y), 2)
simpsons_rule = round(simpsons_rule(x, y), 2)
print (trapezoidal_rule)
print (simpsons_rule)