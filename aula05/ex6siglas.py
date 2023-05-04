def shorten(string): #faz print da sigla(de acordo com as maiusculas)
    sigla=""
    for letter in string:
        if letter.isupper():
            sigla += letter
    return sigla

print(shorten("Universidade de Aveiro"))