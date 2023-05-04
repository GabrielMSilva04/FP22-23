
def primesUpTo(n):
    primes_set = {num for num in range(2,n+1)}
    for base in range(2,n+1):
        if base**2<n+1:
            for mult in range(2,n+1):
                primes_set.discard(base*mult)
    return primes_set

def main():
    # Testing:
    s = primesUpTo(1000)
    print(s)

    # Do some checks:
    assert primesUpTo(30) == {2,3,5,7,11,13,17,19,23,29}
    assert len(primesUpTo(1000)) == 168
    assert len(primesUpTo(7918)) == 999
    assert len(primesUpTo(7919)) == 1000
    print("All tests passed!")

if __name__ == "__main__":
    main()

