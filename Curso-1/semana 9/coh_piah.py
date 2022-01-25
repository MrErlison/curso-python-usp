import re, math

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def conta_caracteres(lista):
    ''' Conta o numero de caracteres de uma lista '''
    total = 0 
    
    for i in lista:
        total += len(i)

    return total


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e 
    deve devolver o grau de similaridade nas assinaturas.'''
    sum = 0
    for i in range(6):
        sum += math.fabs(as_a[i] - as_b[i])

    return sum / 6


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e 
    deve devolver a assinatura do texto.'''

    frases = []
    palavras = []

    sentencas = separa_sentencas(texto)
    for sentenca in sentencas:
        frases += separa_frases(sentenca)

    for frase in frases:
        palavras += separa_palavras(frase)
    
    total_sentencas = len(sentencas)
    total_frases = len(frases)    
    total_palavras = len(palavras)
    
    ''' Média simples do número de caracteres por palavra. '''
    wal = conta_caracteres(palavras) / total_palavras

    ''' Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras. '''
    ttr = n_palavras_diferentes(palavras) / total_palavras

    ''' Número de palavras utilizadas uma única vez dividido pelo número total de palavras. '''
    hlr = n_palavras_unicas(palavras) / total_palavras

    ''' Média simples do número de caracteres por sentença. '''
    sal = conta_caracteres(sentencas) / total_sentencas

    ''' Média simples do número de frases por sentença. '''
    sac = total_frases / total_sentencas

    ''' Média simples do número de caracteres por frase. '''
    pal = conta_caracteres(frases) / total_frases

    return [wal, ttr, hlr, sal, sac, pal]


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e 
    deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
   
    infectados = []
   
    for texto in textos:
        assinatura = calcula_assinatura(texto)
        grau_similaridade = compara_assinatura(ass_cp, assinatura)
        infectados.append(grau_similaridade)

    return infectados.index(min(infectados)) + 1
