correct_id = "admin"
correct_password = "1234"
for attempt in range(1,4):
    user_id = input("Enter user id :")
    password = input("Enter password :")
    if user_id == correct_id and password == correct_password :
        print("Login successful")
        break
    else:
        print("Incorrect password or user id. Try again!")
    if attempt == 3:
        print("you have used all three attempts.")