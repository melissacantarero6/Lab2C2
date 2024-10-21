"""
https://www.kaggle.com/datasets/aayushmishra1512/twitchdata

se puede observar que el canal de tiwch de la empresa Riot Games es quien tiene 14.7%
la mayor cantidad de viewers en sus en vivos de twitch, este canal muestra los envivos de los torneos de LOL
y el Torneo de la VCT valorant ya que son juegos bastantes queridos de la comunidad Gamer,
y abajo de este canal podemos observar que sigue The Greft con 12.4% el es de habla hispana y su contenido es variado 
y por ultimo podemos observar a JokerDTV con un 7.4%
"""

#aqui le tiramos la call a las librerias
import pandas as pd
import matplotlib.pyplot as plt

#cargar el archivo
power = pd.read_csv("twicht.csv")

#agrupar por canal y sumar el numero de peak viewers
data = power.groupby('Channel')['Peak viewers'].sum()

#seleccionar los 10 canales con más "Peak viewers"
top10 = data.nlargest(10)

#crear gráfico de pastel(pie) con los primeros 10
plt.pie(top10.values, labels=top10.index, autopct="%1.1f%%")

#titulo y salida en consola
plt.title("Top 10 Canales y su Popularidad")
plt.show()