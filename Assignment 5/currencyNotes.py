amount = int(input("ENter the number :"))
notes = [2000,500,200,100,50,20,10,5]
print("minimun notes needed :")
for note in notes :
    if amount>= notes:
        count = amount//note
        amount %= note
        print(f"{note}  {count}")