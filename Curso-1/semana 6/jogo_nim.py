
def computador_escolhe_jogada(n,m):
	if n <= m:
		return n

	quantidade = n % (m+1)

	if quantidade > 0:
		return quantidade

	return m

def usuario_escolhe_jogada(n,m):
	pecas_removidas = int(input("Quantas peças você vai tirar?"))
	
	while (pecas_removidas > m) or (pecas_removidas > n): 
		print("Oops! Jogada inválida! Tente de novo.")
		pecas_removidas = int(input("Quantas peças você vai tirar?"))
	
	return pecas_removidas

def partida():
	print("Defina as quantidades")
	n = int(input("Quantas peças? "))
	m = int(input("Limite de peças por jogada? "))

	while n < 1:
		print("O valor informado de peças é inválido!")
		n = int(input("Quantas peças? "))
		m = int(input("Limite de peças por jogada? "))

	if (n % (m+1)) == 0:
		print("Você começa!")
		computador_joga = False
	else:
		print("Computador começa!")
		computador_joga = True

	while n != 0:
		if computador_joga:
			pecas_removidas = computador_escolhe_jogada(n,m)
			print("O computador tirou",pecas_removidas,"peça.")
		else:
			pecas_removidas = usuario_escolhe_jogada(n,m)
			print("Você tirou",pecas_removidas,"peça.")

		n -= pecas_removidas

		print("Agora resta(m)", n, "peça(s) no tabuleiro.\n")

		computador_joga = not computador_joga


def campeonato():
	contador = 1
	while contador < 4:
		print("**** Rodada",contador,"****")
		partida()
		contador += 1

print("Bem-vindo ao jogo do NIM! Escolha:")
print("1 - para jogar uma partida isolada")
inicio_de_jogo = int(input("2 - para jogar um campeonato "))

if inicio_de_jogo == 2:
	print("Voce escolheu um campeonato!")
	campeonato()
	print("**** Final do campeonato! ****")
	print("Placar: Você 0 X 3 Computador")
else:
	partida()
	print("Fim do jogo! O computador ganhou!")
