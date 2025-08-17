def sum():
    num = int(input('Enter number :'))
    sum = 0
    for i in range(1,num+1):
        sum+=i
    return sum
result=sum()
print('The sum is',result)