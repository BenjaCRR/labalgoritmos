def suma_lista(larg,lista):
    if larg==0:
        return 0
    else:
        result = lista[0] + suma_lista(larg - 1, lista[1:])
        return result
    

lista=[2,6,10]
larg=len(lista)
result=suma_lista(larg,lista)
print(result)