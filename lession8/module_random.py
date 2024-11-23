#Способ2
#Импорт только указанных функций из модуля random
from random import choice, randint, random, randrange, shuffle, uniform

result = randint(1, 10)
print(f"результат = {result}")

result = random()
print(f"результат = {result}")

my_list = ["первый", "второй", "третий", "четвертый", "пятый"]
result = choice(my_list)
print(f"результат = {result}")

result = randrange(1, 123, 5)
print(f"результат = {result}")

result = uniform(1, 10)
print(f"результат = {result}")

my_list = ["первый", "второй", "третий", "четвертый", "пятый"]
shuffle(my_list)
print(f"результат = {my_list}")

#Способ1
#Импорт модуля random
#import random

#Генерация случайного числа с помощью функции randint
#result = random.randint(1, 10)
#print(f"результат = {result}")