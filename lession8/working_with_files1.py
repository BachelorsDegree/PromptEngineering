# Подключаем модуль chardet
import io
import sys

import chardet


# Функция для определения кодировки
def detect_file_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        return result['encoding']

file_path = 'new_text_file.txt'  # Замените на путь к вашему файлу
encoding = detect_file_encoding(file_path)
print(f"The encoding of the file is: {encoding}") # Вывод кодировки

# Функция для вывода текста с указанной кодировкой
def print_with_encoding(text, encoding='utf-8'):
    # Перенаправляем sys.stdout на TextIOWrapper с нужной кодировкой
    wrapped_stdout = io.TextIOWrapper(sys.stdout.buffer, encoding=encoding)
    
    try:
        # Выводим текст
        wrapped_stdout.write(text + '\n')
    finally:
        # Закрываем wrapped_stdout, но не sys.stdout
        wrapped_stdout.detach()

# Пример использования
# print_with_encoding("Hello, world! Привет, мир!", encoding='utf-8')
# print_with_encoding("Hello, world! Привет, мир!", encoding='iso-8859-1')

file = open("new_text_file.txt", encoding=encoding) # Открываем файл с определенной кодировкой
text = file.read() # Считываем содержимое файла
print(text) # Выводим содержимое на экран

# Рассмотрим ряд функций для взаимодействия с файлом:
file.seek(0) # Перемещаемся в начало файла
text = file.read(34) # Считываем определенное количество символов
print_with_encoding(text, encoding='utf-8')

file.seek(0)
text = file.readline() # Считываем одну строку
print_with_encoding(text, encoding='utf-8')

file.seek(0)
text = file.readlines() # Считываем все строки
print_with_encoding(''.join(text), encoding='utf-8')

file.close() # Закрываем файл
