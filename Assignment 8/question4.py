def sum():
    n = int(input("enter number :"))
    i = 1
    sum = 0
    for i in range(1,n):
        if(i%2!=0):
            sum+=i
    return sum
result = sum()
print("sum of odd number is :",result)
    

    