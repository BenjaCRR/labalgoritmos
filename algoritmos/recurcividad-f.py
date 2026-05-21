#Tienen que escribir en python una función que reciba una posición n y 
#devuelva el número de Fibonacci correspondiente.

#La sucesión de Fibonacci es una serie donde cada número es la suma de los dos anteriores:
#0, 1, 1, 2, 3, 5, 8...
#En matemáticas, se define como F(n) = F(n-1) + F(n-2). Si se detienen en esta definición, se
#van a dar cuenta de que aparece allí la noción misma de recursividad.

def fibonacci(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        r=fibonacci(n-1)+fibonacci(n-2)
        return r

n=6

r=fibonacci(n)
print(r)


#Esto es un extra para hacer una lista comprobando todos los valores.
#lista=[]
#while True:
#    r=fibonacci(n)
#    lista.append(r)
#    print(lista)
#    n+=1

