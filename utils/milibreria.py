import fire
import streamlit as st
import matplotlib as plt
import numpy as np
import pandas as pd
import seaborn as sns
import plotly_express as px
import plotly.graph_objects as go
from PIL import Image
import requests
from streamlit_option_menu import option_menu
from datetime import datetime
from dateutil.relativedelta import relativedelta
import time
import base64
from utils.milibreria import * 
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder
import pickle


# Leemos los Datasets
acción = pd.read_csv("data/accion_limpio.csv")
aventura = pd.read_csv("data/aventura_limpio.csv")
deportes = pd.read_csv("data/deportes_limpio.csv")
earlyacces = pd.read_csv("data/early_limpio.csv")
estrategia = pd.read_csv("data/estrategia_limpio.csv")
free = pd.read_csv("data/free_limpio.csv")
mmo = pd.read_csv("data/mmorpg_limpio.csv")
rpg = pd.read_csv("data/rpg_limpio.csv")
simulacion = pd.read_csv("data/simulacion_limpio.csv")
indie = pd.read_csv("data/indie_limpio.csv")
dfjunto = pd.read_csv("data/dfjunto.csv")
pyca_filtered = pd.read_csv("data/pyca_filtered.csv")
arima = pd.read_csv("data/arima.csv")
#GRAFICO DE PRECIO MEDIO - AÑO (DE PINCHOS)-------------------------------------------
dfjunto['Release date'] = pd.to_datetime(dfjunto['Release date'])
# Filtrar precios distintos de 0.00
dfjunto_precio = dfjunto[dfjunto['Price'] != 0.00]
# Agrupar los precios por año
yearly_prices = dfjunto_precio.groupby(dfjunto_precio['Release date'].dt.year)['Price'].mean().reset_index()
# Crear el gráfico
pincho = px.line(yearly_prices, x='Release date', y='Price', title='Precios promedio por año')
#GRÁFICO DE +100M por Juego y Fecha----------------------------------------------------
dfjunto_topmax = dfjunto[dfjunto["Owners_max"] >= 100000000.0]
dfjunto_topmax["Release date"] = pd.to_datetime(dfjunto_topmax["Release date"]).dt.strftime('%Y-%m')
cienm = px.bar(dfjunto_topmax, x="Game", y="Owners_max", color="Release date")

# Eliminar la leyenda
cienm.update_layout(
    showlegend=False,
    title="Juegos con más de 100M de jugadores y fecha",
    xaxis_title="Juego",
    yaxis_title="Jugadores máximos"
)
#------------------------------AQUI LOS GRAFICOS PARA ANALISIS CAMBIANTES---------------------------------------
def update_dataframe(df, publisher):
    if publisher == 'Todos':
        df_filtered = df
    else:
        df_filtered = df[df['Publisher(s)'] == publisher]
    return df_filtered
#GRAFICO DE JUEGOS DE MAS DE 50MILLONES BOLITAS---------------------------------------
# Filtrar los juegos con más de 50M de jugadores
df_50 = dfjunto[dfjunto["Owners_max"] >= 50000000.0]
# Eliminar los juegos sin fecha de lanzamiento
df_50["Release date"] = df_50["Release date"].replace("N/A", np.nan)
df_50 = df_50.dropna(subset=["Release date"])
# Convertir la fecha de lanzamiento a formato datetime y extraer el año
df_50["Release date"] = pd.to_datetime(df_50["Release date"])
df_50["Release date"] = df_50["Release date"].dt.strftime('%Y')
# Crear la gráfica de dispersión
cincuentam = px.scatter(df_50, x="Price", y="Game", color="Game", hover_name="Game",
                 hover_data=["Release date"],
                 size="Owners_max", size_max=20,
                 labels={"Game": "Juegos", "Price": "Precio"},
                 title="Lista de juegos de más de 50M de jugadores")
# Ajustar el diseño de la gráfica
cincuentam.update_layout(
    showlegend=False,
    height=1200,
    margin=dict(l=50, r=50, b=50, t=50, pad=4)
)
#GRAFICO DE +99.00$ Por fecha y jugadores-----------------------------------------------
df_filtered = dfjunto[dfjunto['Price'] >= 99.99]

# Creación de la figura
noventainueve = px.scatter(df_filtered, x="Price", y="Release date", size="Owners_max", 
                 color="Owners_max", hover_name="Game", log_x=True,
                 color_continuous_scale="Spectral")

# Títulos
noventainueve.update_layout(title="Juegos de más de 99.99$ por fecha y jugadores máximos",
                  xaxis_title="Precio", yaxis_title="Fecha", coloraxis_colorbar_title="Jugadores máximos")
#GRÁFICO DE DISTRIBUIDORA PRECIO MEDIO--------------------------------------------------------
dfjunto_precio = dfjunto[dfjunto['Price'] != 0.00]
# Obtener el número de juegos publicados por cada editor
publisher_counts = dfjunto_precio.groupby('Publisher(s)')['Game'].nunique().reset_index()
# Ordenar los editores por cantidad de juegos publicados y obtener los primeros 15
top_publishers = publisher_counts.sort_values('Game', ascending=False).head(15)['Publisher(s)']
# Filtrar los datos para los primeros 15 editores
top_publisher_prices = dfjunto_precio[dfjunto_precio['Publisher(s)'].isin(top_publishers)]
# Calcular el precio promedio por editor
publisher_prices = top_publisher_prices.groupby('Publisher(s)')['Price'].mean().reset_index()
# Crear el gráfico
distrimedio = px.bar(publisher_prices, x='Publisher(s)', y='Price', title='Precio promedio de las primeras 15 distribuidoras con más juegos publicados')
# Cambiar el título del eje X
distrimedio.update_layout(xaxis_title='Distribuidora', yaxis_title='Precio')

#GRAFICO DOBLE DE DISTIBUIDORAS Y PRECIO MEDIO ----------------------------------------------------
# Obtener el número de juegos por editor para los primeros 15 editores
games_per_publisher = publisher_counts[publisher_counts['Publisher(s)'].isin(top_publishers)]
# Crear el gráfico
pmedio = go.Figure()
pmedio.add_trace(go.Bar(x=publisher_prices['Publisher(s)'],
                     y=publisher_prices['Price'],
                     name='Precio promedio',
                     marker_color='rgb(91,209,246)')) # Cambio de color
pmedio.add_trace(go.Bar(x=games_per_publisher['Publisher(s)'],
                     y=games_per_publisher['Game'],
                     name='Número de juegos',
                     marker_color='rgb(26, 118, 255)'))
pmedio.update_layout(title='Precio promedio y número de juegos de los primeros 15 distribuidoras con más juegos publicados',
                  xaxis_title='Distribuidora',
                  yaxis_title='Precio promedio / Número de juegos',
                  barmode='group')
#GRAFICO TOP 10 DISTRIBU POR MAX PLAYERS
top_publishers = dfjunto.groupby('Publisher(s)')['Owners_max'].sum().sort_values(ascending=False).head(15)

diezdis = go.Figure(go.Bar(
    y=top_publishers.index,
    x=top_publishers.values,
    orientation='h',
    marker=dict(
        color='rgb(91,209,246)',
        line=dict(color='rgba(91,209,246)', width=1)
    )
))
diezdis.update_layout(
    title='Top 10 distribuidoras por jugadores máximos',
    yaxis_title='Distribuidoras',
    xaxis_title='Jugadores máximos',
    font=dict(size=12),
    height=500,
    autosize=True
)
#GRÁFICO PARA Relación entre Desarrollador(es) y Distribuidor(es)
dfjunto['dev_pub_relation'] = dfjunto.apply(lambda row: 'igual' if row['Developer(s)'] == row['Publisher(s)'] else 'distinto', axis=1)
# Obtener los datos de la relación entre desarrollador(es) y publicador(es)
counts = dfjunto['dev_pub_relation'].value_counts().reset_index()
counts.columns = ['relacion', 'conteo']

# Definir colores personalizados
colors = ['rgb(91,209,246)', '#FF6961']

# Crear gráfico de pastel
distri = px.pie(counts, values='conteo', names='relacion', color='relacion', color_discrete_sequence=colors,
            hole=0.6, labels={'conteo': 'Porcentaje'})

# Configurar estilo y leyenda
distri.update_layout(
    title='Relación entre Desarrollador(es) y Distribuidor(es)',
    title_font_size=20,
    legend_title='Relación',
    legend_traceorder='reversed',

)
distri.update_traces(textposition='inside', textinfo='percent+label')



#COSAS PARA LA REGRESION DE PRECIO--------------------------------------------------------->

# Función para formatear los valores de Owners_max en miles o millones
def format_owners(value):
    if value >= 1000000:
        return f"{value / 1000000:.2f} millones"
    elif value >= 1000:
        return f"{value / 1000:.2f} miles"
    else:
        return f"{value:.2f}"
        
#CONCLUSIONES-----------------------------------------------------------------------------------
conclusiones = [
        "La industria del videojuego es una industria en constante crecimiento, con buenos números y un futuro prometedor.",
        "La popularidad de los juegos gratuitos, de acción y estrategia sugiere que estos géneros son más atractivos para la comunidad.",
        "Los juegos indies, aunque suelen ser más baratos o gratuitos, tienen menos usuarios que los juegos de grandes distribuidoras.",
        "La continuidad en secuelas de muchos juegos de aventura sugiere que este género es muy valorado por la comunidad de jugadores, y también para ser Juegos del Año.",
        "La categoría indie es la que cuenta con más juegos, seguida de acción y aventura.",
        "El 32% de los desarrolladores no publican sus propios juegos",
        "No parece haber una relación muy fuerte entre las categorías, las distribuidoras y el precio final del juego."
    ]

#SERIE TEMPORAL ---------------------------------------------------------------------------------
# Cargar el modelo ARIMA desde el archivo .pkl
    with open('data/modelo_arima.pkl', 'rb') as f:
        modelo_arima_fit = pickle.load(f)

    # Obtener la predicción para los próximos 5 años
    prediccion = modelo_arima_fit.predict(start=len(precio_anual), end=len(precio_anual)+1, typ='levels')

    # Crear un rango de fechas para la predicción (solo los próximos dos años)
    fechas_pred = pd.date_range(start=str(precio_anual.index[-1]), periods=2, freq='AS')

    # Obtener la predicción completa
    prediccion_completa = modelo_arima_fit.predict(start=precio_anual.index[0], end=precio_anual.index[-1], typ='levels')

    # Crear el gráfico con Plotly Express
    ari = px.line()
    ari.add_scatter(x=precio_anual.index, y=precio_anual, name='Datos')
    ari.add_scatter(x=fechas_pred, y=prediccion, name='Predicción a futuro', mode='lines+markers')
    ari.add_scatter(x=precio_anual.index, y=prediccion_completa, name='Predicción completa', mode='lines+markers')
    ari.update_layout(title='Precio promedio de los videojuegos por año', xaxis_title='Año', yaxis_title='Precio promedio')
