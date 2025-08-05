c1 = int(input('Enter cost of first product :'))
c2 = int(input('Enter cost of second product :'))
c3 = int(input('Enter cost of third product :'))
c4 = int(input('Enter cost of fourth  product :'))
c5 = int(input('Enter cost of fifth product :'))

cost = c1+c2+c3+c4+c5
gst = cost*0.18

total_cost = cost + gst
print(f'The total cost of shopping is {total_cost}.')