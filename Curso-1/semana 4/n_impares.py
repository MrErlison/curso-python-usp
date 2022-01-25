
numero = int( input("Digite o valor de n: ") )
contador = 0

while numero > 0:
    if (contador % 2) != 0:
        print(contador)
        numero -= 1
    contador += 1
