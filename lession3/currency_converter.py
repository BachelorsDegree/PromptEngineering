import requests
import json

def get_exchange_rates():
    try:
        # Запрос данных о курсах валют
        response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        # Проверка успешности запроса
        response.raise_for_status()
        # Возврат данных в формате JSON
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении данных: {e}")
        return None

def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency == 'RUB':
        rubles = amount
    else:
        rubles = amount * rates[from_currency]['Value'] / rates[from_currency]['Nominal']
    
    if to_currency == 'RUB':
        return rubles
    else:
        return rubles / rates[to_currency]['Value'] * rates[to_currency]['Nominal']

def main():
    # Получаем данные о курсах
    data = get_exchange_rates()
    if not data:
        return
    
    rates = data['Valute']
    
    # Ввод данных от пользователя
    from_currency = input("Введите код валюты, из которой хотите конвертировать (например, USD): ").upper()
    to_currency = input("Введите код валюты, в которую хотите конвертировать (например, EUR): ").upper()
    amount = float(input("Введите сумму для конвертации: "))
    
    # Проверка наличия валюты в данных
    if from_currency not in rates and from_currency != 'RUB':
        print(f"Валюта {from_currency} не найдена.")
        return
    if to_currency not in rates and to_currency != 'RUB':
        print(f"Валюта {to_currency} не найдена.")
        return

    # Конвертация валюты
    result = convert_currency(amount, from_currency, to_currency, rates)
    print(f"{amount} {from_currency} -> {result:.2f} {to_currency}")

if __name__ == "__main__":
    main()