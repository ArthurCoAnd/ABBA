# Importar Biblioteclas
import csv
import os
import pandas as pd
import PySimpleGUI as psg
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

class Aplicativo:
	def __init__(self):
		# Carregar Index
		self.index = Index()
		self.index.CarregarIndexCSV()
		
		layout = [
			[psg.Text("Album Basic Balance Analyzer")],
			[psg.Frame("Caractarísticas",[
				[psg.Text("Sintetizada", size=(15,1), justification="right"), psg.Slider(range=(0, 100), orientation='h', size=(50, 15), default_value=50, key="acústico"), psg.Text("Acústica", size=(15,1), justification="left")],
				[psg.Text("Paradas", size=(15,1), justification="right"), psg.Slider(range=(0, 100), orientation='h', size=(50, 15), default_value=50, key="dançabilidade"), psg.Text("Dançantes", size=(15,1), justification="left")],
				[psg.Text("Calmas", size=(15,1), justification="right"), psg.Slider(range=(0, 100), orientation='h', size=(50, 15), default_value=50, key="energia"), psg.Text("Enérgicas", size=(15,1), justification="left")],
				[psg.Text("Instrumental", size=(15,1), justification="right"), psg.Slider(range=(0, 100), orientation='h', size=(50, 15), default_value=50, key="instrumental"), psg.Text("Cantada", size=(15,1), justification="left")],
				[psg.Text("Estúdio", size=(15,1), justification="right"), psg.Slider(range=(0, 100), orientation='h', size=(50, 15), default_value=50, key="audiência"), psg.Text("Ao Vivo", size=(15,1), justification="left")],
				[psg.Text("Tristes", size=(15,1), justification="right"), psg.Slider(range=(0, 100), orientation='h', size=(50, 15), default_value=50, key="felicidade"), psg.Text("Felizes", size=(15,1), justification="left")]
				])],
			[psg.Button("Calcular")],
			[psg.Text(size=(100,11), key='resp', font="Consolas 9",visible=False)]
			# [psg.Output(size=(100,11),key="resp",font="Consolas 9",visible=False)]
		]

		self.janela = psg.Window("ABBA", icon='Imagens/notaLogo.ico', resizable=False).layout(layout)

	def Iniciar(self):
		while True:
			eventos, valores = self.janela.Read()
			if eventos == psg.WINDOW_CLOSED:
				break
			if eventos == "Calcular":
				self.index.CalcularUsuário(valores["acústico"],valores["dançabilidade"],valores["energia"],valores["instrumental"],valores["audiência"],valores["felicidade"])
				self.janela["resp"].update(value=self.index.ImprimirTabelaPontuação(10), visible=True)
		self.janela.close()

if __name__ == "__main__":
	Título("ABBA - Album Basic Balance Analyzer", "=")
	psg.theme('DarkAmber')
	app = Aplicativo()
	app.Iniciar()

	# # Exemplo de Código de Download e Cálculo de um Álbum Específico
	# alb = Álbum("The Strokes","The New Abnormal","2xkZV2Hl1Omi8rk2D7t5lN")
	# alb.RegistrarÁlbum()
	# alb.Imprimir()

