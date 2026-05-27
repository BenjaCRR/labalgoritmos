import time
import random
import sys
import matplotlib.pyplot as plt

sys.setrecursionlimit(5000)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    low = [x for x in arr[:-1] if x < pivot]
    equal = [x for x in arr if x == pivot]
    high = [x for x in arr[:-1] if x > pivot]
    return quicksort(low) + equal + quicksort(high)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

tamanos = [100, 200, 400, 600, 800, 1000]
tiempos_quick = []
tiempos_bubble = []
tiempos_insertion = []
tiempos_selection = []

for t in tamanos:
    datos_originales = [random.randint(1, 10000) for _ in range(t)]
    
    datos = datos_originales.copy()
    inicio = time.time()
    quicksort(datos)
    tiempos_quick.append(time.time() - inicio)
    
    datos = datos_originales.copy()
    inicio = time.time()
    bubble_sort(datos)
    tiempos_bubble.append(time.time() - inicio)
    
    datos = datos_originales.copy()
    inicio = time.time()
    insertion_sort(datos)
    tiempos_insertion.append(time.time() - inicio)
    
    datos = datos_originales.copy()
    inicio = time.time()
    selection_sort(datos)
    tiempos_selection.append(time.time() - inicio)

plt.figure(figsize=(10, 6))
plt.plot(tamanos, tiempos_quick, label='Quicksort', color='blue', marker='o', linewidth=2)
plt.plot(tamanos, tiempos_bubble, label='Bubble Sort', color='red', marker='s', linewidth=1.5)
plt.plot(tamanos, tiempos_insertion, label='Insertion Sort', color='orange', marker='^', linewidth=1.5)
plt.plot(tamanos, tiempos_selection, label='Selection Sort', color='purple', marker='d', linewidth=1.5)

plt.title('Comparacion de Tiempos Reales de Ordenamiento', fontsize=14, pad=15)
plt.xlabel('Tamano del arreglo (n)', fontsize=12)
plt.ylabel('Tiempo de ejecucion (segundos)', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(fontsize=10)

plt.show()
