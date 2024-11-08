def bank(a, years):
    rate = 0.10  # Процентная ставка 10%
    for _ in range(years):
        a += a * rate  # Увеличиваем вклад на 10%
    return a

# Пример использования функции
initial_deposit = float(input("Введите сумму вклада в рублях: "))
investment_years = int(input("Введите срок вклада в годах: "))

final_amount = bank(initial_deposit, investment_years)
print(f"Сумма на счету через {investment_years} лет будет: {final_amount:.2f} рублей.")