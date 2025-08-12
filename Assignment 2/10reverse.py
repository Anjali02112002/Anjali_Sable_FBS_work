num = int(input('Enter three digit number :'))
temp = num

d1 = temp%10
temp = temp//10

d2 = temp % 10
temp = temp // 10

d3 = temp % 10
temp = temp // 10

reverse_digit = d1*100 + d2*10 + d3

print(f'After reversing {num} it becomes {reverse_digit}')