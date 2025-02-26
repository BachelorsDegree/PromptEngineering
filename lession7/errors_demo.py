def demonstrate_errors() -> object:
    # Ошибка TypeError: can only concatenate str (not "int") to str
    try:
        result = "Hello" + 5
    except TypeError as e:
        print(f"Ошибка 1: {e}")

    # Ошибка TypeError: object of type 'int' has no len()
    try:
        length = len(5)
    except TypeError as e:
        print(f"Ошибка 2: {e}")

    # Ошибка TypeError: add() missing 1 required positional argument: 'b'
    def add(a, b):
        return a + b

    try:
        add(5)  # Здесь не хватает второго аргумента
    except TypeError as e:
        print(f"Ошибка 3: {e}")

    # Ошибка TypeError: unsupported operand type(s) for +: 'int' and 'list'
    try:
        result = 5 + [1, 2, 3]
    except TypeError as e:
        print(f"Ошибка 4: {e}")

if __name__ == "__main__":
    demonstrate_errors()

#Описание ошибок:

 #   Ошибка 1: При попытке объединить строку и целое число возникает ошибка TypeError, так как Python не может выполнить конкатенацию разных типов.
 #   Ошибка 2: Функция len() не может быть применена к целому числу, что приводит к ошибке TypeError.
 #   Ошибка 3: При вызове функции add() не хватает одного аргумента, что вызывает ошибку TypeError.
 #   Ошибка 4: Попытка сложить целое число и список также приводит к ошибке TypeError.

#Запустив эту программу, вы увидите сообщения об ошибках, которые помогут понять, как они возникают и как их можно исправить.