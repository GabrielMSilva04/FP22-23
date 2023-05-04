# Complete the code to make the HiLo game...

import random

def main():
    # Pick a random number between 1 and 100, inclusive
    secret = random.randrange(1, 101);
    print("Can you guess my secret?")
    # put your code here
    n=0
    tent=0
    while n != secret:
        n=int(input("Your guess? "))
        tent += 1
        if n > secret:
            print("Too high")
            
        elif n < secret:
            print("Too low")
            
        elif n == secret: 
            print("Número de tentativas:",tent)
        

main()
