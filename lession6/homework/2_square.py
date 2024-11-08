import math

def square(side_length):
    # Вычисляем периметр
    perimeter = 4 * side_length
    
    # Вычисляем площадь
    area = side_length ** 2
    
    # Вычисляем диагональ
    diagonal = side_length * math.sqrt(2)
    
    # Возвращаем значения в виде кортежа
    return perimeter, area, diagonal

# Пример использования функции
side = float(input("Введите длину стороны квадрата: "))
(perimeter, area, diagonal) = square(side)

print(f"Периметр: {perimeter}, Площадь: {area}, Диагональ: {diagonal}")

#ИЛИ
#print(f"Периметр квадрата: {perimeter}")
#print(f"Площадь квадрата: {area}")
#print(f"Диагональ квадрата: {diagonal}")