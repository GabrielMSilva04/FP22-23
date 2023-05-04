# Calculadora de IMC
# Recebe o peso e a altura, calcula o IMC e imprime o resultado juntamente com a categoria
def main():
    # receber peso e altura
    peso = ""
    altura = ""
    # para testar, use os valores 80 e 1.80 para peso e altura, respectivamente 
    # em que o resultado deve ser 24.69 e Saudável
float(input("Digite o peso (em kilogramas): ")) 

def IMC(peso, altura):
    #calcular IMC
    imc=peso/(altura**2)
    pass

    #classificar IMC e imprimir resultado
    if 0<imc<18.5:
        cat="Magro"
    elif imc<25:
        cat="Saudável"
    elif imc<30:
        cat="Forte"
    else:
        cat="Obeso"


if __name__ == "__main__":
    main()