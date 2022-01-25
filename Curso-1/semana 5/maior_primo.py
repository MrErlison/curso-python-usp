
def primalidade(numero):
    contador = 1
    primo = True

    while (contador <= numero) and primo:
        contador += 1
        if ((numero % contador) == 0) and (contador != numero):
            return False

    return True


def maior_primo(numero):

    while numero >= 2:
        if primalidade(numero):
            return numero
        numero -= 1

