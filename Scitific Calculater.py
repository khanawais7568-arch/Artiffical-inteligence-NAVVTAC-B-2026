print("Smart Calculater")
print("1. Maths Calculater")
print("2. Tax Calculater")
print("3. Temprature Conveter")
print("4. BMI Calculater")
calculate=float(input("Choose operater= "))
import math
if calculate==1 :  #Math Calculater
    print("Math Calculater")
    print("1. Sum")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. percentage")
    print("7. Compare")
    print("8. Equal or Not Equal")
    print("9. Square root")
    print("10. log")
    print("11. Sin of X")
    print("12. Cos of X")
    print("13. Tan of X")
    op=float(input("Choose operater= "))
    
    if op==1 or op==2 or op==3 or op==4 or op==5 or op==6 or op==7 or op==8 :
        n1=float(input("Enter First Number= "))
        n2=float(input("Enter Second Number= "))
        
        if op==1 :
            print("Your result is= ",n1+n2)
        if op==2 :
            print("Your result is= ",n1-n2)
        if op==3 :
            print("Your result is= ",n1*n2)
        if op == 4:
            if n2 != 0:
                print("Yor result is:", n1/n2)
            else:
                print("Error: Cannot divide by zero")
        if op==5:
            print("Your result is= ",math.pow(n1,n2))
        if op==6:
            print("Your result is= ",n1/n2*100)
        if op==7:
            if n1>n2 :
                print("Number 1 is greater than Number 2  or Number 2 is smaller than Number 1")
            if n2>n1:
                print("Number 2 is greater than Number 1 or Number 1 is smaller than Number 2")
        if op==8:
            if n1==n2 :
                print("Number 1 is equal to Number 2")
            else:
                 print("Number 1 is not equal to Number 2")
                 
    if op==9:   #square root
        nu=float(input("Enter Number= "))
        print("Your result is= ",round(math.sqrt(nu),3))
    if op==10: #log 
        log_value=float(input("Enter log value= "))
        base=float(input("Enter base of= "))
        print("Your result is= ",math.log(log_value, base))
    if op==11 or op==12 or op==13: #(Find Sin, Cos, Tan)
        nu=float(input("Enter Value of X (in degree)= "))
        rad = math.radians(nu)
        if op==11: 
            print("Your result is= ",round(math.sin(rad),1))
        if op==12:
            print("Your result is= ",round(math.cos(rad),1))
        if op==13:
            print("Your result is= ",round(math.tan(rad),1))
    print("________________________")
    
if calculate==2 : #Tax calculater
    a = float(input("Enter Your Pay= "))
    b=a*0.02
    c=a*0.03
    d=a*0.04
    e=a*0.05
    f=a*0.10
    if a < 0:
        print("Invalid")
    elif a <= 5000:
        print("Your tax amount is ",b)
    elif a <= 10000:
        print("Your tax amount is ",c)
    elif a <= 15000:
        print("Your tax amount is ",d)
    elif a <= 20000:
        print("Your tax amount is ",e)
    else:
        print("Your tax amount is", f)
    print("________________________")
    
if calculate==3 :  #Temerature converter
    print("Temperature Converter")
    c = float(input("Enter Temperature in Celsius = "))
    print("Convert to")
    print("1. Kelvin")
    print("2. Fahrenheit")
    o = int(input("Enter your choice = "))
    k = c + 273.15
    f = 9/5 * c + 32
    if o == 1:
        print("Temperature in Kelvin =", k)
    elif o == 2:
        print("Temperature in Fahrenheit =", f)
    else:
        print("Invalid Choice!")
    print("________________________")
    
if calculate==4:     #BMI Calculater
    a=float(input("Enter your age years= "))
    f=float(input("Enter your height in feet= "))
    w=float(input("Enter you weight in Kg= "))
    m=f*0.3048
    bmi=w/m**2
    print("Your Body Mass index(BMI) is = ",round(bmi, 2))
    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25:
        print("Normal Weight")
    elif bmi < 30:
        print("Overweight")
    elif bmi < 40:
        print("Obese weight")
    else:
        print("Extreme Obesity")
    print("________________________")
print("   ")
print("Thanks For Using this Calculater")

