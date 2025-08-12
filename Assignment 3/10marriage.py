gender = str(input('Enter gender of person :'))
age = int(input('Enter age of person :'))

if(gender=='male' and age>=21):
    print('This person is eligible for marriage')
elif(gender == 'female' and age>=18):
    print('This person is eligible for marriage')
else:
    print('Not eligible for marriage')