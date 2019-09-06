#BMI is calculated by weight/(height*height)
age = int(input("How old are you? "))
weight = 0
height = 0
BMI = 0
if age >= 16 :
    weight = int(input("How heavy are you in kilograms? "))
    height = float(input("How tall are you in meters? "))
    BMI = weight/(height*height)
    print("Your BMI is " + str(BMI))
else:
    print("You're not old enough to use the BMI calculator")
