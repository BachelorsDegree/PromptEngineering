# Запрашиваем ввод трех чисел у пользователя
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

# Определяем наименьшее число
min_num = min(num1, num2, num3)

# Проверяем, является ли наименьшее число целым, и выводим результат
if min_num.is_integer():
    print("Наименьшее число:", int(min_num))
else:
    print("Наименьшее число:", min_num)