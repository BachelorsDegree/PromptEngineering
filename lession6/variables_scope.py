def f():
    global text
    text = "локальная(глобальная) переменная"
    print(f"внутри переменной находится - {text}")

f()
print(text)