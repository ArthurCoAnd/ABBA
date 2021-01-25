# Improtar Bibliotecas
import csv
import pandas as pd
import statistics as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# Improtar Ferramentas
from Ferramentas.Título import Título
# Importar Autenticadores
from auth import *

# Fazer "Login" Spotfy
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=cID,client_secret=cS))

class Álbum:
	def __init__(self, Artista, Nome, id):
		# Dados Álbum
		self.artista = Artista
		self.nome = Nome
		self.id = id
		
		# Dados Músicas
			# Gerais
		self.nomeMúsica = []
		self.idMúsica = []
				# duration_ms
		self.duração = []
		self.Mduração = None
		self.DPduração = None
			# Características
				# popularity
		self.popularidade = []
		self.Mpopularidade = None
		self.DPpopularidade = None
				# key
		self.tom = []
				# mode
		self.modoTom = []
				# time_signature
		self.tempo = []
				# acousticness
		self.acústico = []
		self.Macústico = None
		self.DPacústico = None
				# danceability
		self.dançabilidade = []
		self.Mdançabilidade = None
		self.DPdançabilidade = None
				# energy
		self.energia = []
		self.Menergia = None
		self.DPenergia = None
				# instrumentalness
		self.instrumental = []
		self.Minstrumental = None
		self.DPinstrumental = None
				# liveness
		self.audiência = []
		self.Maudiência = None
		self.DPaudiência = None
				# loudness
		self.barulho = []
		self.Mbarulho = None
		self.DPbarulho = None
				# speechiness
		self.fala = []
		self.Mfala = None
		self.DPfala = None
				# valence
		self.felicidade = []
		self.Mfelicidade = None
		self.DPfelicidade = None
				# tempo
		self.bpm = []
		self.Mbpm = None
		self.DPbpm = None

	def RegistrarÁlbum(self):
		# Baixar Dados URL Spotfy
		dA = sp.album_tracks(self.id)

		# Cadastrar Músicas do Álbum
		for i, m in enumerate(dA['items']):
			# Dados Gerais
			self.nomeMúsica.append(m['name'])
			self.idMúsica.append(m['id'])

			# Dados Música
			dM = sp.track(self.idMúsica[i])
			self.duração.append(float(int(dM['duration_ms'])/1000))
			self.popularidade.append(dM['popularity'])

			# Características Música
			cM = sp.audio_features(self.idMúsica[i])
			self.tom.append(int(cM[0]['key']))
			self.modoTom.append(int(cM[0]['mode']))
			self.tempo.append(int(cM[0]['time_signature']))
			self.acústico.append(float(cM[0]['acousticness']))
			self.dançabilidade.append(float(cM[0]['danceability']))
			self.energia.append(float(cM[0]['energy']))
			self.instrumental.append(float(cM[0]['instrumentalness']))
			self.audiência.append(float(cM[0]['liveness']))
			self.barulho.append(float(cM[0]['loudness']))
			self.fala.append(float(cM[0]['speechiness']))
			self.felicidade.append(float(cM[0]['valence']))
			self.bpm.append(float(cM[0]['tempo']))

		self.CacularEstatísticas()

	def CacularEstatísticas(self):
			# duration_ms
		self.Mduração = st.mean(self.duração)
		self.DPduração = st.pstdev(self.duração)
			# popularity
		self.Mpopularidade = st.mean(self.popularidade)
		self.DPpopularidade = st.pstdev(self.popularidade)
			# acousticness
		self.Macústico = st.mean(self.acústico)
		self.DPacústico = st.pstdev(self.acústico)
			# danceability
		self.Mdançabilidade = st.mean(self.dançabilidade)
		self.DPdançabilidade = st.pstdev(self.dançabilidade)
			# energy
		self.Menergia = st.mean(self.energia)
		self.DPenergia = st.pstdev(self.energia)
			# instrumentalness
		self.Minstrumental = st.mean(self.instrumental)
		self.DPinstrumental = st.pstdev(self.instrumental)
			# liveness
		self.Maudiência = st.mean(self.audiência)
		self.DPaudiência = st.pstdev(self.audiência)
			# loudness
		self.Mbarulho = st.mean(self.barulho)
		self.DPbarulho = st.pstdev(self.barulho)
			# speechiness
		self.Mfala = st.mean(self.fala)
		self.DPfala = st.pstdev(self.fala)
			# valence
		self.Mfelicidade = st.mean(self.felicidade)
		self.DPfelicidade = st.pstdev(self.felicidade)
			# tempo
		self.Mbpm = st.mean(self.bpm)
		self.DPbpm = st.pstdev(self.bpm)

	def Imprimir(self):
		Título((self.artista + " - " + self.nome),"=")
		cabeçalho = ["Música","ID","Duração (s)","Popularidade","Tom","Modo Tom","Tempo","Acústico","Dançabilidade","Energia","Instrumental","Audiência","Barulho","Fala","Felicidade","BPM"]
		dados = []
		for i in range(len(self.nomeMúsica)):
			dados.append([])
			dados[i].append(self.nomeMúsica[i])
			dados[i].append(self.idMúsica[i])
			dados[i].append(self.duração[i])
			dados[i].append(self.popularidade[i])
			dados[i].append(self.tom[i])
			dados[i].append(self.modoTom[i])
			dados[i].append(self.tempo[i])
			dados[i].append(self.acústico[i])
			dados[i].append(self.dançabilidade[i])
			dados[i].append(self.energia[i])
			dados[i].append(self.instrumental[i])
			dados[i].append(self.audiência[i])
			dados[i].append(self.barulho[i])
			dados[i].append(self.fala[i])
			dados[i].append(self.felicidade[i])
			dados[i].append(self.bpm[i])
		print(pd.DataFrame(dados,columns=cabeçalho))
		self.ImprimirEstatísticas()

	def ImprimirEstatísticas(self):
		print("= Estatísticas =")
		cabeçalho = ["Popularidade","Acústico","Dançabilidade","Energia","Instrumental","Audiência","Barulho","Fala","Felicidade","BPM"]
		linhas = ["Média","Desvio Padrão"]
		m = [self.Mpopularidade,self.Maudiência,self.Mdançabilidade,self.Menergia,self.Minstrumental,self.Maudiência,self.Mbarulho,self.Mfala,self.Mfelicidade,self.Mbpm]
		dp = médias = [self.DPpopularidade,self.DPaudiência,self.DPdançabilidade,self.DPenergia,self.DPinstrumental,self.DPaudiência,self.DPbarulho,self.DPfala,self.DPfelicidade,self.DPbpm]
		dados = [m,dp]
		print(pd.DataFrame(dados,columns=cabeçalho, index=linhas))

	def SalvarCSV(self):
		# Salvar Dados Músicas
		dados = []
		for i in range(len(self.nomeMúsica)):
			dados.append([])
			dados[i].append(self.nomeMúsica[i])
			dados[i].append(self.idMúsica[i])
			dados[i].append(self.duração[i])
			dados[i].append(self.popularidade[i])
			dados[i].append(self.tom[i])
			dados[i].append(self.modoTom[i])
			dados[i].append(self.tempo[i])
			dados[i].append(self.acústico[i])
			dados[i].append(self.dançabilidade[i])
			dados[i].append(self.energia[i])
			dados[i].append(self.instrumental[i])
			dados[i].append(self.audiência[i])
			dados[i].append(self.barulho[i])
			dados[i].append(self.fala[i])
			dados[i].append(self.felicidade[i])
			dados[i].append(self.bpm[i])

			# Criar Arquivo
		nomeArq = "Álbuns/" + self.nome + ".csv"
		with open(nomeArq, "w", newline="", encoding="utf-8") as arq_csv:
			escritor = csv.writer(arq_csv)
			escritor.writerows(dados)

	def CarregarCSV(self):
		nomeArq = "Álbuns/" + self.nome + ".csv"
		with open(nomeArq, encoding="utf-8") as arq_csv:
			leitor = csv.reader(arq_csv)
			for m in leitor:
				self.nomeMúsica.append(m[0])
				self.idMúsica.append(m[1])
				self.duração.append(float(m[2]))
				self.popularidade.append(int(m[3]))
				self.tom.append(int(m[4]))
				self.modoTom.append(int(m[5]))
				self.tempo.append(int(m[6]))
				self.acústico.append(float(m[7]))
				self.dançabilidade.append(float(m[8]))
				self.energia.append(float(m[9]))
				self.instrumental.append(float(m[10]))
				self.audiência.append(float(m[11]))
				self.barulho.append(float(m[12]))
				self.fala.append(float(m[13]))
				self.felicidade.append(float(m[14]))
				self.bpm.append(float(m[15]))
		self.CacularEstatísticas()