a=int(input("a? "))
b=int(input("b? "))

def euclides(a , b):
    
    r=a%b
    if r==0:
        mdc=b
    elif r>0:
        while r>0:
            a=b
            b=r
            euclides(a , b)
        
    print (mdc)

euclides(a , b)