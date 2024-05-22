import numpy as np

def newton_method(f, der_f, x0, tol=1e-8, max_iter=100):
    x = x0
    counter = 0
    for _ in range(max_iter):
        counter += 1
        fx = f(x)
        der_fx = der_f(x)
        x = x - fx / der_fx
        fx = f(x)
        if abs(fx) < tol:
            return x, fx, counter
    raise ValueError("osiągnięto maksymalną liczbę iteracji")

def bisection_method(f, a, b, tol=1e-3, max_iter=100):
    if f(a) * f(b) > 0:
        raise ValueError("brak różnych znaków na końcach przedziałów")
    
    counter = 0
    for _ in range(max_iter):
        counter += 1 
        c = (a + b) / 2
        fc = f(c)
        if abs(fc) < tol:
            return c, fc, counter
        if f(a) * fc < 0:
            b = c
        else:
            a = c
    raise ValueError("osiągnięto maksymalną liczbę iteracji")

def secant_method(f, a, b, tol=1e-8, max_iter=100):
    counter = 0
    for _ in range(max_iter):
        counter += 1
        f_a = f(a)
        f_b = f(b)
        xk = b - f_b * (b - a) / (f_b - f_a)
        f_xk = f(xk)
        if abs(f_xk) < tol:
            return xk, f_xk, counter
        a = b
        b = xk
    raise ValueError("osiągnięto maksymalną liczbę iteracji")

def f(x):
    return x**3 - 7

def derivative(x):
    return 3 * x ** 2

'''
result = bisection_method(f, 1, 3)
a = result[0]
b = result[1]
c = result[2]

print(a, b, c)

result = newton_method(f, derivative, 2)
a = result[0]
b = result[1]
c = result[2]

print(a, b, c)

'''
result = secant_method(f, 1, 2)
a = result[0]
b = result[1]
c = result[2]

print(a, b, c)