

a1=float(input("1º número do intervalo 1:"))
b1=float(input("2º número do intervalo 1:"))
a2=float(input("1º número do intervalo 2:"))
b2=float(input("2º número do intervalo 2:"))

def intersects(a1 , b1 , a2 , b2):
    assert a1<=b1
    assert a2<=b2
    if a1<b2<b1 or a2<b1<b2:
        intersect=True
    elif a1==a2 or b1==b2:
        intersect=True
    else:
        intersect=False
        
    print(intersect)
    
    return(intersect)
    #return(a1 , b1 , a2 , b2)

intersects(a1, b1, a2, b2)