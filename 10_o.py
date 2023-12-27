import math

def calculate_hypotenuse(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

a = float(input("Введите длину первого катета: "))
b = float(input("Введите длину второго катета: "))

hypotenuse = calculate_hypotenuse(a, b)
print("Длина гипотенузы:", hypotenuse)