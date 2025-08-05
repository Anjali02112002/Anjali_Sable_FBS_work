length = int(input('Enter length of wall :'))
breadth = int(input('Enter breadth of wall :'))
cost = int(input('Enter cost per area :'))

area = length*breadth
total_area = 4*area

total_cost = cost*total_area

print(f'The total cost of painting is {total_cost}.')
