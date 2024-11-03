def hello(*names):
    print(names)
    for name in names:
        print("Hello", name)
    
hello("Alice", "Bob", "Charlie")
