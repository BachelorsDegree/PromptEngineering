import re


def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    return result

# Получение пользовательского ввода
try:
    a = float(input("Введите значение для a: "))
    b = float(input("Введите значение для b: "))
    
    # Вызов функции и вывод результата
    result = safe_divide(a, b)
    if result is None:
        print("Ошибка: деление на ноль.")
        #print(result)
    else:
        print(f"Результат деления {a} на {b} равен: {result}")
except ValueError:
    print("Введены некорректные данные. Пожалуйста, вводите числовые значения.")