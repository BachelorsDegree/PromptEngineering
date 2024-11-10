my_list = [1, 2, 3, 4, 5]

try:
    index = int(input("Введите индекс элемента: "))
    print(my_list[index])
except IndexError:
    print("Такого элемента нет в списке")