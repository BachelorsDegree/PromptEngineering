def get_integer_input():
    while True:
        user_input = input("Введите целое число: ")
        try:
            # Попробуем преобразовать ввод в целое число
            number = int(user_input)
            print(f"Вы ввели целое число: {number}")
            return number  # Возвращаем корректное значение
        except ValueError:
            print("Невозможно преобразовать введенное значение в целое число. Попробуйте еще раз.")
        except TypeError:
            print("Введено значение неподходящего типа. Попробуйте еще раз.")

if __name__ == "__main__":
    try:
        get_integer_input()
        
        # Пример, который вызывает TypeError
        # Создаем переменную, которая не может быть использована в int()
        invalid_value = "string" + 5  # Это вызовет TypeError
    except TypeError as e:
        print(f"Ошибка типа: {e}")
