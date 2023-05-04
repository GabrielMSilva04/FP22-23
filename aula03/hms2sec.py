h=int(input("hour?" ))
m=int(input("minutes?" )) 
s=int(input("seconds?" ))

def hms2sec(h , m , s):   
    s=s+(h*3600)
    s=s+(m*60)

    print("Seconds:",s)
    
hms2sec(h , m , s)