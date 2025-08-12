#WAP to swap without using third variable
x = int(input('Enter first number :'))
y = int(input('Enter second number :'))

x = x + y
y = x - y
x = x - y
print(f'After swapping the values x is {x}, y is {y}')