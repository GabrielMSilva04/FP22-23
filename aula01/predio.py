from math import factorial


dist3a=2*4*3*3*365 #2 pessoas,4 viagens, 3 pisos, 3 metros
dist2a=2*4*3*2*365
dist1a=2*4*3*1*365

dist=(dist3a+dist2a+dist1a)/1000
print("A distância percorrida pelo elevador em um ano é",dist,"km") 


A=int(input("Andares: "))
M=int(input("Moradores por andar: "))


dpM=365*4*(((3+(3*A))*A)/2) #soma geral de viagens

d=dpM*M

d=d/1000 #m-km
t=d/3.6 #1m/s=3,6km/h, t=d/v

print("Distância num prédio com",A,"andares com",M,"moradores cada:",d,"km")
print("Tempo de funcionamento do elevador num prédio com",A,"andares com",M,"moradores cada:",t,"h")
