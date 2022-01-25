def busca(lista, elemento):
	posicao = 0
	for i in lista:
		if i == elemento:
			return posicao
		posicao += 1
		
	return False
