def calculate_bmi(weight, height):
    return weight / (height ** 2)
def bmi_menu():
    while True:
        w = float(input("Weight (kg): "))
        h = float(input("Height (m): "))
        b = calculate_bmi(w, h)
        print("BMI:", round(b, 2))