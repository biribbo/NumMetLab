def horner_from_newton(b_array, x_array, s) :
    x_count = len(x_array)
    p = b_array.pop()
    for i in range(x_count):
        p = p*(s - x_array.pop()) + b_array.pop()
    return p

#stopien = int(input("Podaj stopień wielomianu: "))
print("Wielomian ma postać w(x) = b_0 + b_1(x - x_0) + b_2(x - x_0)(x - x_1)...")
b_array = [1, -0.16666666666666666, 0.016666666666666663] # enter the data manually, input currently broken
x_array = [1, 4]
punkt = float(input("Podaj punkt s: "))

'''
for i in range(stopien+1):
    b = float(input("Podaj b_{}: ".format(i)))
    b_array.append(b)

for i in range(stopien):
    x = float(input("Podaj x_{}: ".format(i)))
    x_array.append(x)
'''

result = horner_from_newton(b_array, x_array, punkt)
print("Wartość wielomianu w punkcie s:", result)