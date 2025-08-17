def sum():
    num = int(input("Enter digit :"))
    sum = 0
    while(num>0):
       d = num%10
       num = num//10
       sum+=d
    return sum
result=sum()
print("Sum is :",result)