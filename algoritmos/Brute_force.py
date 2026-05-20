import time
import matplotlib.pyplot as plt

def es_unico_brute(lista):
    n = len(lista)
    ops = 0
    for i in range(n):
        for j in range(i + 1, n):
            ops += 1 
            if lista[i] == lista[j]:
                return False, ops
    return True, ops

def test_fuerza_bruta():
    tamanos = [10, 50, 100, 200, 400, 600, 800]
    tiempos = []

    for n in tamanos:
        lista = list(range(n))
        
        inicio = time.perf_counter()
        es_unico_brute(lista)
        fin = time.perf_counter()
        
        tiempos.append(fin - inicio)
    plt.figure(figsize=(8, 5))
    plt.plot(tamanos, tiempos, 'go-', label='Fuerza Bruta O(n²)')
    plt.title("Tiempo de Ejecución Brute Force")
    plt.xlabel("Tamaño del input (n)")
    plt.ylabel("Tiempo (segundos)")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    test_fuerza_bruta()
