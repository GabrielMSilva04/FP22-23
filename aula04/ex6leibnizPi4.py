x=int(input("n? "))

def leibnizPi4(n):
    pi4 = 0
    for i in range(n+1):
        m=((-1)**i)/(2*i+1)
        pi4 += m
    print(pi4)

leibnizPi4(x)