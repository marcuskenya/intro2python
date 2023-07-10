from database import User

users = User.select()
# Use for loop 2 display.
for user in users:
    print(user.name, user.email, user.password)
