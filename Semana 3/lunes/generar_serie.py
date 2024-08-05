def serie(a,b,c):
    lista=[]
    for i in range(1,a+1):
        an=c+b*(i-1)
        lista.append(an)
    return lista

a = int(input("Ingrese la longitud de terminos de la serie: "))
b = int(input("Ingrese ""d"" de la serie aritmeética: "))
c = int(input("Ingrese el primer término de la serie aritmética: "))
k=serie(a,b,c)
print(k)