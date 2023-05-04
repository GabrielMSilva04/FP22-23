# Testa se um número é primo 
# Exemplo: 53 é primo porque só é divisível por 1 e por ele mesmo

def is_prime(n):
    count=0
    for i in range(1,n+1):
        if n%i == 0:
            count += 1
    if count<=2:
        return True
    else:
        return False

def main():
    assert(is_prime(2) == True) # True
    assert(is_prime(3) == True) # True
    assert(is_prime(4) == False) # False
    assert(is_prime(5) == True) # True
    assert(is_prime(53) == True) # False
    assert(is_prime(7) == True) # True
    assert(is_prime(8) == False) # False
    assert(is_prime(9) == False) # False
    assert(is_prime(10) == False) # False
    assert(is_prime(129) == False) # False
    print("All tests passed!")
if __name__ == "__main__":
    main()  