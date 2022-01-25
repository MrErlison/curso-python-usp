
''' recebe uma frase (uma string) como parâmetro e 
    devolve uma string com as letras maiúsculas que existem nesta frase, 
    na ordem em que elas aparecem '''
def maiusculas(frase):
    m = ""

    for i in frase:
        if 90 >= ord(i) >= 65:
            m += i

    return m