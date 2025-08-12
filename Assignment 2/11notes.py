#WAP to count minimum notes present in a given amount
amt = int(input('Enter the amount :'))
temp = amt

two_thousand = temp // 2000
temp = temp % 2000

five_hundred = temp // 500
temp = temp % 500

hundred = temp // 100
temp = temp % 100

fifty = temp // 50
temp = temp % 50

twenty = temp // 20
temp = temp % 20

ten = temp // 10
temp = temp % 10

total_notes = two_thousand + five_hundred + hundred + fifty + twenty + ten 
print(f'Total no. of notes present in {amt} is {total_notes}')

