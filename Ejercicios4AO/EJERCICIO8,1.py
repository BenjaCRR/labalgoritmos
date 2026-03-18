def main():
    invitados=["John Pork", "Orce", "TRIPLE T"]
    for i in invitados:
        print("Hola",i,"venite a comer paaaaa")
    print("JOHN PORK MURIÓ. No vendrá a la cena.")
    print("")
    invitados.remove("John Pork")
    invitados.append("gouarnalosse")
    for i in invitados:
        print("Hola",i,"te invito a la merienda de hoy a las six de la tarde")
    print("")
#usar inserts, sumar tres mas, avisar.
    for i in invitados: 
        print("hola", i, "Al final sumamos mas gente")
    print("")
    invitados.insert(0,"Bianchi")
    extension=len(invitados)
    invitados.insert(extension//2,"Jeffrey E.")
    invitados.append("Jorge Maheama")
    print("Lista final de invitados: ",invitados, "¡Los espero!")

    cantidad_invitados=len(invitados)
    print("Hay un total de", cantidad_invitados, "invitados")



main()