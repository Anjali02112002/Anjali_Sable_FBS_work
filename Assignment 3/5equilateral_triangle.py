a = int(input("Enter first side of triangle :"))
b = int(input("Enter second side of triangle :"))
c = int(input("Enter third side of triangle :"))

if(a==b==c):
    print('This is an equilateral triangle')
elif(a==b or b==c or a==c):
    print('This is isoceles triangle')
elif(a != b != c):
    print('This is a scalene triangle')
else:
    print('Triangle is invalid')