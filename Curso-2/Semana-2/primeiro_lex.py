
def primeiro_lex(lista):

	primeiro = lista[0]

	for i in lista:
		if i < primeiro:
			primeiro = i

	return primeiro