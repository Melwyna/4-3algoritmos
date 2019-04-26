from funciones.functions import invertir

print("*Tercer punto*")
a=int(input("Escribe el numero de valores que a tener la lista:"))
lista=[]
for i in range (0,a):
 t0=input("Escribe los valores de la lista que quieres ivertir:")
 lista.append(t0)
tuple=(lista)
f=invertir(tuple)
print('\n', "la tupla original es:", '\n', lista, '\n', "y la tupla invertida es:",'\n', f)