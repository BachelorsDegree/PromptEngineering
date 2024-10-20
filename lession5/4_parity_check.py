def main():
    try:
        # Запрашиваем у пользователя начало и конец диапазона
        start = int(input("Введите начало диапазона: "))
        end = int(input("Введите конец диапазона: "))
        
        print("Четные числа в диапазоне от", start, "до", end, ":")
        
        # Используем цикл for для перебора чисел в заданном диапазоне
        for number in range(start, end + 1):
            if number % 2 == 0:
                print(number)
    
    except ValueError:
        print("Ошибка: введите целые числа.")

# Запускаем программу
main()