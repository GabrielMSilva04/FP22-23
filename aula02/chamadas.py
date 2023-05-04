tempo=int(input("Qual é o tempo de duração da chamada e segundos? "))
custoprimmin=0.12 #primeiro minuto
custopseg=0.12/60 #custo por segundo apos o primeiro minuto
if tempo<=60:
    custo=custoprimmin
else:
    custo=custoprimmin+custopseg*(tempo-60)

print("O custo da chamada vai ser:",custo)