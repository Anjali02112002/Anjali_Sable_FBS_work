a=int(input('enter value of a :'))
b=int(input('enter value of b :'))
c=int(input('enter value of c :'))

sqrt=((b**2)-(4*a*c))**0.5

result1=((-b)+sqrt)/2*a
result2=((-b)-sqrt)/2*a

print(f'the root of quadratic eqation is {result1} and {result2}')
