import time
import matplotlib.pyplot as plt

def multiplicar_matrices(n):
    A = [[i + j for j in range(n)] for i in range(n)]
    B = [[i * j for j in range(n)] for i in range(n)]
    C = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def test_matrices():
    tamanos = [10, 30, 60, 100, 150, 200]
    tiempos = []

    for n in tamanos:
        inicio = time.perf_counter()
        multiplicar_matrices(n)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)

    plt.figure(figsize=(8, 5))
    plt.plot(tamanos, tiempos, 'ro-', label='Matrices O(n³)')
    plt.title("Tiempo de Ejecución: Multiplicación de Matrices")
    plt.xlabel("Dimensión n")
    plt.ylabel("Segundos")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    test_matrices()
