import csv
ventas = r"C:\Usuarios\TuUsuario\Documentos\ventas.csv"
def leer_ventas(ventas):
    lista_ventas=[]
    try:
        with open(ventas, mode="r",encoding='utf-8') as archivo:
            lector_dict = csv.DictReader(archivo)
                
            for fila in lector_dict:
                lista_ventas.append(fila) 
        return lista_ventas
    except FileNotFoundError:
        print(f"Error, el archivo {ventas} no existe")
        return []
    except IOError:
        ("Error, no se pudo leer.")
        return []

leer_ventas(ventas)
