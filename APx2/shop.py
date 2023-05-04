# Pode correr o programa sem argumentos:
#   python3 shop
# ou passando outros ficheiros de produtos como argumento:
#   python3 shop produtos1.txt ...

def loadDataBase(fname, produtos):
    """Lê dados do ficheiro fname e atualiza/acrescenta a informação num
    dicionário de produtos com o formato {código: (nome, secção, preço, iva), ...}.
    """
    file = open(fname, 'r')
    next(file)
    for line in file:
        p=line.split("\n") #remover \n de cada linha
        lst=p[0].split(";") #adicionar todos os elementos de uma linha numa lista
        if lst[0] not in produtos:
            n=lst[4].split("%")
            lst[4]=int(n[0])/100
            produtos[lst[0]]=(lst[1],lst[2],lst[3],lst[4]) #acrescentar tuple
    return produtos

   

def registaCompra(produtos):
    """Lê códigos de produtos (ou códigos e quantidades),
    mostra nome, quantidade e preço final de cada um,
    e devolve dicionário com {codigo: quantidade, ...}
    """
    compra={}
    while True:
        codeinput = input("Code? ")
        prod = codeinput.split(" ")
        if len(prod) == 1: #se não for introduzido número depois do código
            prod.append("1") 
        code = prod[0]
        quant = prod[1]
        if not quant.isnumeric():
            print("Quantidade inválida!")
        elif code in produtos:
            quantity = int(prod[1])
            t = produtos[code] #tuple com nome do produto etc
            preco = (float(t[2])+float(t[2])*float(t[3]))*quantity #iva incluido
            print(str(t[0])+"  "+str(quantity)+"  "+"{:.2f}".format(preco)) #exemplo: Cogumelos  1  2.44+taxa
            if code in compra:
                compra[code] += quantity #adicionar caso já esteja registado
            else:
                compra[code] = quantity
        elif code == "":
            break      
    return compra    

         

def fatura(produtos, compra):
    """Imprime a fatura de uma dada compra."""
    fatura={}
    for prod in compra: #ex: compra[prod]=quantidade de prod; prod=codigo
        z=list(produtos[prod])
        z.pop(1)        #retirar seccao a tuple
        z[1]=float(z[1])
        z.append(compra[prod]) #adicionar quantidade
        prod2=tuple(z)
        if produtos[prod][1] not in fatura: #se seccao não for uma key
            fatura[produtos[prod][1]]=[prod2]
        else:
            fatura[produtos[prod][1]].append(prod2)
    precobruto = 0
    precoliquido = 0
    for x in fatura: #cada seccao
        print(x)
        
        dic={}
        for y in fatura[x]:
           nome = y[0]
           info = y[1:]
           dic[nome]=info   #ex:{Atum: [3.38, 0.06, 3], [...]}
        for product in dic:
           quantity = int(dic[product][2])
           price = float(dic[product][0])
           tax = float(dic[product][1])
           pricemulti = price*quantity
           pricetax = pricemulti + pricemulti*tax
           
           precoprodtotal = (price+price*tax)*quantity
           print("{:>4} {:<31}({:>2}%){:>11}".format(str(quantity) , product , str(int(tax*100)) , "{:.2f}".format(precoprodtotal)))
           precoliquido += pricetax
           precobruto += pricemulti         
    ivatotal = precoliquido - precobruto
    print("{:>41}{:>11}".format("Total Bruto:" , "{:.2f}".format(precobruto)))
    print("{:>41}{:>11}".format("Total IVA:" , "{:.2f}".format(ivatotal)))
    print("{:>41}{:>11}".format("Total Liquido:" , "{:.2f}".format(precoliquido)))



def main(args):
    # produtos guarda a informação da base de dados numa forma conveniente.
    produtos = {} 
    # Carregar base de dados principal
    loadDataBase("produtos.txt", produtos) #ex: 'p1': ('Ketchup.', 'Mercearia Salgado', 1.59, 0.23)
    produtos = loadDataBase("produtos.txt", produtos)
    # Juntar bases de dados opcionais (Não altere)
    for arg in args:
        loadDataBase(arg, produtos)
    
    # Use este código para mostrar o menu e ler a opção repetidamente
    MENU = "(C)ompra (F)atura (S)air ? "
    repetir = True
    count = 0
    dicncompra={} #dicionário, key=numero compra, valor=compra
    while repetir:
        # Utilizador introduz a opção com uma letra minúscula ou maiúscula
        op = input(MENU).upper()
        # Processar opção
        if op == "C":
            # Esta opção regista os produtos de uma compra
            compra = registaCompra(produtos)
            count += 1
            dicncompra[count] = compra
        if op == "F":
            while True:
                ncompra=input("Numero compra? ")
                if ncompra=="":
                    break
                elif not ncompra.isnumeric(): #se não for numerico
                    continue
                elif int(ncompra) in dicncompra:
                    ncompra=int(ncompra)
                    cart = dicncompra[ncompra]
                    fatura(produtos, cart)
                    break
                else: #se compra com número inserido não foi feita
                    print("Compra não registada!")
        if op == "S":
            print("Obrigado!")
            break

# Não altere este código / Do not change this code
import sys
if __name__ == "__main__":
    main(sys.argv[1:])
