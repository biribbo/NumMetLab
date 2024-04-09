import numpy as np
from scipy.interpolate import CubicSpline
import math

e = math.exp(1)
x = np.array([0, 1, 2, 3])
y = np.array([1, e, e**2, e**3])

spline = CubicSpline(x, y, bc_type='natural')
rounded_coefficients = np.round(spline.c, decimals=5)
c = rounded_coefficients

result = spline(5)
print(result)
print(c)