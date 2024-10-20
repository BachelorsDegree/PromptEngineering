import random

def get_computer_choice():
    # Случайным образом выбираем один из вариантов: 'камень', 'ножницы' или 'бумага'
    return random.choice(['камень', 'ножницы', 'бумага'])

def determine_winner(user_choice, computer_choice):
    # Определяем победителя на основе выбора пользователя и компьютера
    if user_choice == computer_choice:
        return 'Ничья'  # Если выборы совпадают, то это ничья
    elif (user_choice == 'камень' and computer_choice == 'ножницы') or \
         (user_choice == 'ножницы' and computer_choice == 'бумага') or \
         (user_choice == 'бумага' and computer_choice == 'камень'):
        return 'Пользователь'  # Пользователь выигрывает в этих комбинациях
    else:
        return 'Компьютер'  # В остальных случаях выигрывает компьютер

def main():
    # Инициализируем счет для пользователя и компьютера
    user_wins = 0
    computer_wins = 0

    # Игра продолжается, пока один из игроков не наберет 3 победы
    while user_wins < 3 and computer_wins < 3:
        # Пользователь вводит свой выбор
        user_choice = input("Введите ваш выбор (камень, ножницы, бумага): ").strip().lower()
        
        # Проверяем корректность ввода
        if user_choice not in ['камень', 'ножницы', 'бумага']:
            print("Некорректный ввод. Пожалуйста, выберите 'камень', 'ножницы' или 'бумага'.")
            continue  # Если ввод некорректный, переходим к следующей итерации цикла
        
        # Получаем выбор компьютера
        computer_choice = get_computer_choice()
        print(f"Компьютер выбрал: {computer_choice}")

        # Определяем победителя текущего раунда
        winner = determine_winner(user_choice, computer_choice)
        if winner == 'Пользователь':
            user_wins += 1  # Увеличиваем счет пользователя
            print("Вы выиграли этот раунд!")
        elif winner == 'Компьютер':
            computer_wins += 1  # Увеличиваем счет компьютера
            print("Компьютер выиграл этот раунд!")
        else:
            print("Этот раунд ничья!")

        # Выводим текущий счет
        print(f"Счет: Пользователь {user_wins} - {computer_wins} Компьютер\n")

    # Определяем итогового победителя
    if user_wins == 3:
        print("Поздравляем! Вы выиграли игру!")
    else:
        print("К сожалению, компьютер выиграл игру.")

if __name__ == "__main__":
    main()