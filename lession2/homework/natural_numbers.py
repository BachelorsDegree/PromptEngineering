def contains_digit_3(number):
  return '3' in str(number)

def find_numbers_with_digit_3(limit):
  numbers_with_3 = []
  for i in range(1, limit + 1):
      if contains_digit_3(i):
          numbers_with_3.append(i)
  return numbers_with_3

limit = 2024
numbers_with_3 = find_numbers_with_digit_3(limit)

print(f"Количество чисел от 1 до {limit}, содержащих цифру 3: {len(numbers_with_3)}")
print("Числа, содержащие цифру 3:")
print(", ".join(map(str, numbers_with_3)))







#Первоначальный вариант
#def contains_digit_3(number):
#  return '3' in str(number)

#def count_numbers_with_digit_3(limit):
#  count = 0
#  for i in range(1, limit + 1):
#      if contains_digit_3(i):
#          count += 1
#  return count

#limit = 2024
#result = count_numbers_with_digit_3(limit)
#print(f"Количество чисел от 1 до {limit}, содержащих цифру 3: {result}")


#Этот код определяет функцию `contains_digit_3`, которая проверяет, содержится ли цифра 3 в числе, и функцию `count_numbers_with_digit_3`, которая проходит по всем числам от 1 до заданного предела и считает те, которые содержат цифру 3. Результат выводится на экран.