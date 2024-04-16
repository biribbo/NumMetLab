import numpy as np
from scipy.interpolate import CubicSpline
import math
import re

e = math.exp(1)
x = np.array([3.0, 4.5, 7.0, 9.0])
y = np.array([2.5, 1.0, 2.5, 0.5])

spline = CubicSpline(x, y, bc_type='natural')
rounded_coefficients = np.round(spline.c, decimals=5)
c = rounded_coefficients

n = len(x) - 1
m = len(c) - 1

result = spline(5)
print(result)

for i in range(n):
    p = ""
    p += str(c[m][i])
    poly = "(x - {})".format(x[i])
    for j in range(m-1, -1, -1):
        p += " + " + str(c[j][i]) + poly + "^" + str(m - j)
    p = p.replace("+ -", "- ")
    p = p.replace("(x - 0)", "x")
    p = p.replace("^1", "")
    
    print(p)