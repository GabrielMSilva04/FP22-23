def inputFloatList():
    list=[]
    while True:
        n=input("Número?")
        if n != "":
            n=float(n)
            list.append(n)
        else:
            break
    print(list)
    return(list)

lst=inputFloatList()


v=float(input("v?"))


def countLower(list, v):
    count=0
    for x in list:
        if v > x:
            count +=1
    print(count)
    
countLower(lst, v)


def minmax(list):
    for x in list:       
        countmax=0
        countmin=0
        for y in list:
            if x > y:
                countmax += 1
                if countmax == (len(list)-1):
                    max=x
            elif x < y:
                countmin += 1
                if countmin == (len(list)-1):
                    min=x
    return(min,max)
   
mnmx=minmax(lst) 
print("mínimo:",mnmx[0])
print("máximo",mnmx[1])

def media(list,min,max):
    med=(min+max)/2
    count=0
    for x in list:
        if med > x:
            count += 1
    print("números inferiores ao valor médio do min e max:",count)
    
media(lst , mnmx[0], mnmx[1])