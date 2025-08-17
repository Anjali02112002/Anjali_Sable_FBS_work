def sum():
    n = int(input("Enter number :"))
    sum = 0  # to store the sum of prime numbers
    num = 2   # prime number will start from 2
    count = 0 # count of prime number
    while(sum<n):
     for i in range(1,n//+1):
        if(num%2==0):
         break
     
     else:
        sum+=num
     count+=1
    
    return sum

result=sum()
print("sum is :",result)

