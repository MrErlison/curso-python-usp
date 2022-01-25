
''' recebe uma lista de strings com nome de pessoas como parâmetro e
	devolve o nome mais curto presente na lista. '''
def menor_nome(nomes):

	menor_nome = nomes[0]

	for i in nomes:
		nome = i.strip().lower()
		if len(nome) < len(menor_nome):
			menor_nome = nome

	return menor_nome.capitalize()
