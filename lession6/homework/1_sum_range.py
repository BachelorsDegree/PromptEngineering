def sum_range(start, end):
    total_sum = sum(range(start, end + 1))
    return total_sum

# Запросим у пользователя ввод диапазона
user_input = input("Введите диапазон в формате 'start-end': ")

# Разделим ввод на два числа
start_str, end_str = user_input.split('-')

# Преобразуем строки в целые числа
start = int(start_str)
end = int(end_str)

# Вызовем функцию и выведем результат
result = sum_range(start, end)
print(f"Сумма чисел в диапазоне от {start} до {end} равна {result}.")