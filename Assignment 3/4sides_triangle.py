a = int(input('Enter first side of triangle :'))
b = int(input('Enter second side of triangle :'))
c = int(input('Enter third side of triangle :'))

if(a+b>c and b+c>a):
    print('Triangle is valid')
else:
    print('Triangle is invalid')