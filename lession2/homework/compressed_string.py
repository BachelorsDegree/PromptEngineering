def compress_string(s):
    if not s:
        return ""

    compressed = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1

    # Добавляем последние символы
    compressed.append(s[-1] + str(count))

    return ''.join(compressed)

# Запрос строки у пользователя
input_string = input("Введите строку для сжатия: ")
compressed_string = compress_string(input_string)
print(f"Сжатая строка: {compressed_string}")


# Первоначальный вариант
#def compress_string(s):
#  if not s:
#      return ""

#  compressed = []
#  count = 1

#  for i in range(1, len(s)):
#      if s[i] == s[i - 1]:
#          count += 1
#      else:
#          compressed.append(s[i - 1] + str(count))
#          count = 1

  # Добавляем последние символы
#  compressed.append(s[-1] + str(count))

#  return ''.join(compressed)

# Пример использования
#input_string = "aabcccccaaa"
#compressed_string = compress_string(input_string)
#print(f"Сжатая строка: {compressed_string}")