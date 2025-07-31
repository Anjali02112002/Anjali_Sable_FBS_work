area = int(input('Enter area of wall :'))
cost = int(input('Enter of painting per unit area :'))

interior_area = 8*area
exterior_area = 8*area

cost_interior = cost*interior_area
cost_exterior = cost*exterior_area

total_cost = cost_interior + cost_exterior

print(f'total cost of painting is {total_cost}')


