# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tYqvXXHsyi5PBwRAowCW2l_kwVBA7QSt
"""



#//Importación de librerías necesarias
import numpy as np  # //Para operaciones matemáticas y manejo de arrays
import pandas as pd  # //Para manipulación de datos en formato DataFrame
import matplotlib.pyplot as plt  # //Para visualización gráfica
from sklearn.cluster import KMeans  # //Para el algoritmo de clustering K-means
from sklearn.datasets import make_blobs  # //Para crear datos simulados

#//Generación de un conjunto de datos de ejemplo
data, labels = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# //Convertimos los datos generados en un DataFrame para manipularlos fácilmente
df = pd.DataFrame(data, columns=["X", "Y"])

# //Visualización de los datos antes de aplicar el clustering
plt.scatter(df["X"], df["Y"], s=50, color='blue', label='Datos Originales')  #//Graficar los puntos de datos
plt.title('Datos antes del clustering')  # Título del gráfico
plt.xlabel('Eje X')  # Etiqueta eje X
plt.ylabel('Eje Y')  # Etiqueta eje Y
plt.legend()  # Mostrar la leyenda
plt.show()  # Mostrar la gráfica

#// Aplicar el algoritmo K-means
kmeans = KMeans(n_clusters=4, random_state=0)  #//Crear el modelo con 4 clusters
kmeans.fit(df)  # Ajustar el modelo con los datos

# //Obtener los resultados del clustering
clusters = kmeans.labels_  # Etiquetas de los clusters asignadas a cada punto
centroids = kmeans.cluster_centers_  #//Obtener las coordenadas de los centroides

# //Agregar las etiquetas de los clusters al DataFrame
df['Cluster'] = clusters

# //Visualización de los resultados del clustering
plt.scatter(df["X"], df["Y"], c=df["Cluster"], s=50, cmap='viridis', label='Clusters')  # Graficar puntos con colores según el cluster
plt.scatter(centroids[:, 0], centroids[:, 1], s=200, c='red', marker='x', label='Centroides')  # Graficar centroides
plt.title('Resultado del clustering con K-means')  #//Título del gráfico
plt.xlabel('Eje X')  #// Etiqueta eje X
plt.ylabel('Eje Y')  #// Etiqueta eje Y
plt.legend()  #// Mostrar la leyenda
plt.show()  #// Mostrar la gráfica