from bs4 import BeautifulSoup
import requests

class Perfil:
	def __init__(self, NomeDeUsuario):
		self.NomeDeUsuario = NomeDeUsuario
		self.getDados(NomeDeUsuario)
	
	def getDados(self,NomeDeUsuario):
		CaminhoPerfil = 'https://onibusbrasil.com/'+ NomeDeUsuario
		
		Requisicao = requests.get(CaminhoPerfil, timeout=5)
		ConteudoDaPagina = BeautifulSoup(Requisicao.content, "html.parser")
		DadosPrincipais = ConteudoDaPagina.find_all('a',class_='color-white')[0].text
		
		ConteudoTextual = []
		ConteudoTextual.append(DadosPrincipais)
		
		self.numeroFotos = ConteudoDaPagina.find_all('strong',)[1].text
		self.numeroVisualizacoes = ConteudoDaPagina.find_all('strong',)[2].text
		self.numeroComentarios = ConteudoDaPagina.find_all('strong',)[3].text
		self.nome = ConteudoTextual[0].split('\n')

	def mostrarDados(self):
		print ("Nome do usuario:",self.nome[1])
		print ("Numero de fotos postadas:",  self.numeroFotos)
		print ("Numero de visualizações:",  self.numeroVisualizacoes)
		print ("Numero de comentários:",  self.numeroComentarios)










print("script que coleta informações de um perfil no onibusbrasil.com")


opcao = input("deseja cadastrar um novo nome de usuario?S/N")
if opcao == "S" or opcao == "s":
	f= open("cache.txt","w+")
	user_name = input("digite o nome do usuario sem o @")
	f.write(user_name)
else:
	f=open("cache.txt", "r")
	user_name = f.read()
f.close()

Usuario = Perfil(user_name)
Usuario.mostrarDados()

input("digite a tecla ENTER para finalizar...")
exit()

