my_list = []

# Добавляем 3 элемента в список
my_list.insert(len(my_list), 10)
my_list.insert(len(my_list), 20)
my_list.insert(len(my_list), 30)

# Вставляем 2 элемента в самое начало списка
my_list.insert(0, 5)
my_list.insert(0, 15)

# Сортируем список по убыванию
my_list.sort(reverse=True)

# Выводим итоговый список
print(my_list)