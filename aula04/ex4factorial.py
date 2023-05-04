n=int(input("n? "))
def factorial(n):
    x=1
    for v in range (1 , n+1):
        x *= v
    print(x)

factorial(n)