def mybmi():
    try:
        weight = float(input("Enter your weight in kg"))
        height = float(input("Enter your height in metres "))
        bmi = weight / (height * height)
        print(f"My bmi is {bmi}kg/m2")
    except:
        print("Sorry not a number")


mybmi()
