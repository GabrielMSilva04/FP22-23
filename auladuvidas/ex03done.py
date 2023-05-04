# Calcula o fatorial de um número n de forma iterativa
# Exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120

def factorial_iterative(n):
    fac=n
    if n <= 0:
        fac=1
    else:
        for i in range(n-1,0,-1):
            fac *= i
    return fac


def main():

    assert(factorial_iterative(0) == 1) # 1
    assert(factorial_iterative(5) == 120) # 120
    assert(factorial_iterative(10) == 3628800) # 3628800 

    print("All tests passed!")

if __name__ == "__main__":
    main()