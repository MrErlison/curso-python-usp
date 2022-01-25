import pytest

def busca(lista, elemento):
	primeiro = 0
	ultimo = len(lista)-1

	while primeiro <= ultimo:
		meio = (primeiro + ultimo)//2
		if lista[meio] == elemento:
			return meio

		if elemento < lista[meio]:
			ultimo = meio - 1
		else:
			primeiro = meio + 1

	return False


# refatorado
def busca_binaria(lista, elemento, minimo=0, maximo=None):
	if maximo == None:
		maximo = len(lista) - 1

	if maximo < minimo:
		return False

	meio = minimo + (maximo - minimo) // 2

	if lista[meio] > elemento:
		return busca_binaria(lista, elemento, minimo, meio-1)
	elif lista[meio] < elemento:
		return busca_binaria(lista, elemento, meio+1, maximo)
	else:
		return meio 



a = [10, 20, 30, 40, 50, 60]

@pytest.mark.parametrize("lista, valor, esperado", [
	(a, 10, 0),
	(a, 20, 1),
	(a, 30, 2),
	(a, 40, 3),
	(a, 50, 4),
	(a, 60, 5),
	(a, 70, False),
	(a, 15, False),
	(a, -10, False)
	])

def testa_busca_binaria(lista, valor, esperado):
	assert busca_binaria(lista, valor) == esperado
