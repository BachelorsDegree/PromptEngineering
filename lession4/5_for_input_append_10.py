# Создаем пустой список
user_input_list = []

# Цикл для запроса ввода 10 раз
for i in range(10):
    user_input = input(f"Введите символ или цифру ({i+1}/10): ")
    user_input_list.append(user_input)

# Выводим итоговый список
print("Введенные символы/цифры:", user_input_list)