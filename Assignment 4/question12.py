num = int(input('Enter number :'))
n = int(input('Enter the number of digit :'))
sum = 0
temp = num
while(temp>0):
    d = temp%10
    temp = temp//10
    sum += d**n
if( sum == num):
    print(f'{num} is an armstrong number')
else:
    print(f'{num} is not an armstrong number')