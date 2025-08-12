num = int(input('Enter number :'))
i = 1
fact = 1
while(i<=num):
    fact*=i #fact = fact*1
    i+=1
print(f'The factorial of {num} is {fact}')