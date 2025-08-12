user_id = str(input("Enter user id :"))
password = int(input('Enter password :'))

if (user_id == 'admin' and password == 1234):
    print("User id and password is correct :")
else:
    print("User id and password is not valid")
    