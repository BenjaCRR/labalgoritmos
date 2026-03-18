x=True
users=[]
while x==True:
    user=input("¿Quien anda ahí? (ponga ´f´ para terminar de escribir): ")
    if user=="f":
        x=False
    else:
        x=True
        users.append(user)

print(users)


for u in users:
    if u=="admin":
        print("klk mi admin")
    elif u!="admin":
        print("Hola ",u," es un placer verlo/a de vuelta")
    else:
        print("LISTA VACÍA")
        