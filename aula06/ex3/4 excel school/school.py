# Complete o programa!

# a)
def loadFile(fname, lst):
    file = open(fname, 'r')
    next(file)
    for line in file:
        t=line.split('\t') #each cell content
        lstline=[t,notaFinal(t)]
        lst.append(lstline)
    file.close()
    return lst



# b) Crie a função notaFinal aqui...
def notaFinal(reg):
    notasstr=reg[-3::] #last 3 elements on line
    notas=[]
    for n in notasstr: #transform strings into float
        n=float(n)
        notas.append(n)
    media=sum(notas)/len(notas)
    return round(media,1) #one decimal case



# c) Crie a função printPauta aqui...
def printPauta(reg,file):
    file.write("\n{:>6}  {:^70}  {:>4}".format(reg[0], reg[1][1], reg[-1]))
    print("{:>6}  {:^70}  {:>4}".format(reg[0], reg[1][1], reg[-1])) #reg=[numero[nome,etc]nota]
    

    

# d)
def main():
    lst = []
    # ler os ficheiros
    loadFile("school1.csv", lst)
    loadFile("school2.csv", lst)
    loadFile("school3.csv", lst)
    
    # ordenar a lista
    lst2=[]
    for line in lst:
        n=int(line[0][0])
        line.insert(0, n)
        lst2.append(line)
    lst2=sorted(lst2) 
    
    # mostrar a pauta
    f = open("school.txt", "w")
    f = open("school.txt", "a")
    f.write("{:>6} {:^70} {:>6}".format("Numero", "Nome", "Nota"))
    print("{:>6} {:^70} {:>6}".format("Numero", "Nome", "Nota"))   # <(left aligned) ^(center aligned) >(right aligned) 
    for line in lst2:
        printPauta(line,f)
    f.close()
    


# Call main function
if __name__ == "__main__":
    main()