import random

def choose_students(student_list, num_to_choose=5):
    # Преобразуем список в множество для удаления повторений
    unique_students = set(student_list)
    
    # Проверяем, что уникальных имён достаточно для выбора
    if len(unique_students) < num_to_choose:
        raise ValueError("Недостаточно уникальных имён для выбора.")
    
    # Преобразуем множество обратно в список
    unique_students_list = list(unique_students)
    
    # Случайным образом выбираем 5 уникальных имён
    chosen_students = random.sample(unique_students_list, num_to_choose)
    return chosen_students

try:
    # Читаем список имён из файла students.txt
    with open(r'PromptEngineering\lession8\homework\students.txt', 'r', encoding='utf-8') as file:
        students = file.read().splitlines()

    # Выбираем 5 уникальных имён
    selected_students = choose_students(students)
    print("Выбранные учащиеся:", selected_students)

except FileNotFoundError:
    print("Ошибка: файл students.txt не найден.")
except ValueError as e:
    print(f"Ошибка: {e}")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")