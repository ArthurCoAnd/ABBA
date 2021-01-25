# Importar Biblioteclas
import csv
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# Importar Autenticadores
from auth import *

# Fazer "Login" Spotfy
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=cID,client_secret=cS))

class Música:
	def __init__(self, Nome, id):
		# Dados Música
		self.nome = Nome
		self.artista = ""
		self.id = id
			# duration_ms
		self.duração = None
			# popularity
		self.popularidade = None
			# key
		self.tom = None
			# mode
		self.modoTom = None
			# time_signature
		self.tempo = None
			# acousticness
		self.acústico = None
			# danceability
		self.dançabilidade = None
			# energy
		self.energia = None
			# instrumentalness
		self.instrumental = None
			# liveness
		self.audiência = None
			# loudness
		self.barulho = None
			# speechiness
		self.fala = None
			# valence
		self.felicidade = None
			# tempo
		self.bpm = None

	def RegistrarMúsica(self):
		# Dados Música
		dM = sp.track(self.id)
		self.artista = dM['artists'][0]['name']
		self.duração = float(int(dM['duration_ms'])/1000)
		self.popularidade = int(dM['popularity'])

		# Características Música
		cM = sp.audio_features(self.id)
		self.tom = int(cM[0]['key'])
		self.modoTom = int(cM[0]['mode'])
		self.tempo = int(cM[0]['time_signature'])
		self.acústico = float(cM[0]['acousticness'])
		self.dançabilidade = float(cM[0]['danceability'])
		self.energia = float(cM[0]['energy'])
		self.instrumental = float(cM[0]['instrumentalness'])
		self.audiência = float(cM[0]['liveness'])
		self.barulho = float(cM[0]['loudness'])
		self.fala = float(cM[0]['speechiness'])
		self.felicidade = float(cM[0]['valence'])
		self.bpm = float(cM[0]['tempo'])