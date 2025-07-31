length = int(input('Enter length :'))
breadth = int(input('Enter breadth :'))

radius = 0.5*breadth

area = length*breadth+(0.5*3.14)*radius*radius

perimeter = 2*length+breadth+(3.14*radius)

print(f'Area of given input is {area} And perimeter is {perimeter}')