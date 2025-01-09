import modules.arithmetic as arithmetic


def main():
    # Примеры использования функций из модуля arithmetic
    a = 10
    b = 5

    print(f"{a} + {b} = {arithmetic.add(a, b)}")
    print(f"{a} - {b} = {arithmetic.subtract(a, b)}")
    print(f"{a} * {b} = {arithmetic.multiply(a, b)}")
    try:
        print(f"{a} / {b} = {arithmetic.divide(a, b)}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()