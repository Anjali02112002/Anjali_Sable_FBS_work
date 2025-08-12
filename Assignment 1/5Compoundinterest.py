num1=int(input('Enter principal amount :'))
num2=int(input('Enter time :'))
num3=int(input('Enter rate :'))
#formula of CP
Compound_Interest=(num1*(1+num3/100)**num2)-num1

print(f'Compound ineterest of given number is{Compound_Interest}')