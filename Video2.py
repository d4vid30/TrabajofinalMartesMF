#EJERCICIO1/VIDEO2

from random import *

print ("Los elementos en python de una lista inicializan en 0")

a=[2,3,4,7, 5.23, True, "Hola", 3+9j, [4,3,9[2,8,7]]]
b=[4,8,9,7]

c=a+b
print("La longitud de b es: " , len(b), "|n")

b.append(70)
print(b)

b.insert(2,-12)
print(b)

b.remove(0)

k=b.index(8)
print(k)

b=[0,4,8,9,7,5,8]

for i in range(len(b)):
    b[i]=b[i]+1

for i in["hola", 3, [4,8,9], 3+-1j, "mundo"]:
    print(i)

g=range(10)
print(g)


i=0
while i<5:
    i=int(10+random())
    print("i= ", i)


# TODO: EJERCICIO2/VIDEO2



print("Ejemplo con listas y estructuras de control en Python")

# Lista con diferentes tipos de datos
datos = [10, False, "Python", 4.5, [1, 2], 2+3j]
print("Lista original:", datos)


nueva = [3, 6, 9]


combinada = datos + nueva
print("Lista combinada:", combinada)

nueva.append(12)
nueva.insert(1, -5)
print("Lista modificada:", nueva)


repetidos = nueva.count(6)
print("El número 6 aparece:", repetidos, "veces")


for i in range(len(nueva)):
    nueva[i] *= 2

print("Lista multiplicada por 2:", nueva)


for item in ["inicio", 99, [5, 5], True, None]:
    print("Elemento:", item)


print("Valores aleatorios:")
j = 0
while j < 15:
    j = int(random() * 20)
    print("j =", j)