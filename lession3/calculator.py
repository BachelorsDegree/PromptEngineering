def add(x, y):
    return round((x + y),1)

def subtract(x, y):
    return round((x - y),1)

def multiply(x, y):
    return round((x * y),1)

def divide(x, y):
    if y == 0:
        return "Ошибка: деление на ноль"
    return round((x / y),1)

def floordiv(x, y):
    if y == 0:
        return "Ошибка: деление на ноль"
    return round((x // y),1)

def modulus(x, y):
    if y == 0:
        return "Ошибка: деление на ноль"
    return round((x % y),1)

def power(x, y):
    return round((x ** y),1)

def calculator():
    while True:
        print("\nВыберите операцию:")
        print("1: Сложение")
        print("2: Вычитание")
        print("3: Умножение")
        print("4: Деление")
        print("5: Целая часть от деления")
        print("6: Остаток от деления")
        print("7: Возведение в степень")
        print("8: Выход")

        choice = input("Введите номер операции (1/2/3/4/5/6/7/8): ")

        if choice == '8':
            print("Выход из программы.")
            break

        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: пожалуйста, введите числовые значения.")
            continue

        if choice == '1':
            print(f"Результат: {add(num1, num2)}")
        elif choice == '2':
            print(f"Результат: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Результат: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Результат: {divide(num1, num2)}")
        elif choice == '5':
            print(f"Результат: {floordiv(num1, num2)}")
        elif choice == '6':
            print(f"Результат: {modulus(num1, num2)}")
        elif choice == '7':
            print(f"Результат: {power(num1, num2)}")
        else:
            print("Неправильный ввод")

if __name__ == "__main__":
    calculator()




