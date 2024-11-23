import math

a = float(input("Введите длину катета a: "))
b = float(input("Введите длину катета b: "))

#с = math.sqrt(a**2 + b**2)
c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))

print(f"Длина гипотенузы c равна: {с}")