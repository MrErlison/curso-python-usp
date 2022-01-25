import random

def lista_grande(n):
	lista = []
	for i in range(n):
		lista.append( random.randrange(1, n*10))
	return lista

# refatorado
def lista_grande(n):
	return [ramdom.randrange(n) for i in range(n)]