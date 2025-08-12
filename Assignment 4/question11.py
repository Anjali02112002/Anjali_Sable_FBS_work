num = int(input('Enter number :'))
temp = num
sum = 0
while(temp>0):
    d=temp%10
    temp=temp//10
    i=1
    fact=1
    while(i<=d):
          fact*=i  #fact=fact*1
          i+=1
    sum+=fact #sum=sum+fact
if(sum==num):
        print(f'{num} is a strong number.')
else:
        print(f'{num} is not a strong number.')