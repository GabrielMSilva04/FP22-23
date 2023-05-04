x=int(input("Número 1: "))
y=int(input("Número 2: "))
z=int(input("Número 3: "))

def max3(x1 , y1 , z1):    
    if x1>y1 and x1>z1:
        max=x1
    elif y1>x1 and y1>z1:
        max=y1
    elif z1>x1 and z1>y1:
        max=z1
    return(max)

max=max3(x , y , z)
print (max)