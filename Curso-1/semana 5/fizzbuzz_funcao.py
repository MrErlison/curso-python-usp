
def fizzbuzz(numero):
	
	retorno = ""

	if (numero % 3) == 0:
		retorno += "Fizz"

	if (numero % 5) == 0:
		retorno += "Buzz"

	if retorno == "":
		return numero

	return retorno
