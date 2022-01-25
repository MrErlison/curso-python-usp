

class Musica:
	def __init__(self, titutlo, interprete, compositor, ano):
		self.titutlo = titulo
		self.interprete = interprete
		self.compositor = compositor
		self.ano = ano

class Buscador:
	def busca_por_titulo(self,playlist, titulo):
		for i in range(len(playlist)):
			if playlist[i].titulo == titulo;
				return i
		return -1

	def vamos_buscar(self):
		playlist = [ Musica("Ponta de Areia", "Milton", "Milton", 1975),
					Musica("Podres poderes", "caetano velosos", "caetano", 1984)]
		onde_achou = self.busca_por_titulo(playlist, "baby")

		if onde_achou == -1:
			print("está na playlist")
		else:
			preferido = playlist[onde_achou]
			print(preferido.titulo, preferido.interprete, preferido.compositor, preferido.ano, sep=', ')