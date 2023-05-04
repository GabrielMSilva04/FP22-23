from tkinter import filedialog

def main():
    # 1) Pedir nome do ficheiro (experimente cada alternativa):
    #name = input("File? ")  #name(relative path): aula06\ex 1(soma em doc txt)\nums.txt                                #A
    name = filedialog.askopenfilename(title="Choose File") #B
    
    # 2) Calcular soma dos números no ficheiro:
    total = fileSum(name)
    
    # 3) Mostrar a soma:
    print("Sum:", total)


def fileSum(filename):
    # Complete a função para ler números do ficheiro e devolver a sua soma.
    lst=[]
    fileobj = open(filename, 'r') # open for reading
    for line in fileobj: # for each line from the file
        lst.append(float(line)) # add every line to a list
    soma=sum(lst) #sum lines
    fileobj.close() #close doc
    return soma


if __name__ == "__main__":
    main()

