

def soma_lista(lista):
	final = len(lista)-1

	if final == 0:
		return lista[final]

	return lista[-1] + soma_lista(lista[:final])
