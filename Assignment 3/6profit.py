#calculate profit or loss 
Cost_price = int(input('Enter cost price :'))
Selling_price = int(input('Enter selling price :'))

if Selling_price > Cost_price:
    print('This is profit')
elif Cost_price > Selling_price:
    print('This is loss')
else:
    print('There is no profit or loss')