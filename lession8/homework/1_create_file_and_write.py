def write_user_input_to_file():
    # Запрашиваем у пользователя ввод текста
    user_input = input("Введите текст, который вы хотите записать в файл: ")
    
    # Открываем файл user_data.txt в режиме записи
    with open("user_data.txt", "w", encoding="utf-8") as file:
        # Записываем введенный текст в файл
        file.write(user_input)
    
    print("Текст успешно записан в файл user_data.txt.")
    
    # Открываем файл user_data.txt в режиме чтения
    with open("user_data.txt", "r", encoding="utf-8") as file:
        # Считываем содержимое файла
        file_content = file.read()
    
    # Выводим содержимое файла на экран
    print("Содержимое файла user_data.txt:")
    print(file_content)

# Запускаем функцию
write_user_input_to_file()