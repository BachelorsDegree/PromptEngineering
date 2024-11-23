import random

# Все доступные символы для генерации пароля
letters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%~&*()_+="

# Переменная для хранения пароля
password = ""

# Генерация пароля длиной 8 символов
for i in range(8):
    password += random.choice(letters)

# Вывод итогового результата
print(password)
