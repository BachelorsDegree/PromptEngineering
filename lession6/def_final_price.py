def final_price(price, discount=10):  # Фикс. скидка
#def final_price(price, discount):
    result = price - (price * discount / 100)
    print(f"Цуна с учетом скидки = {result}")

#final_price(1500, 50)
#final_price(23000, 27)
final_price(23000)
# Фикс скидка + Фикс. цена
final_price(23000, 20)
# Фикс скидка + Фикс. цена с указанием скидки = два значения в результате
final_price(discount=34, price=15000) 
#поменять значения местами, но указать что к чему относится