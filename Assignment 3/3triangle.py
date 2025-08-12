angle1 = int(input('Enter fisrt angle of triangle : '))
angle2 = int(input('Enter seconod angle : '))
angle3 = int(input('Enter third angle : '))

if (angle1+angle2+angle3 == 180):
    print('Triangle is valid')
else:
    print('Triangle is invalid')