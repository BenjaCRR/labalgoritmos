edad= int(input("ingrese su edad: "))

if edad < 2:
    print("eres un bebe")
elif edad >= 2 and edad < 4:
    print("eres un niño chiquito")
elif edad >= 4 and edad < 13:
    print("eres un niño")
elif edad >= 13 and edad < 20:
    print("eres un adolecente")
elif edad >= 20 and edad < 65:
    print("eres un adulto")
else: 
    print("eres un adulto mayor")