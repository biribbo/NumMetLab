from tokenize import Double


def horner_from_newton(x_count, b_array, x_array, s) :
    p = b_array.pop()
    for i in range(x_count):
        p = p*(s - x_array.pop()) + b_array.pop()
    return p

stopien = int(input("Podaj stopień wielomianu: "))
print("Wielomian ma postać w(x) = b_0 + b_1(x - x_0) + b_2(x - x_0)(x - x_1)...")
b_array = []
x_array = []
punkt = float(input("Podaj punkt s: "))

for i in range(stopien+1):
    b = float(input("Podaj b_{}: ".format(i)))
    b_array.append(b)

for i in range(stopien):
    x = float(input("Podaj x_{}: ".format(i)))
    x_array.append(x)

result = horner_from_newton(stopien, b_array, x_array, punkt)
print("Wartość wielomianu w punkcie s:", result)