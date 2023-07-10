from database import User

try:
    jina = input("Enter  name\n ")
    arafa = int(input("Enter email\n"))
    siri = int(input("Enter your password\n"))

    User.create(name=jina, email=arafa, password=siri)

    print("User created successfully")
except:

    print("Failed to create User")
