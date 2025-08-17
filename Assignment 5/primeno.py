n = int(input('Enter the number :'))
count = 0
num = 2
while(count<n):
    for i in range (2,num//2+1):
        if(num%2==0):
            break
        else:
            print(f'The first {n} prime numbers are {count}',end=' ')
            count+=1
        num+=1