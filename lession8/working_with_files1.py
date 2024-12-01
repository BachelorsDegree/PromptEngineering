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

file_path = 'new_text_file.txt'  # Replace with your file path
encoding = detect_file_encoding(file_path)
print(f"The encoding of the file is: {encoding}") # Вывод кодировки


# Функция для вывода текста с указанной кодировкой
def print_with_encoding(text, encoding='utf-8'):
    """
    Print text to standard output with the specified encoding.

    Parameters:
    - text (str): The text to print.
    - encoding (str): The encoding to use for the output (default is 'utf-8').
    """
    # Create a TextIOWrapper for standard output with the desired encoding
    with io.TextIOWrapper(sys.stdout.buffer, encoding=encoding) as f:
        f.write(text + '\n')  # Write the text with a newline

# Example usage
# if __name__ == "__main__":
#    print_with_encoding("Hello, world! Привет, мир!", encoding='utf-8')
#    print_with_encoding("Hello, world! Привет, мир!", encoding='iso-8859-1')  # This may raise an error if characters are not supported



file = open("new_text_file.txt") # Открываем файл
text = file.read( ) # Считываем содержимое файла
print(text) # Выводим содержимое на экран

# Рассмотрим ряд функций для взаимодействия с файлом:
text = file.read(10) # Считываем определенное количество символов
print_with_encoding(text, encoding='cp1251')
text = file.readline ( ) # Считываем одну строку
print(text)
text = file.readlines ( ) # Считываем все строки
print(text)


file.close ( ) # Закрываем файл


