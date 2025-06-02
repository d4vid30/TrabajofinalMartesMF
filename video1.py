#primer ejercicio/video1
from math import *
from random import *

print("Programa para calcular el valor de pi")
N=100 ##se cuenta la cantidad de puntos
Pdentro=0 ##cuenta los puntos dentro del circulo
r=0.5 #radio del circulo

for i in range(N):
    x=random()
    y=random()
    if ((x-0.5)*2 + (y-0.5)*2)<=0.5*2:
        Pdentro=Pdentro+1

PI=(Pdentro)/((r**2)*float(N))
print("El valor de pi con el metodo de Montecarlo es: " , PI)
print("El error es de: " , abs(PI-pi))
print("El error porcentual es:  " , abs((PI-pi)/PI)*100)        

#ejercicio2/video1
#Saber el valor aproximado de "e"


print("Programa para estimar el valor de e")

N = 1000  # número de repeticiones
suma_total = 0

for i in range(N):
    suma = 0
    pasos = 0
    while suma < 1:
        suma += random()
        pasos += 1
    suma_total += pasos

e_aprox = suma_total / N

print("Estimacion de e:", e_aprox)