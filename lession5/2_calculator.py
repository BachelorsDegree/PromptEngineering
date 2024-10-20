def calculator():
    # Запрашиваем у пользователя ввод в формате "число1 операция число2"
    user_input = input("Введите выражение (например, '2 + 2'): ")

    # Разбиваем строку на составляющие
    parts = user_input.split()

    # Проверяем, что введены правильные данные
    if len(parts) != 3:
        print("Ошибка: введите выражение в формате 'число1 операция число2'.")
        return

    try:
        number1 = float(parts[0])
        operation = parts[1]
        number2 = float(parts[2])
    except ValueError:
        print("Ошибка: убедитесь, что введены корректные числа.")
        return

    # Выполняем операцию
    if operation == '+':
        result = number1 + number2
    elif operation == '-':
        result = number1 - number2
    elif operation == '*':
        result = number1 * number2
    elif operation == '/':
        if number2 == 0:
            print("Ошибка: деление на ноль.")
            return
        result = number1 / number2
    else:
        print("Ошибка: неизвестная операция.")
        return

    # Выводим результат
    print(f"Результат: {result}")

# Запускаем калькулятор
calculator()