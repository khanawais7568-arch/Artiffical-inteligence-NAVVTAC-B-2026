# main.py

import arithmetic
import bmi
import temperature
import length

while True:
    print("\n==== SMART CALCULATOR ====")
    print("1.Arithmetic")
    print("2.BMI")
    print("3.Temperature")
    print("4.Length")

    op = input("Select: ")

    if op == "1":
        arithmetic.arithmetic_menu()

    elif op == "2":
        bmi.bmi_menu()

    elif op == "3":
        temperature.temperature_menu()

    elif op == "4":
        length.length_menu()

    else:
        print("Invalid option")