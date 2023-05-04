# Complete este programa como pedido no guião da aula.

def listContacts(dic):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:>12s} : {}".format("Numero", "Nome"))
    for num in dic:
        print("{:>12s} : {}".format(num, dic[num]))

def addContact(contacts):
    name = str(input("Nome do contacto? "))
    number = str(input("Número do contacto? "))
    if number not in contacts:
        contacts[number] = name
        print("Número Adicionado")
    else:
        print("Número já registado!")
    return contacts

def removeContact(contacts):
    number = str(input("Número do contacto? "))
    if number in contacts:
        del(contacts[number])
        print("Número Removido")
    else:
        print("Número não registado!")
    return contacts

def findNumber(contacts):
    number = str(input("Número do contacto? "))
    print(contacts.get(number))
    #print(contacts[number]) igual mas dá erro se não existir


def filterPartName(contacts, partName):
    """Returns a new dict with the contacts whose names contain partName."""
    for num in contacts:
        contactName = contacts[num]
        if partName in contactName:
            print("{:>12s} : {}".format(num, contactName))


def menu():
    """Shows the menu and gets user option."""
    print()
    print("(L)istar contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("(T)erminar")
    op = input("opção? ").upper()   # converts to uppercase...
    return op


def main():
    """This is the main function containing the main loop."""

    # The list of contacts (it's actually a dictionary!):
    contacts = {"234370200": "Universidade de Aveiro",
        "727392822": "Cristiano Aveiro",
        "387719992": "Maria Matos",
        "887555987": "Marta Maia",
        "876111333": "Carlos Martins",
        "433162999": "Ana Bacalhau"
        }

    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print("\nContactos:")
            listContacts(contacts)
        elif op == "A":
            print("\nAdicionar contacto:")
            addContact(contacts)
        elif op == "R":
            print("\nRemover contacto:")
            removeContact(contacts)
        elif op == "N":
            print("\nEncontrar contacto:")
            findNumber(contacts)
        elif op == "P":
            print("\nFiltrar contacto:")
            partName = str(input("Parte do nome do contacto? "))
            filterPartName(contacts, partName)
        else:
            print("Não implementado!")
    

# O programa começa aqui
main()

