def partition(array, low, high):
  pivot = array[high]  # Elige el último elemento de la lista como array
  i = low - 1          # Puntero i marca el límite de los elementos menores o iguales al array, haciendo como barrrera
  # El puntero j recorre toda la lista actual, desde el inicio hasta antes del array
  for j in range(low, high):
     # Compara si el elemento actual visitado por j es menor o igual al array
     if array[j] <= pivot:
       i += 1          # Expande la zona de items menores moviendo el puntero i hacia adelante
       array[i], array[j] = array[j], array[i]# Intercambia la posicion de los items, moviendo el menor hacia la izq

  # Coloca el array en su posición correcta final, intercambiándolo con el elemento en i + 1 (o sea para estar adelante de esta división creada)
  array[i+1], array[high] = array[high], array[i+1]
  return i+1           # Devuelve la posicion exacto donde quedó ubicado el array

# Define la función principal del algoritmo Quicksort usando recursividad
def quicksort(array, low=0, high=None):
  # Si es la primera llamada (inicial), establece 'high' como el índice del último elemento
  if high is None:
    high = len(array) - 1
  # Condición de control: se ejecuta solo si el subsegmento actual tiene al menos dos elementos
  if low < high:  # Divide la lista y obtiene la posición definitiva del pivote actual
    pivot_index = partition(array, low, high)# Aplica Quicksort de forma recursiva a la mitad izquierda (elementos menores al array)
    quicksort(array, low, pivot_index-1)    # Aplica Quicksort de forma recursiva a la mitad derecha (elementos mayores al array)
    quicksort(array, pivot_index+1, high)
    
mylist = [64, 34, 25, 5, 22, 11, 90, 12]
quicksort(mylist)
print(mylist)
