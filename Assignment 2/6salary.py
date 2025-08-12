salary = int(input('Enter basic salary :'))
temp = salary

da = salary*0.1
da = temp

ta = salary*1.2
ta = temp

hra = salary*1.5
hra = temp

total_salary = da + ta + hra
print(f'Total salary of employee is {total_salary}')