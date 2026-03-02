def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def arithmetic_menu():
    while True:
        print("\n Arithmetic")
        print("\n1.Add\n  2.Subtract\n  3.Multiply\n  4.Divide")
        ch = input("Choice: ")
        a = float(input("First number: "))
        b = float(input("Second number: "))

        if ch == "1":
            print("Result:", add(a, b))
        elif ch == "2":
            print("Result:", subtract(a, b))
        elif ch == "3":
            print("Result:", multiply(a, b))
        elif ch == "4":
            print("Result:", divide(a, b))
        else:
            print("Invalid choice")