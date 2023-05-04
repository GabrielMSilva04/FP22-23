# Cria um número de telefone a partir de uma lista de 10 inteiros 
# Exemplo: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] -> "(123) 456-7890"


def create_phone_number(n):
    tel="("+n[:2]+") "+n[2:5]+"-"+n[5:]
    tel="({}) {}-{}"
    l="".join([str(i) for i in n])
    return tel.format(l[0:3],l[3:6],l[6:10])
#   return "({}{}{}) {}{}{}-{}{}{}{}".format(n[0],n[1],n[2],n[3],n[4],n[5],n[6],n[7],n[8],n[9])
def main():

    assert(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) == "(123) 456-7890"
    assert(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == "(111) 111-1111"
    assert(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0])) == "(023) 056-0890"
    assert(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == "(000) 000-0000"
    print("All tests passed!")

if __name__ == "__main__":
    main()

