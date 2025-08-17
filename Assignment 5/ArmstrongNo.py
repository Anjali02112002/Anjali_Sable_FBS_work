num = int(input("Enter number :"))
temp = num
sum = 0
count = 0
temp2 = num
while temp2>2 :
    count+=1
    temp2//10
temp = num
while(temp>0):
    digit = temp%10
    sum += digit**count
    temp=temp//10
if sum == num:
    print(f'{num} is an armstrong number.')
else:
    print(f'{num} is not an armstrong number.')