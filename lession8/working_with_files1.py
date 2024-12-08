# Подключаем модуль chardet
import io
import locale
import sys

import chardet


def print_system_encoding():
    # Получаем кодировку системы
    system_encoding = locale.getpreferredencoding()
    print(f"Системная кодировка: {system_encoding}")

print_system_encoding()

def print_console_encoding():
    # Получаем кодировку стандартного вывода
    encoding = sys.stdout.encoding
    print(f"Кодировка консоли: {encoding}")

print_console_encoding()

# Функция для определения кодировки
def detect_file_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        return result['encoding']

file_path = 'new_text_file.txt'  # Замените на путь к вашему файлу
encoding = detect_file_encoding(file_path)
print(f"Кодировка файла: {encoding}") # Вывод кодировки

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

file = open("new_text_file.txt") # Открываем файл с определенной кодировкой
# ИЛИ file = open("new_text_file.txt", encoding=encoding) и тогда, 
# дальше можно кодировку не указывать или указать utf-8(.txt файл в utf-8)
text = file.read() # Считываем содержимое файла
print("Печатаем текст из файла с кодировкой utf-8 в открытого в кодировке cp1251:")
print("\n")
print(text) # Выводим содержимое на экран
print("\n")
# Рассмотрим ряд функций для взаимодействия с файлом:

print("Используем функцию для вывода текста из файла с кодировкой utf-8 в текст в кодировке cp1251:")
file.seek(0) # Перемещаемся в начало файла
text = file.read(34) # Считываем определенное количество символов
print_with_encoding(text, encoding='cp1251')
print("\n")
file.seek(0)
text = file.readline() # Считываем одну строку
print_with_encoding(text, encoding='cp1251')
print("\n")
file.seek(0)
text = file.readlines() # Считываем все строки
print_with_encoding(''.join(text), encoding='cp1251')
print("\n")
file.close() # Закрываем файл
