from cmath import acos
import math
from re import A

A=int(input("Cateto 1? "))
B=int(input("Cateto 2? "))
C=math.sqrt(A**2+B**2) #raíz quadrada

cosA=A/C
ang=math.acos(A/C) #em radiano, de 0 a 2pi
ang=(180*ang)/math.pi #em graus (0,360)
ang2=round(ang,2) #arredondar ang em 2 casas decimais

print("Hipotenusa:",C)
print("Ângulo entre cateto A e hipotenusa:", ang2)