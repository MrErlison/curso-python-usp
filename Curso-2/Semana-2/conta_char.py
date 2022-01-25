
def conta_letras(frase, contar="vogais"):
	
	# a=97 e=101 i=105 o=111 u=117
	vogais = [97, 101, 105, 111, 117]

	excluir = [" "]

	total_vogais = 0
	total = 0

	for i in frase:
		if ord(i.lower()) in vogais:
			total_vogais += 1

		if i not in excluir: 
			total += 1

	if contar == "vogais":
		return total_vogais

	return total - total_vogais