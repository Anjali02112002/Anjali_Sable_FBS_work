Cost_price = int(input('Enter cost price :'))
discount = int(input('Enter discount on cost price :'))

discounted_value = Cost_price*discount/100
selling_price = Cost_price + discounted_value

print(f'The selling price is {selling_price}')