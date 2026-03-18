lugares=["Y","A","L","F","S"]
print("lista original: ", lugares)

print("Usando sorted: ", sorted(lugares))
print("")
print("La lista aún sigue siendo como la original: ", lugares)

print("")
lugares.reverse()
print("Lista reversed: ",lugares)
lugares.reverse()
print("Revertido nuevamente (Original): ",lugares )

print("")
lugares.sort()
print("Lista ordenada alfabéticamente con sort(): ", lugares)
lugares.sort(reverse=True)
print("Lista en orden alfabético inverso con sort(): ", lugares)
