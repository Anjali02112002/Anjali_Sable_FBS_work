def count_digits(num):

    temp = num
    count=0
    while(temp>0):
        num = temp%10
        temp=temp//10
        count+=1
    return count

def check(num):
    temp = num
    n = count_digits(num)
    sum = 0
    while(temp>0):
        d = temp%10
        temp = temp//10
        n1= d**n
        sum+=n1
    return sum == num
n = int(input("Enter number :"))

if check(n):
    print(n,"is an armstrong number.")
else:
    print(n,"is not an armstrong number.")

    