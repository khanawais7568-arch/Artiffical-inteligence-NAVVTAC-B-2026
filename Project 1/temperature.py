def c_to_f(c):
    return (c * 9/5) + 32
def f_to_c(f):
    return (f - 32) * 5/9

def temperature_menu():
    while True:
        print("\n1.C → F   2.F → C   3.Back")
        ch = input("Choice: ")
        if ch == "1":
            c = float(input("Celsius: "))
            print("Result:", c_to_f(c))

        elif ch == "2":
            f = float(input("Fahrenheit: "))
            print("Result:", f_to_c(f))
        else:
            print("Invalid choice")