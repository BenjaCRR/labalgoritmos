import matplotlib.pyplot as plt
import numpy as np
import time

def busqueda_lineal(lista, objetivo):
    ops = 0
    for i in range(len(lista)):
        ops += 1 
        if lista[i] == objetivo:
            return ops
    return ops

def busqueda_binaria(lista,objetivo):
    ops = 0
    bajo = 0
    alto = len(lista) - 1
    while bajo <= alto:
        ops += 1
        medio = (bajo + alto) // 2
        if lista[medio] == objetivo:
            return ops
        elif lista[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    return ops 
        
def test_grafico():

    #
    tamanos=[25,50,100,175,225,250]
    tiempo_l=[]
    tiempo_b=[]
    for i in tamanos:
        lista = list(range(i))
        inicio = time.perf_counter()
        busqueda_lineal(lista, -1)
        tiempo_l.append(time.perf_counter() - inicio)

        inicio = time.perf_counter()
        busqueda_binaria(lista, -1)
        tiempo_b.append(time.perf_counter() - inicio)
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 3, 1)
    plt.plot(tamanos, tiempo_l, label='Lineal O(n)', marker='o')
    plt.plot(tamanos, tiempo_b, label='Binaria O(log n)', marker='s')
    plt.title("Búsquedas")
    plt.xlabel("Tamaño de n")
    plt.ylabel("Tiempo (s)")
    plt.legend()
    plt.show()

def main():
    test_grafico()
    
main()