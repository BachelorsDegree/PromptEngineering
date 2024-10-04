def main():
    # Запрашиваем имя и возраст
    name = input("Введите ваше имя: ")
    age = int(input("Введите ваш возраст в годах: "))

    # Вычисляем возраст в различных единицах
    age_in_months = age * 12
    age_in_days = age * 365
    age_in_hours = age_in_days * 24
    age_in_minutes = age_in_hours * 60
    age_in_seconds = age_in_minutes * 60

    # Выводим приветствие и информацию о возрасте
    print(f"Привет {name}! Тебе {age}.")
    print(f"{age} лет — это {age_in_months} месяцев или {age_in_days} дней, или {age_in_hours} часов, или {age_in_minutes} минут, или {age_in_seconds} секунд.")

    # Выводим формулы
    print("\nФормулы для расчета:")
    print("Возраст в месяцах: возраст * 12")
    print("Возраст в днях: возраст * 365")
    print("Возраст в часах: возраст в днях * 24")
    print("Возраст в минутах: возраст в часах * 60")
    print("Возраст в секундах: возраст в минутах * 60")

if __name__ == "__main__":
    main()