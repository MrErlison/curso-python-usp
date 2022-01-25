import time
import random

class Buscador:
	def busca_sequencial(self, lista, x):
		for i in range(len(lista)):
			if lista[i] == x:
				return i
		return -1

	def busca_binaria(self, lista, x):
		primeiro =0
		ultimo = len(lista)-1

		while primeiro <= ultimo:
			meio = (primeiro + ultimo)//2
			if lista[meio] == x:
				return meio
			else:
				if x < lista[meio]:
					ultimo = meio - 1
				else:
					primeiro = meio + 1
		return -1


n = 100

lista = [random.randrange(n) for i in range(n)]
lista.append(9999)
lista.sort()

b = Buscador()

a = time.time()
b.busca_sequencial(lista, -9999)
d = time.time()
print("sequencial", d - a)

a = time.time()
b.busca_binaria(lista, -9999)
d = time.time()
print("binaria", d - a)
