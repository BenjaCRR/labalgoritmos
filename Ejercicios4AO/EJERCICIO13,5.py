print("Ingrese su top tres frutas favoritas.")
toptres=[]
for i in range(1,4):
    fruta=input("ingresar fruta: " )
    toptres.append(fruta)
print(toptres)

for f in toptres:
    if f=="kiwi":
        print("Te gusta el kiwi, como a mí!")
    elif f=="anana":
        print("A mí tambíen me gusta el ananá")
    elif f=="pera":
        print("Amo la pera!")

