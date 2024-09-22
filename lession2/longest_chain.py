def longest_chain(s):
  max_length = 0
  current_length = 0
  o_count = 0
  in_chain = False

  for char in s:
      if char == 'D':
          if in_chain:
              # Завершаем текущую цепочку и обновляем максимальную длину
              max_length = max(max_length, current_length + 1)
          # Начинаем новую цепочку
          current_length = 1
          o_count = 0
          in_chain = True
      elif char == 'O' and in_chain:
          if o_count < 2:
              o_count += 1
              current_length += 1
          else:
              # Нарушение условия, цепочка должна закончиться
              in_chain = False
              current_length = 0
              o_count = 0
      elif in_chain:
          current_length += 1

  return max_length

# Укажите путь к текстовому файлу
file_path = 'D:\\PythonProjects\\PromptEngineering\\text.txt'

# Чтение текста из файла
with open(file_path, 'r') as file:
  text_from_file = file.read().strip()

result = longest_chain(text_from_file)
print(f"Длина самой длинной цепочки: {result}")

# Пример использования с текстовой переменной, закомментирован
# text = "ACDDOFDCCDOODFODDDOFACDOFD"
# result = longest_chain(text)
# print(f"Длина самой длинной цепочки: {result}")