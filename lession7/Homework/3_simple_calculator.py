try:
    user_input = input("Введите операцию (например, 3 + 4): ")
    num1, operator, num2 = user_input.split()

    # Преобразуем введенные значения в числа
    num1 = float(num1)
    num2 = float(num2)

    # Выполняем операцию в зависимости от оператора
    if operator == "+":
        result = num1 + num2
        print(f"Результат: {result}")
    elif operator == "-":
        result = num1 - num2
        print(f"Результат: {result}")
    elif operator == "*":
        result = num1 * num2
        print(f"Результат: {result}")
    elif operator == "/":
        # Обработка деления на ноль
        if num2 == 0:
            raise ZeroDivisionError("Ошибка: Деление на ноль невозможно.")
        result = num1 / num2
        print(f"Результат: {result}")
    else:
        print("Ошибка: Неподдерживаемый оператор. Используйте +, -, * или /.")

except ValueError:
    print("Ошибка: Невозможно преобразовать введенные значения в числа. Убедитесь, что вы вводите числа корректно.")
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(f"Произошла ошибка: {e}")


#Способ2

#user_input = input("Введите операцию")
#num1, operator, num2 = user_input.split()

#num1 = float(num1)
#num2 = float(num2)

#if operator == "+":
#    result = num1 + num2
#    print(result)
#elif operator == "-":
#    result = num1 - num2
#    print(result)
#elif operator == "*":
#    result = num1 * num2
#    print(result)
#elif operator == "/":
#    result = num1 / num2
#    print(result)




#Способ1
# number1 = int(input("введите число - "))
# s = input("введите знак математической операции - ")
# number2 = int(input("введите число - "))

# if s == "+":
#     print(number1 + number2)
# elif s == "-":
#     print(number1 - number2)
# elif s == "*":
#     print(number1 * number2)
# elif s == "/":
#     print(number1 / number2)
