def fibonacci():
    num = int(input("Enter number :"))
    a = 1
    b = 0
    print("Fibonacci series:")
    for i  in range (num):
        c = a+b
        a=b
        b=c
        
        print(c,end=' ')
fibonacci()
