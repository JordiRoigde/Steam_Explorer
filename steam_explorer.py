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
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle
import requests
from bs4 import BeautifulSoup
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
import re

#------------------ CONFIGURACIÓN DE PÁGINA ----------------

st.set_page_config(page_title="STEAM GAMES | JORDI ROIG",
        layout="centered",
        page_icon="🎮",
        )
#Establecemos la imagen de fondo de la app
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
     <style>
        .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local("img/fondo_3_1.jpg")  

st.markdown(
    f"""
    <style>
    [data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
    }}
    [data-testid="stSidebar"]{{                 
    background-color: rgba(0, 0, 0, 0);
    border: 0.5px solid #ff4b4b;
        }}
    </style>
    """
 , unsafe_allow_html=True)




# categorias = ["Acción", "Aventura", "Deportes", "Early Access", "Estrategia", "Free to Play", "MMORPG", "RPG", "Simulación", "Indie"]
# categoria_seleccionada = st.selectbox("Selecciona una categoría", categorias)


#------------------ COMIENZA NUESTRA APP  ----------------------------------------------------------

#Imagen con efecto máscara de recorte usada como título.
st.image("img/banner_2.jpg")

# Creamos el Menú horizontal
menu = option_menu(
    menu_title=None,
    options=["Inicio", "Comparaciones", "Gráficos", "PowerBi", "Predicción de Precio", "Predicción de Jugadores","Conclusiones"],
    icons= ["house", "list", "upload", "clipboard-plus", "bell", "star","check"],
    default_index=0,
    orientation="horizontal"
)


#------------------ NAVEGANDO POR EL MENÚ  -----------------------------------------------------


###################### MENU INTRODUCCIÓN ################################
if menu =="Inicio":
    st.markdown("<h2 style='text-align: center;  background-color: #ff4b4b ; color: #FFFFFF;'>STEAM EXPLORER</h2>" ,unsafe_allow_html=True) #título

    #Comienza el Primer párrafo
    st.markdown(
    """
    <div style="border: 0px solid #ff4b4b; padding: 10px; background-color: rgba(254, 143, 143, 0); color: #FFFFFF; text-align: justify;">
    Steam es una plataforma de distribución de videojuegos en línea desarrollada por Valve Corporation. Fue lanzada en 2003 y actualmente cuenta con más de 120 millones de usuarios activos en todo el mundo.

    Steam permite a los usuarios comprar, descargar y jugar a videojuegos en sus ordenadores personales. Además, la plataforma ofrece una serie de herramientas y funciones para mejorar la experiencia de juego, como la capacidad de unirse a comunidades de jugadores, compartir capturas de pantalla y retransmitir en vivo las partidas a través de la plataforma Twitch.

    Una de las ventajas principales de Steam es la enorme cantidad de juegos disponibles en su catálogo. Desde los grandes éxitos hasta los títulos independientes, Steam ofrece una amplia variedad de opciones para todos los gustos y presupuestos. Además, la plataforma cuenta con frecuentes ofertas y promociones que permiten a los usuarios adquirir juegos a precios muy asequibles.
    </div>
    """, unsafe_allow_html=True)
    st.image("img/fondo_2.jpg")  #imagen Proba1
    st.write("<div style='text-align: right; font-size: small'>Imagen obtenida de www.hobbyconsolas.com</div>", unsafe_allow_html=True)
    st.write("")
    st.write("")

    #Título primer párrafo
    st.markdown("<h2 style='text-align: center;  background-color: #ff4b4b ; color: #FFFFFF;'>VIDEOJUEGOS Y LA INDUSTRIA</h2>" ,unsafe_allow_html=True)
    conc1 = 'https://www.itreseller.es/en-cifras/2022/08/el-sector-de-los-videojuegos-mueve-1795-millones-de-euros-en-espana'
    response = requests.get(conc1)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('title').text
    st.markdown(f'## [{title}]({conc1})')
    #DOS SCRAPP
    conc2 = 'https://vandal.elespanol.com/noticia/1350761043/estas-son-las-companias-de-videojuegos-que-mas-dinero-ingresaron-en-2022/'
    response = requests.get(conc2)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('title').text
    image_url = soup.find('meta', property='og:image')['content']
    st.markdown(f'## [{title}]({conc2})')
    st.image(image_url)
    #TRES SCRAPP
    conc3 = 'https://www.13.cl/esports/articulos/videojuegos-ya-hacen-mas-dinero-que-las-peliculas-y-los-deportes-combinados'
    response = requests.get(conc3)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('h2').text
    article_url = soup.find('meta', property='og:url')['content']
    image_url = soup.find('meta', property='og:image')['content']
    st.markdown(f'## [{title}]({article_url})')
    st.image(image_url)

    
    st.markdown(
    """
    <div style="border: 0px solid #ff4b4b; padding: 10px; background-color: rgba(254, 143, 143, 0); color: #FFFFFF; text-align: justify;">
    Los videojuegos se encuentran en constante crecimiento y han pasado de ser una simple forma de entretenimiento a una industria multimillonaria que abarca a personas de todas las edades y géneros. La evolución de los videojuegos ha sido tal que se han convertido en una parte importante de la cultura popular en todo el mundo.

    Cada vez más personas juegan a videojuegos y esta actividad es vista como algo positivo, ya que puede mejorar habilidades como la coordinación, la memoria y la resolución de problemas. Además, los videojuegos pueden ser una herramienta educativa y terapéutica, y son una forma de escapar de la rutina diaria.

    La industria de los videojuegos genera mucho dinero y es cada vez más grande, tanto que supera a la industria del cine y de los deportes combinados. Los eventos relacionados con los videojuegos, como torneos y convenciones, atraen a una gran cantidad de personas y han generado una economía alrededor de los videojuegos. Empresas y marcas han visto el potencial de los videojuegos y han invertido en patrocinios y publicidad en el sector.
    </div>
    """, unsafe_allow_html=True)

    #Línea separatoria
    st.markdown("""<hr style="height:1px;background-color: #ff4b4b; align:left" /> """, unsafe_allow_html=True)

    #Título segundo párrafo
    st.markdown("<h2 style='text-align: center;  background-color: #ff4b4b ; color: #FFFFFF;'>PRIMER VIDEOJUEGO</h2>" ,unsafe_allow_html=True) #título
    st.write("")
    #Segundo párrafo
    # Hacemos la solicitud GET a la página de Wikipedia que deseamos extraer
    
    url = "https://es.wikipedia.org/wiki/Primer_videojuego"
    response = requests.get(url)

    # Parseamos el contenido HTML utilizando BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Buscamos los mini-títulos utilizando el atributo de clase 'mw-headline'
    mini_titulos = soup.find_all('span', {'class': 'mw-headline'})

    # jugamos con los mini títulos
    mini_titulos_list = []
    for mini_titulo in mini_titulos:
        # Verificamos si el mini-título comienza con un número
        if mini_titulo.text[0].isdigit():
            # Agregamos el mini-título a la lista si cumple los criterios
            mini_titulos_list.append(mini_titulo.text)
            # Detenemos el proceso si encontramos "1972: Pong"
            if "1972: Pong" in mini_titulo.text:
                break

    # Mostramos los mini-títulos en la aplicación de Streamlit
    st.markdown("<h3 style='text-align: justify;'>Hay numerosos debates acerca de quién creó el primer videojuego, dependiendo la respuesta en gran medida de la definición de videojuego. La evolución de los videojuegos presenta una maraña entre varias industrias, incluyendo la científica, la informática, la industria arcade, y la electrónica de consumo.</h3>", unsafe_allow_html=True)

    st.write(f"[Los primeros juegos de la página de Wikipedia]({url})", target='_blank')


    for mini_titulo in mini_titulos_list:
        st.write(mini_titulo)




    #SLIDER INTRO

    mi_sidebar= False
    if(st.button("Primer  videojuego 🎮" )):
        mi_sidebar=True
        if mi_sidebar:
            
            with st.sidebar:
                st.markdown("""
                        <style>
                        sidebar.sidebar-content {
                            background-color: #FFFFFF;
                            }
                        </style>
                    """, unsafe_allow_html=True)
                st.sidebar.image('img/barra1.png')
                st.header(":red[Tennis for Two]")
                col1, col2 = st.columns(2)
                with col1:
                    st.write("Día presentado:")
                    st.markdown("<h2 style='text-align: center;  background-color: #ff4b4b ; color: #FFFFFF;'>18/10/1958</h2>" ,unsafe_allow_html=True) #título
                # col2.metric("Imágen Wikipedia", "v")
                with col2:
                    st.write("Imágen Wikipedia")
                    st.image("img/Tennis.jpg")


                # Fecha del juego
                fecha_juegos = datetime(1958, 10, 18)
                now = datetime.now()                      # Gracias a datetime va haciendo la operación siempre con la fecha actual.
                tiempo_transcurrido = relativedelta(now, fecha_juegos)
                
                #Columnas representadas en el sidebar del tiempo transcurrido.
                st.header(":red[Tiempo desde que se estrenó Tennis for Two:]")
                st.write("Años: ", tiempo_transcurrido.years)
                st.write("Meses: ", tiempo_transcurrido.months)
                st.write("Días: ", tiempo_transcurrido.days)
                st.write("Horas: ", tiempo_transcurrido.hours)
                st.write("Minutos: ", tiempo_transcurrido.minutes)
                st.write("Segundos: ", tiempo_transcurrido.seconds)
    
        if st.button("Ocultar videojuego 🎮"):
                    mi_sidebar=False



##################################    MENÚ COMPARACIONES    ##################################


if menu == "Comparaciones":
    st.markdown("<h2 style='text-align: center;  background-color: #ff4b4b ; color: #FFFFFF;'>Comparaciones</h2>" ,unsafe_allow_html=True)
    
    # Creamos el Menú vertical para las categorías
    opciones = ["Acción", "Aventura", "Deportes", "EarlyAcces", "Estrategia", "Free", "MMO", "RPG", "Simulacion", "Indie"]
    categoria = option_menu(
        "Selecciona una categoría:",
        opciones,
        default_index=0
    )    
    st.sidebar.image('img/barra2.png')
    # Agregamos un sidebar para filtrar el DataFrame por precio
    st.sidebar.header('Filtrar por precio')
    min_value, max_value = st.sidebar.slider(
        'Selecciona un rango de precio:',
        0.0, 100.0, (0.0, 100.0)
    )
    
    # Agregamos un sidebar para filtrar el DataFrame por Owners_max_text
    st.sidebar.header('Filtrar por usuarios máximos')
    owners_options = ["Sin filtro", "500.0M", "100.0M", "50.0M", "20.0M", "10.0M", "2.0M", "1.0M", "500.0K", "200.0K", "100.0K", "50.0K", "20.0K", "0.00"]
    owners = st.sidebar.selectbox(
        "Selecciona una opción de usuarios máximos:",
        owners_options,
        index=0
    )
    
    # Obtener el DataFrame correspondiente a la categoría seleccionada
    df = globals()[categoria.lower()]  
    
    # Aplicar el filtro por precio
    df = df[(df['Price'] >= min_value) & (df['Price'] <= max_value)]
        
    # Aplicar el filtro por Owners_max_text si no se seleccionó la opción "Sin filtro"
    if owners != "Sin filtro":
        df = df[df['Owners_max_text'] == owners]
        
    # Convertir la columna "Release date" a datetime
    df['Release date'] = pd.to_datetime(df['Release date'])
    
    # Agregamos un sidebar para filtrar el DataFrame por Publisher
    st.sidebar.header('Filtrar por distribuidor')
    publishers = ['Todos', 'Electronic Arts', 'Ubisoft', 'Activision', 'Bethesda Softworks', 'Xbox Game Studios', 'Square Enix', 'SEGA', 'Capcom', 'Amazon Games', 'Valve']
    publisher = st.sidebar.radio("Selecciona un distribuidor:", publishers, index=0)

    # Filtramos el DataFrame por el Publisher seleccionado, a menos que se seleccione "Todos"
    if publisher == 'Todos':
        df  # creamos una copia del DataFrame original
    else:
        df = df[df['Publisher(s)'] == publisher]  # filtramos el DataFrame original y creamos una copia del resultado
        # Mostramos el DataFrame filtrado
        container = st.empty()
        container.markdown("<style> .css-1v3fvcr {text-align: center !important;} </style>", unsafe_allow_html=True)
        container.dataframe(df)
     
    # Calcular la media de la columna "Price" para el DataFrame filtrado y mostrar el resultado
    mean_price = round(df["Price"].mean(), 2)
    st.write(f"<p style='text-align: center; font-size: 24px; font-weight: bold;'>El precio medio de tu selección {categoria} es: {mean_price}</p>", unsafe_allow_html=True)
# Calcular la media de la columna "Owners_max" para el DataFrame filtrado y mostrar el resultado
    mean_owners = round(df["Owners_max"].mean(), 2)
    st.write(f"<p style='text-align: center; font-size: 24px; font-weight: bold;'>El número medio usuarios de tu selección {categoria} es: {format_owners(mean_owners)}</p>", unsafe_allow_html=True)
    # Crear el gráfico de barras verticales
    df_top15 = df.nlargest(15, "Release date")
    fig = go.Figure(go.Bar(
        x=df_top15["Game"],
        y=df_top15["Release date"],
        text=df_top15["Price"],
        hovertemplate=
            "<b>%{x}</b><br>" +
            "Fecha de lanzamiento: %{y}<br>" +
            "Precio: %{text}<br>",
        orientation="v"
    ))

    # Personalizar el gráfico
    fig.update_layout(
        title=f"Los 15 juegos más nuevos de la categoría {categoria}",
        xaxis_title="Juego",
        yaxis_title="Fecha de lanzamiento",
        height=600
    )
    st.plotly_chart(fig)
    #GRAFICO PIE
    # Crear un DataFrame con los tres juegos más caros
    df_top3 = df.nlargest(3, "Price")[["Game", "Price"]]

    # Crear el gráfico pie
    fig = px.pie(df_top3, values="Price", names="Game", title=f"Los 3 juegos más caros de tu filtro y de la categoría {categoria}")
    st.plotly_chart(fig)
######################### GRÁFICOS ################################
elif menu == "Gráficos":
    st.markdown("<h2 style='text-align: center; background-color: #ff4b4b; color: #FFFFFF;'>Análisis</h2>", unsafe_allow_html=True)
    # Aquí puedes agregar el código para el análisis de los datos

    #GRAFICO DE PINCHOS PRECIO MEDIO - AÑO
    # Cargar el modelo ARIMA desde el archivo .pkl
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
    fig = px.line()
    fig.add_scatter(x=precio_anual.index, y=precio_anual, name='Datos')
    fig.add_scatter(x=fechas_pred, y=prediccion, name='Predicción a futuro', mode='lines+markers')
    fig.add_scatter(x=precio_anual.index, y=prediccion_completa, name='Predicción completa', mode='lines+markers')
    fig.update_layout(title='Precio promedio de los videojuegos por año', xaxis_title='Año', yaxis_title='Precio promedio')
    st.plotly_chart(fig)
#Serie temmporal en meses
    st.plotly_chart(meses)    

    #GRAFICO DE +99.00$ Por fecha y jugadores
    st.plotly_chart(noventainueve, use_container_width=True)
    #GRAFICO DE 100M
    st.plotly_chart(cienm)
    #GRAFICO 50M
    st.plotly_chart(cincuentam, use_column_width=True)
    # Mostrar el gráfico distri-desa
    st.plotly_chart(distri, use_container_width=True)
    #GRAFICO DISTRIBUIDORA PRECIOMEDIO
    st.plotly_chart(distrimedio)
    #GRAFICO DOBLE DISTRIBUIDORA PRECIO MEDIO Y JUEGOS
    st.plotly_chart(pmedio)
    # TOP10DISTRIBUIDORAS PLAYERS MAX
    st.plotly_chart(diezdis, use_column_width=True)
        
######################### POWERBI ################################

if menu == "PowerBi":
    st.markdown("<h2 style='text-align: center; background-color: #ff4b4b; color: #FFFFFF;'>Panel de PowerBi</h2>", unsafe_allow_html=True)
    st.markdown(
        f'<div style="max-width:1024px"><iframe title="buscapowerbi" width="100%" height="500" src="https://app.powerbi.com/view?r=eyJrIjoiYTI5NDI1MGUtNjhjYS00ODI3LWI1ZWYtZjhmZWE4OWU4ZDNlIiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9" frameborder="0" allowFullScreen="true"></iframe></div>',
        unsafe_allow_html=True,
    )


######################### REGRESIÓN ################################

if menu =="Predicción de Precio":
    st.markdown("<h2 style='text-align: center;  background-color: #ff4b4b ; color: #FFFFFF;'>Regresión de Precio</h2>" ,unsafe_allow_html=True) #título
    st.sidebar.image('img/barra3.png')
    # Definir los controles del sidebar
    
    st.sidebar.header('Parámetros de entrada')
    developer = st.sidebar.selectbox('Desarrollador(es)', pyca_filtered['Developer(s)'].unique())
    owners_max = st.sidebar.selectbox('Número máximo de jugadores', pyca_filtered['Owners_max'].unique())
    acción = st.sidebar.selectbox('Acción', ['No', 'Sí'])
    aventura = st.sidebar.selectbox('Aventura', ['No', 'Sí'])
    deportes = st.sidebar.selectbox('Deportes', ['No', 'Sí'])
    early = st.sidebar.selectbox('Early Access', ['No', 'Sí'])
    estrategia = st.sidebar.selectbox('Estrategia', ['No', 'Sí'])
    mmo = st.sidebar.selectbox('MMORPG', ['No', 'Sí'])
    rpg = st.sidebar.selectbox('RPG', ['No', 'Sí'])
    simulacion = st.sidebar.selectbox('Simulación', ['No', 'Sí'])
    indie = st.sidebar.selectbox('Indie', ['No', 'Sí'])
    release_year = st.sidebar.text_input('Año de lanzamiento', '2022')
    # Validar año de lanzamiento
    valid_year = re.match(r'^\d{4}$', release_year)
    if not valid_year:
        st.error('Por favor, introduzca un año válido de 4 dígitos.')
        st.stop()
    

    # Convertir los valores de entrada en un formato adecuado para la predicción
    accion = 1 if acción == 'Sí' else 0
    aventura = 1 if aventura == 'Sí' else 0
    deportes = 1 if deportes == 'Sí' else 0
    early = 1 if early == 'Sí' else 0
    estrategia = 1 if estrategia == 'Sí' else 0
    mmorpg = 1 if mmo == 'Sí' else 0
    rpg = 1 if rpg == 'Sí' else 0
    simulacion = 1 if simulacion == 'Sí' else 0
    indie = 1 if indie == 'Sí' else 0

    # Obtener el código del desarrollador
    developer_col = 'dev_code'
    dev_dict = {k:v for v,k in enumerate(pyca_filtered['Developer(s)'].unique())}
    pyca_filtered[developer_col] = pyca_filtered['Developer(s)'].replace(dev_dict)
    developer_coded = dev_dict[developer]

    # Cargar el modelo desde el archivo
    with open('data/precio_pred.pkl', 'rb') as archivo:
        model = pickle.load(archivo)
    # Convertir los valores de entrada en un formato adecuado para la predicción
    X_new = [[accion, aventura, deportes, early, estrategia, mmorpg, rpg, simulacion, indie, release_year, owners_max, developer_coded]]

    # Hacer predicciones en los nuevos datos
    y_pred = model.predict(X_new)
    # Formatear el precio como una cadena de texto con separador de miles y dos decimales
    precio_formateado = '${:,.2f}'.format(y_pred[0])
    # Crear contenedor con el precio predicho
    precio_container = st.container()
    with precio_container:

        # Contenido del contenedor
        precio_formateado = f'$ {round(y_pred[0], 2):,}'
        st.markdown(
            f"""
            <div style="
                border: 2px solid #ffffff;
                background-color: transparent;
                border-radius: 10px;
                padding: 20px;
                text-align: center;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
                margin-top: 20px;
                margin-left: auto;
                margin-right: auto;
                width: 60%;
            ">
                <div style="font-size: 30px; font-weight: 700; margin-bottom: 20px; color: #ffffff;">Tu juego según tus parámetros de entrada debería costar:</div>
                <div style="font-size: 80px; font-weight: 700; color: #ff4b4b;">{precio_formateado}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
######################### CLASIFICACIÓN ################################
if menu =="Predicción de Jugadores":
    st.markdown("<h2 style='text-align: center;  background-color: #ff4b4b ; color: #FFFFFF;'>Clasificación de Jugadores</h2>" ,unsafe_allow_html=True) #título
    st.sidebar.image('img/barra4.png')
    # Crear la barra lateral
    st.sidebar.header('Introduzca los valores de entrada')
    developer = st.sidebar.selectbox('Desarrollador(es)', pyca_filtered['Developer(s)'].unique())
    release_year = st.sidebar.slider('Año de lanzamiento', 2000, 2022, 2015)
    price = st.sidebar.slider('Precio', 0, 100, 50)
    accion = st.sidebar.selectbox('Acción', ['No', 'Sí'])
    aventura = st.sidebar.selectbox('Aventura', ['No', 'Sí'])
    deportes = st.sidebar.selectbox('Deportes', ['No', 'Sí'])
    early = st.sidebar.selectbox('Early Access', ['No', 'Sí'])
    estrategia = st.sidebar.selectbox('Estrategia', ['No', 'Sí'])
    mmorpg = st.sidebar.selectbox('MMORPG', ['No', 'Sí'])
    rpg = st.sidebar.selectbox('RPG', ['No', 'Sí'])
    simulacion = st.sidebar.selectbox('Simulación', ['No', 'Sí'])
    indie = st.sidebar.selectbox('Indie', ['No', 'Sí'])

    # Convertir los valores de entrada en un formato adecuado para la predicción
    accion = 1 if accion == 'Sí' else 0
    aventura = 1 if aventura == 'Sí' else 0
    deportes = 1 if deportes == 'Sí' else 0
    early = 1 if early == 'Sí' else 0
    estrategia = 1 if estrategia == 'Sí' else 0
    mmorpg = 1 if mmorpg == 'Sí' else 0
    rpg = 1 if rpg == 'Sí' else 0
    simulacion = 1 if simulacion == 'Sí' else 0
    indie = 1 if indie == 'Sí' else 0
    
    # Obtener el código del desarrollador
    developer_col = 'dev_code'
    dev_dict = {k:v for v,k in enumerate(pyca_filtered['Developer(s)'].unique())}
    pyca_filtered[developer_col] = pyca_filtered['Developer(s)'].replace(dev_dict)
    developer_coded = dev_dict[developer]
    with open('data/rf_model.pkl', 'rb') as f:
        rf_model = pickle.load(f)
    # Realizar la predicción y mostrar el resultado en tiempo real
    sample = [accion, aventura, deportes, early, estrategia, mmorpg, rpg, simulacion, indie, release_year, price, developer_coded]
    predicted_owners = rf_model.predict([sample])
    predicted_owners_str = predicted_owners[0].replace('\xa0', ' ')
    
    # Crear contenedor con el número estimado de jugadores
    num_jugadores_container = st.container()
    with num_jugadores_container:
        # Formatear el texto con comas y añadir estilo CSS
        styled_text = f"<div style='font-size: 36px; font-weight: bold; color: #ff4b4b;'>{predicted_owners_str}</div>"
        
        # Mostrar texto en el contenedor
        st.markdown(
            f"""
            <div style="
                border: 2px solid #ffffff;
                background-color: transparent;
                border-radius: 10px;
                padding: 20px;
                text-align: center;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
                margin-top: 20px;
                margin-left: auto;
                margin-right: auto;
                width: 60%;
            ">
                <div style="font-size: 30px; font-weight: 700; margin-bottom: 20px; color: #ffffff;">El número estimado de jugadores es:</div>
                {styled_text}
            </div>
            """,
            unsafe_allow_html=True
        )
        
######################### CONCLUSIONES Y DESPEDIDA ################################
if menu =="Conclusiones":
    st.markdown("<h2 style='text-align: center;  background-color: #ff4b4b ; color: #FFFFFF;'>CONCLUSIONES</h2>" ,unsafe_allow_html=True) #título



    st.markdown("")
    st.markdown("")
    for i, c in enumerate(conclusiones):
        st.markdown(f"<h3 style='margin-bottom: 10px;'><span style='background-color: #ff4b4b; color: #FFFFFF; padding: 5px; border-radius: 5px;'>{i+1}</span><span style='margin-left: 10px;'></span><span style='text-align: justify;'>{c}</span></h3>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
#BARRA SEPARATORIA Y LUGARES DE PNGS
    st.markdown("""<hr style="height:1px;background-color: #ff4b4b; align:left" /> """, unsafe_allow_html=True)
    

    with st.container():
        st.write("<div style='text-align: center; color: white;'>Los PNG'S de esta presentación són de: <a href='https://www.freepng.es' target='_blank'>www.freepng.es</a></div>", unsafe_allow_html=True)
        st.write("<div style='text-align: center; color: white;'>Herramienta de creación de nombres e imágenes: <a href='https://rezuaq.be/new-area/image-creator' target='_blank'>https://rezuaq.be/new-area/image-creator</a></div>", unsafe_allow_html=True)
    st.markdown("""<hr style="height:1px;background-color: #ff4b4b; align:left" /> """, unsafe_allow_html=True)

    # mostrar la imagen "game_over"
    barra_conc = st.image('img/barra_conc.png')
    game_over_img = st.image('img/game_over.png')

    # agregar botón "Revivir?"
    if st.button('¿Revivir?'):
        # esconder la imagen "game_over"
        barra_conc.empty()
        game_over_img.empty()
        # mostrar la imagen "gracias"
        st.image('img/barra1.png')
        st.image('img/gracias.png')
        
        # # mostrar mensaje de agradecimiento
        # st.write("Volver al Inicio")
        
        # # agregar botón "Volver a jugar"
        # if st.button('Volver a jugar'):
        #     st.experimental_rerun()
