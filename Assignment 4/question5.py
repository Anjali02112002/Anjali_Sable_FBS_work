num = int(input('Enter number :'))
a = -1
b = 1
for i in range(num):
    c = a + b
    print(c, end=' ')
    a = b
    b = c


#using while loop

num = int(input('\nEnter number :'))
a = -1
b = 1
i = 1
while(i<=num):
    c = a + b
    print(c, end=' ')
    a = b
    b = c
    i+=1