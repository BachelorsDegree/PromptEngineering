def draw_rectangle_with_area(width, height):
    # Вычисляем площадь прямоугольника
    area = width * height

    # Создаем верхнюю и нижнюю границы
    border = '*' * (width + 2)

    # Создаем среднюю часть
    middle = '*' + ' ' * width + '*'

    # Создаем строку с площадью, расположенной по центру
    area_string = str(area)
    total_padding = width - len(area_string)
    left_padding = total_padding // 2
    right_padding = total_padding - left_padding
    area_line = '*' + ' ' * left_padding + area_string + ' ' * right_padding + '*'

    # Создаем строку с шириной, выровненной по центру
    width_string = str(width)
    width_padding = (width + 2 - len(width_string)) // 2
    width_line = ' ' * width_padding + width_string + ' ' * (width + 2 - width_padding - len(width_string))

    # Выводим две пустые строки
    print("\n\n")

    # Выводим строку с шириной
    print(width_line)

    # Выводим верхнюю границу
    print(border)

    # Определяем, куда вставить строку с площадью
    area_line_index = height // 2

    # Выводим прямоугольник с площадью по центру
    for i in range(height):
        if i == area_line_index:
            # Добавляем высоту справа от центральной строки
            print(area_line + ' ' + str(height))
        else:
            print(middle)

    # Выводим нижнюю границу
    print(border)

# Запрос ширины и высоты у пользователя
width = int(input("Введите ширину: "))
height = int(input("Введите высоту: "))

# Использование введенных пользователем значений
draw_rectangle_with_area(width, height)