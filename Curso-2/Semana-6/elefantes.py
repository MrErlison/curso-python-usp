

def incomodam(n):

	if n < 1:
		return ""
	
	texto = "incomodam "
	if n == 1:
		return texto
	
	n -= 1

	return incomodam(n) + texto


def elefantes(n):
	if n < 1:
		return ""

	if n == 1:
		musica = "Um elefante incomoda muita gente\n"
		return musica

	if n-1 == 1:
		musica = "Um elefante incomoda muita gente\n"
		musica += str(n) + " elefantes " + incomodam(n) + "muito mais\n"
		return musica
	else:
		musica = str(n-1) + " elefantes incomodam muita gente\n"
		musica += str(n) + " elefantes " + incomodam(n) + "muito mais\n"
		
	n -= 1

	return elefantes(n) + musica
