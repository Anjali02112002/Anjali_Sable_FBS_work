basic_salary = int(input('Enter basic salary :'))

da_amt = basic_salary * 0.1 # basic*10/100

ta_amt = basic_salary * 0.12 

hra_amt = basic_salary * 0.15

total_salary = basic_salary + da_amt + ta_amt + hra_amt

print(f'Total salary is {total_salary}')

