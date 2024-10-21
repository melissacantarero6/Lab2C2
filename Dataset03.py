"""
https://www.kaggle.com/datasets/surajjha101/top-youtube-channels-data

Al revisar el archivo CSV, nos encontramos con un dato interesante: el canal Tserie es el que tiene el mayor número de suscriptores.
Esto se hace evidente al observar el gráfico de líneas, que muestra un crecimiento impresionante en su audiencia.
Este éxito no es casualidad. Es probable que la calidad del contenido, 
la frecuencia con la que publican y la conexión que establecen con su comunidad sean factores clave en este aumento de seguidores. 
Sin duda, Tserie ha logrado captar la atención de muchos, 
y su crecimiento es un testimonio del impacto que pueden tener en el mundo digital.
"""
import pandas as pd
import matplotlib.pyplot as plt

#Llamar el CSV a trabajar
FrananCrack = pd.read_csv("youtuber.csv")

#Eliminar las comas en la columna 'subscribers' y convertir a números porque sino no saldran datos (error que nos tomo 30 minutos resolver)
FrananCrack['subscribers'] = FrananCrack['subscribers'].str.replace(',', '').astype(float)

#Verificar los datos procesados
print(FrananCrack[['Youtuber', 'subscribers']])

#Ordenar por número de suscriptores
FrananCrack_sorted = FrananCrack.sort_values(by='subscribers', ascending=False).head(10)

#Graficar los datos con un gráfico de líneas
plt.figure(figsize=(10, 6))
plt.plot(FrananCrack_sorted['Youtuber'], FrananCrack_sorted['subscribers'], marker='o', color='skyblue', linestyle='-')

plt.xlabel('Youtuber')
plt.ylabel('Suscriptores')
plt.title('Top 10 Youtubers por número de suscriptores')
plt.xticks(rotation=45, ha='right')  # Rotar los nombres de los Youtubers para mejor legibilidad
plt.tight_layout()  # Ajustar el layout para evitar que se corte el texto

plt.show()