# Importar Biblioteclas
import csv
import math
import os
import pandas as pd
import statistics as st
# Importar Ferramentas
from Ferramentas.Álbum import Álbum
from Ferramentas.Título import Título

class Index:
	def __init__(self):
		self.nome = []
		self.artista = []
		self.id = []
		self.álbuns = []
		# Classificação
		self.usuário = []
		self.usuárioR = []
		self.pontuação = []

		self.Macústico = []
		self.DPacústico = []

		self.Mdançabilidade = []
		self.DPdançabilidade = []

		self.Menergia = []
		self.DPenergia = []

		self.Minstrumental = []
		self.DPinstrumental = []

		self.Maudiência = []
		self.DPaudiência = []

		self.Mfelicidade = []
		self.DPfelicidade = []

	def CalcularUsuário(self, acústico, dançabilidade, energia, instrumental, audiência, felicidade):
		self.usuário = [acústico, dançabilidade, energia, instrumental, audiência, felicidade]
		self.CalcularCaracterísticasRelativasUsuário()
		dados = [self.usuário,self.usuárioR]
		Título("Características Usuário","=")
		cabeçalho = ["acústico","dançabilidade","energia","instrumental","audiência","felicidade"]
		ind = ["Usuário", "Relativo"]
		print(pd.DataFrame(dados, index=ind, columns=cabeçalho))
		self.CalcularPontuação()

	def CalcularCaracterísticasRelativasUsuário(self):
		# ( (max + min) * usr / 100 ) + min
		self.usuárioR = []
		self.usuárioR.append(((max(self.Macústico)-min(self.Macústico))*self.usuário[0]/100)+min(self.Macústico))
		self.usuárioR.append(((max(self.Mdançabilidade)-min(self.Mdançabilidade))*self.usuário[1]/100)+min(self.Mdançabilidade))
		self.usuárioR.append(((max(self.Menergia)-min(self.Menergia))*self.usuário[2]/100)+min(self.Menergia))
		self.usuárioR.append(((max(self.Minstrumental)-min(self.Minstrumental))*self.usuário[3]/100)+min(self.Minstrumental))
		self.usuárioR.append(((max(self.Maudiência)-min(self.Maudiência))*self.usuário[4]/100)+min(self.Maudiência))
		self.usuárioR.append(((max(self.Mfelicidade)-min(self.Mfelicidade))*self.usuário[5]/100)+min(self.Mfelicidade))

	def CalcularPontuação(self):
		self.pontuação = []
		Mcaracterísticas = [self.Macústico, self.Mdançabilidade, self.Menergia, self.Minstrumental, self.Maudiência, self.Mfelicidade]
		DPcaracterísticas = [self.DPacústico, self.DPdançabilidade, self.DPenergia, self.DPinstrumental, self.DPaudiência, self.DPfelicidade]
		for i in range(len(self.álbuns)):
			pts = 0
			for j in range(len(Mcaracterísticas)):
				dist = abs(self.usuárioR[j]-Mcaracterísticas[j][i])
				distR = abs((Mcaracterísticas[j][i]+DPcaracterísticas[j][i]+Mcaracterísticas[j][i]) * dist * 100)
				mult = 0.1**distR
				pts += 100 * mult
			self.pontuação.append(pts)
		top10 = self.ImprimirTabelaPontuação(10)
		print(top10)

	def ImprimirTabelaPontuação(self, x):
		Título("Tabela Pontuação Álbuns", "=")
		dados = []
		cabeçalho = ["Artista", "Pontuação"]
		for i in range(len(self.álbuns)):
			dados.append([])
			# dados[i].append(self.nome[i])
			dados[i].append(self.artista[i])
			dados[i].append(self.pontuação[i])
		df = pd.DataFrame(dados, index=self.nome, columns=cabeçalho)
		dfs = df.sort_values(by=['Pontuação'], ascending=False)
		return str(dfs.head(x))
	
	def AdicionarCSVIndex(self, arq):
		with open(arq+".csv", encoding="utf-8") as arq_csv:
			leitor = csv.reader(arq_csv)
			for artista, nome, id in leitor:
				if(not self.PresenteIndex(artista,nome,id)):
					self.artista.append(artista)
					self.nome.append(nome)
					self.id.append(id)
					a = Álbum(artista,nome,id)
					try:
						a.CarregarCSV()
					except:	
						a.RegistrarÁlbum()
						a.Imprimir()
						a.SalvarCSV()
						Título(nome+".csv - SALVO", "=")
					self.álbuns.append(a)
		self.SalvarIndexCSV()
					
	def SalvarIndexCSV(self):
		dados = []
		for i in range(len(self.artista)):
			dados.append([])
			dados[i] = [self.artista[i],self.nome[i],self.id[i]]
		with open("indexT.csv", "w", newline="", encoding="utf-8") as arq_csv:
			escritor = csv.writer(arq_csv)
			escritor.writerows(dados)

	def CarregarIndexCSV(self, imprimir=False):
		self.artista = []
		self.nome = []
		self.id = []
		with open("index.csv", encoding="utf-8") as arq_csv:
			leitor = csv.reader(arq_csv)
			for artista, nome, id in leitor:
				self.artista.append(artista)
				self.nome.append(nome)
				self.id.append(id)
		self.CarregarÁlbunsIndex(imprimir)
		
	def CarregarÁlbunsIndex(self, imprimir=False):
		self.álbuns = []
		for i in range(len(self.artista)):
			a = Álbum(self.artista[i],self.nome[i],self.id[i])
			a.CarregarCSV()
			self.álbuns.append(a)
		for i in range(len(self.álbuns)):
			if(imprimir):
				self.álbuns[i].Imprimir()

			self.Macústico.append(self.álbuns[i].Macústico)
			self.DPacústico.append(self.álbuns[i].DPacústico)

			self.Mdançabilidade.append(self.álbuns[i].Mdançabilidade)
			self.DPdançabilidade.append(self.álbuns[i].DPdançabilidade)

			self.Menergia.append(self.álbuns[i].Menergia)
			self.DPenergia.append(self.álbuns[i].DPenergia)

			self.Minstrumental.append(self.álbuns[i].Minstrumental)
			self.DPinstrumental.append(self.álbuns[i].DPinstrumental)

			self.Maudiência.append(self.álbuns[i].Maudiência)
			self.DPaudiência.append(self.álbuns[i].DPaudiência)

			self.Mfelicidade.append(self.álbuns[i].Mfelicidade)
			self.DPfelicidade.append(self.álbuns[i].DPfelicidade)

		if(len(self.artista)>0):
			Título("Dados Index","=")
			print("Álbuns - ",len(self.álbuns))
			alb1 = 0
			for i in range(len(self.álbuns)):
				listM = self.álbuns[i].nomeMúsica
				if(len(listM)<2):
					alb1 += 1
			if(alb1>0):
				print("Álbuns com 1 música - ",alb1)
				Título("EXECUTANDO REMOÇÂO DE ÁLBUNS COM 1 MÚSICA","*")
				self.RemoverÁlbuns1Música()
				self.CarregarIndexCSV()

			Título("Média Características Álbuns","=")
			cabeçalho = ["acústico","dançabilidade","energia","instrumental","audiência","felicidade"]
			ind = ["MédiaMax","MédiaMédia","MédiaMin"]
			dados = [
				[max(self.Macústico),max(self.Mdançabilidade),max(self.Menergia),max(self.Minstrumental),max(self.Maudiência),max(self.Mfelicidade)],
				[st.mean(self.Macústico),st.mean(self.Mdançabilidade),st.mean(self.Menergia),st.mean(self.Minstrumental),st.mean(self.Maudiência),st.mean(self.Mfelicidade)],
				[min(self.Macústico),min(self.Mdançabilidade),min(self.Menergia),min(self.Minstrumental),min(self.Maudiência),min(self.Mfelicidade)]]
			print(pd.DataFrame(dados, index=ind, columns=cabeçalho))

	def RemoverÁlbuns1Música(self):
		novoArtista = []
		novoNome = []
		novoID = []
		for i in range(len(self.nome)):
			númeroMúsica = len(self.álbuns[i].nomeMúsica)
			if(númeroMúsica>1):
				novoNome.append(self.nome[i])
				novoArtista.append(self.artista[i])
				novoID.append(self.id[i])
			else:
				os.remove("Álbuns/"+self.nome[i]+".csv")
				Título(self.nome[i]+" - REMOVIDO","*")

		self.nome = novoNome
		self.artista = novoArtista
		self.id = novoID

		self.SalvarIndexCSV()

	def PresenteIndex(self, artista, nome, id):
		r = False
		for i in range(len(self.artista)):
			if((self.artista == artista and self.nome == nome)or(self.id == id)):
				r = True
				break
		return r