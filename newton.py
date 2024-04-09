def newton_matrix(x, y):
    n = len(x)
    F = [[None] * n for _ in range(n)]

    for i in range(n):
        F[i][0] = y[i]

    for j in range(1, n):
        for i in range(n - j):
            F[i][j] = (F[i + 1][j - 1] - F[i][j - 1]) / (x[i + j] - x[i])

    return [F[0][i] for i in range(n)]

def newton_interpolation_polynomial(x, y):
    n = len(x)
    a = newton_matrix(x, y)
    p = str(y[0])
    for i in range(1, n):
        p += " + {}".format(a[i])
        for j in range(i):
            p += "(x - {})".format(x[j])
    return p

wezly = int(input("Podaj ilość węzłów: "))
x_array = []
y_array = []

for i in range(wezly):
    x = float(input("Podaj x_{}: ".format(i)))
    x_array.append(x)

for i in range(wezly):
    y = float(input("Podaj y_{}: ".format(i)))
    y_array.append(x)

result = newton_interpolation_polynomial(x_array, y_array)
print(result)