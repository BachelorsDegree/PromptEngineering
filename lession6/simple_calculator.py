#Способ2

user_input = input("Введите операцию")
num1, operator, num2 = user_input.split()

num1 = float(num1)
num2 = float(num2)

if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)







#Способ1
# number1 = int(input("введите число - "))
# s = input("введите знак математической операции - ")
# number2 = int(input("введите число - "))

# if s == "+":
#     print(number1 + number2)
# elif s == "-":
#     print(number1 - number2)
# elif s == "*":
#     print(number1 * number2)
# elif s == "/":
#     print(number1 / number2)
