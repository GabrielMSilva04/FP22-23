def evenThenOdd(string):
    even= string[::2]
    odd= string[1::2]
    final=even+odd
    print(final)
    return final

evenThenOdd("abcd")


def removeAdjacentDuplicates(string):
    final=string[0]
    n=string[0]
    for l in string:
        if string.index(l) != string.index(n):
            final+=l
        n=l
    return final

print(removeAdjacentDuplicates("Mississippi"))
print(removeAdjacentDuplicates("aaaaaaaaaabbbbbbbbbbccccccccccddddddddddddddgeeeeeeeee"))
            

def reapeatNumTimes(n):
    lst=[]
    for i in range (1,n+1): #para n elementos
        for i2 in range(i): #para valor do elemento
            lst.append(i)
    return lst
            
print(reapeatNumTimes(4))
print(reapeatNumTimes(3))


def positionOfFirstLargest(arr):
    n=arr[0]
    ind=0
    for n2 in arr:
        if n2 > n or n2 is arr[0]:
            n=n2
            indf=ind #index da primeira ocorrencia do máximo
        ind += 1 #index de n2
        
    return indf
    
print(positionOfFirstLargest([10,90,30,40,30,20,40]))
print(positionOfFirstLargest([1000,90,30,40,30,20,40]))
print(positionOfFirstLargest([10,90,30,40,30,200,40]))