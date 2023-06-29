mass = float(input("Enter your mass in kilos"))
height = float(input("Enter your height in metres squared "))

bmi = mass / (height * height)

if bmi <= 18:
    print("Underweight")
elif bmi <= 29.0:
    print("Normal weight")
elif bmi <= 34.0:
    print("Overweight")
else:
    print("Obese")

    print("Your BMI is", bmi, "kg/m2")
