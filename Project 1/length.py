def meters_to_km(m):
    return m / 1000
def km_to_meters(km):
    return km * 1000
def meters_to_feet(m):
    return m * 3.28084
def feet_to_meters(f):
    return f / 3.28084


def length_menu():
    while True:
        print("\n1.M→KM 2.KM→M 3.M→Feet 4.Feet→M 5.Back")

        ch = input("Choice: ")
        if ch == "1":
            print(meters_to_km(float(input("Meters: "))))
        elif ch == "2":
            print(km_to_meters(float(input("KM: "))))
        elif ch == "3":
            print(meters_to_feet(float(input("Meters: "))))
        elif ch == "4":
            print(feet_to_meters(float(input("Feet: "))))
        else:
            print("Invalid choice")