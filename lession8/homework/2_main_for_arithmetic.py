import modules.arithmetic as arithmetic

def main():
    # Запрашиваем у пользователя целые числа для a и b
    a = int(input("Введите целое число для a: "))
    b = int(input("Введите целое число для b: "))

    # Примеры использования функций из модуля arithmetic
    print(f"{a} + {b} = {arithmetic.add(a, b)}")
    print(f"{a} - {b} = {arithmetic.subtract(a, b)}")
    print(f"{a} * {b} = {arithmetic.multiply(a, b)}")
    try:
        print(f"{a} / {b} = {arithmetic.divide(a, b)}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()