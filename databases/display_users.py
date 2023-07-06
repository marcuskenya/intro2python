from database import Student

students = Student.select()
# Use for loop 2 display.
for user in students:
    print(user.name, user.number, user.age, user.gender, user.studentcode)
