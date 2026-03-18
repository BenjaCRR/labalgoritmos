def main():
    #Consigna: Hacer un programa que utilice al menos dos metodos de strings que no conozcamos. Ir agregando com,entarios respecto a su funcionamiento
    string=input("Ingrese string: ")
    ISUPPER(string)
    ISLOWER(string)
def ISUPPER(string):

    verificar= string.isupper()
    #Con este método podremos coroborar si el string ingresado está o no compleyamente en mayúsuclas
    if verificar==True:
        print("Se encuentra al completo en mayúsculas.")
    else:
        print("El texto NO está al completo en mayúsuclas.")
def ISLOWER(string):
    verificar=string.islower()
    if verificar==True:
        print("Se encuentra al completo en minúsculas.")
    else:
        print("El string tampoco está en minusculas al completo.")




main()