age1 = int(input('enter age of person1 : '))
age2 = int(input('enter age of person2 : '))
age3 = int(input('enter age of person3 : '))
age4 = int(input('enter age of person4 : '))
age5 = int(input('enter age of person5 : '))
ticket = int(input('Enter ticket price : '))

#person 1 
if (age1<12):
    amt1 = ticket*0.7
elif(age1>59):
    amt1 = ticket*0.5
else:
    amt1 = ticket

#person 2
if (age2<12):
    amt2 = ticket*0.7
elif(age2>59):
    amt2 = ticket*0.5
else:
    amt2 = ticket

#person 3
if (age3<12):
    amt3 = ticket*0.7
elif(age3>59):
    amt3 = ticket*0.5
else:
    amt3 = ticket

#person 4
if (age4<12):
    amt4 = ticket*0.7
elif(age4>59):
    amt4 = ticket*0.5
else:
    amt4 = ticket

#person 5
if (age5<12):
    amt5 = ticket*0.7
elif(age5>59):
    amt5 = ticket*0.5
else:
    amt5 = ticket

total_amount = amt1 + amt2 + amt3 + amt4 + amt5

print(f'Total amount of ticket to travel is {total_amount}')