def days_in_month(month):
    # Словарь, сопоставляющий номер месяца с количеством дней
    month_days = {
        1: 31,  # Январь
        2: 28,  # Февраль (не учитываем високосный год)
        3: 31,  # Март
        4: 30,  # Апрель
        5: 31,  # Май
        6: 30,  # Июнь
        7: 31,  # Июль
        8: 31,  # Август
        9: 30,  # Сентябрь
        10: 31, # Октябрь
        11: 30, # Ноябрь
        12: 31  # Декабрь
    }
    
    # Возвращаем количество дней в указанном месяце
    return month_days.get(month, "Ошибка: введите номер месяца от 1 до 12.")

def main():
    try:
        # Запрашиваем у пользователя номер месяца
        month_number = int(input("Введите номер месяца (1-12): "))
        # Выводим количество дней в месяце
        print(f"Количество дней в месяце: {days_in_month(month_number)}")
    except ValueError:
        print("Ошибка: введите целое число.")

# Запускаем программу
main()