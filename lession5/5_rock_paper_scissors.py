import random

def get_computer_choice():
    return random.choice(['камень', 'ножницы', 'бумага'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'Ничья'
    elif (user_choice == 'камень' and computer_choice == 'ножницы') or \
         (user_choice == 'ножницы' and computer_choice == 'бумага') or \
         (user_choice == 'бумага' and computer_choice == 'камень'):
        return 'Пользователь'
    else:
        return 'Компьютер'

def main():
    user_wins = 0
    computer_wins = 0

    while user_wins < 3 and computer_wins < 3:
        user_choice = input("Введите ваш выбор (камень, ножницы, бумага): ").strip().lower()
        if user_choice not in ['камень', 'ножницы', 'бумага']:
            print("Некорректный ввод. Пожалуйста, выберите 'камень', 'ножницы' или 'бумага'.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Компьютер выбрал: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        if winner == 'Пользователь':
            user_wins += 1
            print("Вы выиграли этот раунд!")
        elif winner == 'Компьютер':
            computer_wins += 1
            print("Компьютер выиграл этот раунд!")
        else:
            print("Этот раунд ничья!")

        print(f"Счет: Пользователь {user_wins} - {computer_wins} Компьютер\n")

    if user_wins == 3:
        print("Поздравляем! Вы выиграли игру!")
    else:
        print("К сожалению, компьютер выиграл игру.")

if __name__ == "__main__":
    main()