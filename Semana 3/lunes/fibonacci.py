def fibonacci(n):
    lista = [0, 1]

    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return lista

    while len(lista) < n:
        fibo_num = lista[-1] + lista[-2]
        lista.append(fibo_num)
    return lista
n = int(input("Ingrese la cabtidad de elementos de la serie de Fibonacci que desea imprimir: "))

fibonacci_pedir = fibonacci(n)
print(fibonacci_pedir)

