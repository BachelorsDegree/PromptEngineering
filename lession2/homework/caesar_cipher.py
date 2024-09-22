def caesar_cipher(text, shift, encrypt=True):
  result = []
  for char in text:
      if char.isalpha():
          # Определяем базовый код в зависимости от регистра
          base = ord('A') if char.isupper() else ord('a')
          # Смещение в зависимости от операции (шифрование/дешифрование)
          shift_direction = shift if encrypt else -shift
          # Вычисляем новый символ с учетом сдвига и добавляем его в результат
          new_char = chr((ord(char) - base + shift_direction) % 26 + base)
          result.append(new_char)
      else:
          # Если символ не является буквой, добавляем его без изменений
          result.append(char)
  return ''.join(result)

def main():
  text = input("Введите текст для шифрования/дешифрования: ")
  shift = int(input("Введите величину сдвига: "))
  choice = input("Выберите операцию (e - шифрование, d - дешифрование): ").lower()

  if choice == 'e':
      encrypted_text = caesar_cipher(text, shift, encrypt=True)
      print(f"Зашифрованный текст: {encrypted_text}")
  elif choice == 'd':
      decrypted_text = caesar_cipher(text, shift, encrypt=False)
      print(f"Расшифрованный текст: {decrypted_text}")
  else:
      print("Некорректный выбор операции.")

if __name__ == "__main__":
  main()