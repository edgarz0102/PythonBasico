#Ejercicio1
suma=0
lista=[]
for i in range(1,11,1):
    lista.append(i)
    suma=suma+i
print(lista,"La suma de los numeros anteriores es: ",suma)
#Ejercicio2
numero = int(input("Ingrese un número: "))
factorial=1
texto="1"
for i in range(1,numero+1,1):
    factorial=factorial*i
for i in range(2,numero+1,1):
    texto=texto+"*"+str(i)    
print(texto," = ",factorial)

#Ejercicio3
numero = int(input("Ingrese un número: "))
control=1
suma=0
while control<=numero:
    a=control*control
    suma+=a
    print(str(control)+"*"+str(control)+" = ",a)
    control+=1
print("La suma de la serie anterior es: ",suma)

#Ejercicio4
lista=[]
while True:
    numero = int(input("Ingrese un número y digite -1 si quiere que termine: "))
    if numero==-1:
        break
    lista.append(numero)

promedio=sum(lista)/len(lista)
maximo=max(lista)
minimo=min(lista)
print(lista)
print(promedio,maximo,minimo)