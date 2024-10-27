a = int(input("введите число - "))
b = int(input("введите число - "))
c = int(input("введите число - "))

if a > b and a > c:
    print(f"самое большое число - {a}")
elif b > a and b > c:
    print(f"самое большое число - {b}")
elif c > a and c > b:
    print(f"самое большое число - {c}")
else:
    print("все числа равны")