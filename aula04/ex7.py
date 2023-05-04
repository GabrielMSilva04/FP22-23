
def soma():
    som = 0.0
    while True:
        s=input("Valor?")
        if s == "":
            break
        n = float(s)
        som = som + n
    print(som)
    
soma()