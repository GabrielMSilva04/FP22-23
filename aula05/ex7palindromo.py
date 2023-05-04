def ispalindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False
        
s=input("word?")
print(ispalindrome(s))
ispalindrome(s)