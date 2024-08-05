def esparimpar(fin):
    rango=range(1, fin+1)
    pares=[]
    impares=[]
    for i in rango:
        if i%2==0:
            pares.append(i)
        else:
            impares.append(i)
    return pares, impares

fin=int(input("Ingrese el número final del rango: "))
pares, impares = esparimpar(fin)
print("Los pares son: ",pares)
print("Los impares son: ",impares)

