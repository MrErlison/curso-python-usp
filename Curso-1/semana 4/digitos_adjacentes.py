
numero = int( input("Digite o valor: ") )
adj = False

while (not adj) and (numero > 0):
    if (numero % 10) == ( (numero // 10) % 10 ):
        adj = True
    numero = numero // 10

if adj:
    print("sim")
else:
    print("não")
