numero = int( input("Digite o valor") )
contador = 1
primo = True

while (contador <= numero) and primo:
    contador += 1
    if ((numero % contador) == 0) and (contador != numero):
        primo = False

if primo:
    print("primo")
else:
    print("não primo")
