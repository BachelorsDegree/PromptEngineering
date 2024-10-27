from datetime import datetime


def show_current_datetime():
    # Получаем текущую дату и время
    current_datetime = datetime.now()
    # Форматируем дату и время в удобочитаемом виде
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    # Выводим результат
    print("Текущая дата и время:", formatted_datetime)

# Вызовем функцию
show_current_datetime()