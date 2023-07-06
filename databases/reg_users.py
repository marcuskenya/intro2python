from database import Student

try:
    jina = input("Enter  name\n ")
    no = int(input("Enter number\n"))
    mwaka = int(input("Enter your age\n"))
    jumuiya = input("Enter your gender\n")
    code = int(input("Enter the studentcode\n"))

    Student.create(name=jina, number=no, age=mwaka
                   , gender=jumuiya, studentcode=code)

    print("Student created successfully")
except:

    print("Failed to create student")
