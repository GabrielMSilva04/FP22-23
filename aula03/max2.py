x=int(input("Número 1: "))
y=int(input("Número 2: "))

def max2(x1 , y1):
    
    if x1==y1:
        max="Números iguais"
    elif x1>y1:
        max=x1
    else:
        max=y1
    return(max)
max=max2(x , y)
print (max)