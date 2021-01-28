# Importar Biblioteclas
import csv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# Improtar Classes
from Ferramentas.Álbum import Álbum
from Ferramentas.Index import Index
from Ferramentas.Título import Título
# Importar Autenticadores
from auth import *

# Fazer "Login" Spotfy
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=cID,client_secret=cS))

# Procura ID spotify de um arquivo .CSV com Nome do Artista e Nome do Álbum
def ProcurarID(arq):
		alb = []
		# Ler Aqrquivo com Artista e Nome
		with open(arq+".csv", encoding="utf-8") as arq_csv:
			leitor = csv.reader(arq_csv)
			for artista, nome in leitor:
				Título(artista+" - "+nome,"=")
				busca = sp.search(nome,limit=1,type='album')
				# id = print(busca['albums']['items'][0]['id'])
				try:
					id = busca['albums']['items'][0]['id']
					alb.append([artista,nome,id])
				except:
					print("Álbum não cadastrado!!!")
		# Criar Arquivo com Artista, Nome e id
		with open(arq+"IDX.csv", "w", newline="", encoding="utf-8") as arq_csv:
			escritor = csv.writer(arq_csv)
			escritor.writerows(alb)

# Baixa dados de um álbum que pode ser usado para registrar no index
def RegistrarÁlbum(alb):
	# Baixar Dados URL Spotfy
	dA = sp.album_tracks(alb.id)

	# Cadastrar Músicas do Álbum
	for i, m in enumerate(dA['items']):
		# Dados Gerais
		alb.nomeMúsica.append(m['name'])
		alb.idMúsica.append(m['id'])

		# Dados Música
		dM = sp.track(alb.idMúsica[i])
		alb.duração.append(float(int(dM['duration_ms'])/1000))
		alb.popularidade.append(dM['popularity'])

		# Características Música
		cM = sp.audio_features(alb.idMúsica[i])
		alb.tom.append(int(cM[0]['key']))
		alb.modoTom.append(int(cM[0]['mode']))
		alb.tempo.append(int(cM[0]['time_signature']))
		alb.acústico.append(float(cM[0]['acousticness']))
		alb.dançabilidade.append(float(cM[0]['danceability']))
		alb.energia.append(float(cM[0]['energy']))
		alb.instrumental.append(float(cM[0]['instrumentalness']))
		alb.audiência.append(float(cM[0]['liveness']))
		alb.barulho.append(float(cM[0]['loudness']))
		alb.fala.append(float(cM[0]['speechiness']))
		alb.felicidade.append(float(cM[0]['valence']))
		alb.bpm.append(float(cM[0]['tempo']))
	
	alb.CacularEstatísticas()

if __name__ == "__main__":
	Título("Registrador de Álbuns - ABBA", "=")
	
	# # Exemplo de Código de Procurar ID spotify de uma lista
	# ProcurarID("Listas Álbuns/Top100BrCP")
	
	# # Exemplo de Código de Download e Cálculo de um Álbum Específico
	# alb = Álbum("The Strokes","The New Abnormal","2xkZV2Hl1Omi8rk2D7t5lN")
	# RegistrarÁlbum(alb)
	# alb.Imprimir()

