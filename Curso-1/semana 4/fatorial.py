
numero = int( input("Digite o valor de n: ") )

if numero == 0:
    fatorial = 1
else:
    fatorial = numero

while numero > 1:
    fatorial *= (numero - 1)
    numero -= 1

print(fatorial)
