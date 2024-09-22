def sort_numbers(numbers):
  return sorted(numbers)

# Чтение списка чисел от пользователя
input_numbers = input("Введите список чисел, разделенных пробелами: ")

# Преобразование строки ввода в список целых чисел
numbers_list = list(map(int, input_numbers.split()))

# Сортировка списка
sorted_list = sort_numbers(numbers_list)

# Вывод отсортированного списка
print("Отсортированный список:", sorted_list)