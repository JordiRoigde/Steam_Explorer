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


#------------------ COSAS QUE PODEMOS USAR EN TODA NUESTRA APP ----------------
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
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local("Imágenes/streamlit_background_4.png")  


# Con lo primero quito la barra de arriba y la hago transparerente
# Con lo segundo hago transparente el sidebar y le añado un pequeño borde.
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


# Leemos el Dataset
df = pd.read_csv("accion.csv")

#------------------ COMIENZA NUESTRA APP  ----------------------------------------------------------

#Imagen con efecto máscara de recorte usada como título.
st.image("img/banner.png")

# Creamos el Menú horizontal
menu = option_menu(

    menu_title=None,
    options=["Introducción", "Dataframe", "Análisis", "Modelo de predicción de supervivencia"],
    icons= ["house", "list", "clipboard-plus"],
    default_index=0,
    orientation="horizontal"
)


#------------------ NAVEGANDO POR EL MENÚ  -----------------------------------------------------


###################### MENU INTRODUCCIÓN ################################
if menu =="Introducción":
    st.markdown("<h2 style='text-align: center;  background-color: #ff4b4b ; color: #FFFFFF;'>Introducción</h2>" ,unsafe_allow_html=True) #título

    #Comienza el párrafo introductorio
    st.markdown(
                             """
    <div style="border: 0px solid #ff4b4b; padding: 10px; background-color: rgba(254, 143, 143, 0); color: #FFFFFF;">
    STEAM STEAM STEAMSTEAM STEAM STEAMSTEAM STEAM STEAMSTEAM STEAM STEAMSTEAM STEAM STEAMSTEAM STEAM STEAMSTEAM STEAM STEAMSTEAM STEAM STEAM
    
    STEAM STEAM STEAMSTEAM STEAM STEAMSTEAM STEAM STEAMSTEAM STEAM STEAMSTEAM STEAM STEAMSTEAM STEAM STEAMSTEAM STEAM STEAMSTEAM STEAM STEAM
    
    """, unsafe_allow_html=True)
    st.image("img\proba1.jpg")  #imagen Proba1


    #Título primer párrafo
    st.markdown("<h3 style='text-align: left; color: #FFFFFF;'>SEGUNDA INTRODUCCIÓN BRO</h3>" ,unsafe_allow_html=True)

    st.markdown(
                             """
    <div style="border: 0px solid #ff4b4b; padding: 8px; background-color: rgba(254, 143, 143, 0); color: #FFFFFF;">   
    STEAMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM <br>
    <br>
    Steam2steam2steam2!!!!!!!!!!!!!!!!!!!!!!!!!!111111111111111111111111111111111111111111111111111111111111111
    
    """, unsafe_allow_html=True)    

    #Línea separatoria
    st.markdown("""<hr style="height:1px;background-color: #ff4b4b; align:left" /> """, unsafe_allow_html=True)

    #Título segundo párrafo
    st.markdown("<h3 style='text-align: left; color: #FFFFFF;'>INTRO TRES</h3>" ,unsafe_allow_html=True)

    #Segundo párrafo
    st.markdown(
                             """
    STEAMMMMMMMMMMMMMMM333333   
    STEAMMMMMMMMMMMMMMM333333   
    STEAMMMMMMMMMMMMMMM333333   
    STEAMMMMMMMMMMMMMMM333333   
    STEAMMMMMMMMMMMMMMM333333   
    
    <br>
    <br>
    <br>
    <br>
                            </div>
                             """, unsafe_allow_html=True)




    #Trabajamos aquí el sidebar del menú introducción

    mi_sidebar= False
    if(st.button("¿INFO DE STEAM? 🎮" )):
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

                st.header(":red[ESTO SON JUEGOS TETE]")
                col1, col2 = st.columns(2)
                col1.metric("Infouno", "juegouno")
                col2.metric("Infodos", "juegodos")

            

                # Aquí queremos mostrar fechas de juegos??????????
                fecha_juegos = datetime(1958, 10, 18)
                now = datetime.now()                      # Gracias a datetime va haciendo la operación siempre con la fecha actual.
                tiempo_transcurrido = relativedelta(now, fecha_juegos)
                
                #Columnas representadas en el sidebar del tiempo transcurrido.
                st.header(":red[Tiempo des de que se estrenó este juego:]")
                st.write("Años: ", tiempo_transcurrido.years)
                st.write("Meses: ", tiempo_transcurrido.months)
                st.write("Días: ", tiempo_transcurrido.days)
                st.write("Horas: ", tiempo_transcurrido.hours)
                st.write("Minutos: ", tiempo_transcurrido.minutes)
                st.write("Segundos: ", tiempo_transcurrido.seconds)
    
        if st.button("Ocultar juego"):
                    mi_sidebar=False



##################################    MENÚ DATAFRAME    ##################################

if menu =="Dataframe":
    st.markdown("<h2 style='text-align: center;  background-color: #ff4b4b ; color: #FFFFFF;'>Dataframe</h2>" ,unsafe_allow_html=True)

    # Creación de filtros en el sidebar

    st.sidebar.header("Filtrado Dataframe:")
    seleccion_sexo = st.sidebar.multiselect("Género:", options=df["Sex"].unique(), default=df["Sex"].unique())
    seleccion_salvacion = st.sidebar.multiselect("Superviviente:", options=df["Survived"].unique(), default=df["Survived"].unique())
    seleccion_embarked = st.sidebar.multiselect("Embarcado:", options=df["Embarked"].unique(), default=df["Embarked"].unique())
    seleccion_clase = st.sidebar.multiselect("Clase:", options=df["Pclass"].unique(), default=df["Pclass"].unique())

    edad = df["Age"].unique().tolist()
    seleccion_edad = st.sidebar.slider("Edad:", min_value= 0 , max_value= 80, value = (0, 80))

    precio_billete = df["Fare"].unique().tolist()
    seleccion_precio = st.sidebar.slider("Precio billete:", min_value =0, max_value = 513, value = (0, 513))

    # DF con los filtros aplicados
    seleccion_df = df.query("Sex == @seleccion_sexo & Survived == @seleccion_salvacion & Embarked == @seleccion_embarked & Pclass == @seleccion_clase & Age >= @seleccion_edad[0] & Age <= @seleccion_edad[1] & Fare >= @seleccion_precio[0] & Fare <= @seleccion_precio[1]")
    st.dataframe(seleccion_df)

    # Indicamos después de cada filtrado los resultados obtenidos.
    resultado_df=seleccion_df.shape[0]
    st.markdown(f"*Resultados obtenidos: **{resultado_df}** *" )

    
    st.markdown(        # Esto es para dejar espacio entre la tabla y lo siguiente
    """
    <br>
    <br>
    """, unsafe_allow_html=True)

    # Aquí se crea la leyenda y descripción de los campos del dataset
    st.markdown(
        """
        <h4 style='text-align: center; color: #ff4b4b;'>Descripción de los campos</h4>
   
    <b> PassengerId --> </b> &nbsp;&nbsp; Identificador del pasajero<br>
    <b>Survived --> </b> &nbsp;&nbsp;       Indica si el pasajero sobrevivió<br>
    <b>Pclass --> </b> &nbsp;&nbsp;         Indica la clase de pasajero primera, segunda o tercera<br>
    <b>Name --> </b> &nbsp;&nbsp;           Nombre completo del pasajero<br>
    <b>Sex --> </b> &nbsp;&nbsp;            Género del pasajero <br>
    <b>Age --> </b> &nbsp;&nbsp;            Edad del pasajero<br>
    <b>SibSp --> </b> &nbsp;&nbsp;          Cantidad de hermanas/os o esposas/os a bordo<br>
    <b>Parch --> </b> &nbsp;&nbsp;          Cantidad de padres o hijos a bordo<br>
    <b>Ticket --> </b> &nbsp;&nbsp;          Número de ticket<br>
    <b>Fate --> </b> &nbsp;&nbsp;           Precio del billete<br>
    <b>Cabin --> </b> &nbsp;&nbsp;          Cabina en la cual se encuentra alojado el pasajero (columna eliminada) <br>
    <b>Embarked --> </b> &nbsp;&nbsp;       Puerto de embarque<br>
    <b>rango_edad --> </b> &nbsp;&nbsp;     Indica dentro de qué rango de edad se encuentran los pasajeros<br>
    <b>viajando_solos --> </b> &nbsp;&nbsp; Será un 1 si el pasajero viaja solo o un 0 si viaja acompañado. Estos valores han sido extraidos de la columna SibSp y Parch <br>
    """,unsafe_allow_html=True)




################################## MENÚ ANÁLISIS ##################################

######  COMENZAMOS CON LAS GRÁFICAS   ##### 

if menu =="Análisis":
    # Título de la pestaña Análisis
    st.markdown("<h2 style='text-align: center; background-color: #ff4b4b ; color: #FFFFFF;'>Análisis exploratorio</h2>" ,unsafe_allow_html=True)

     # Usamos línea de separación
    st.markdown("""<hr style="height:2px;background-color: white;" /> """, unsafe_allow_html=True)


    #Título gráfica a la izquierda + imagen a la derecha
    st.markdown("<div style='display:flex;align-items:left;'>"
               "<h1 style='color:#ff4b4b;font-size:24px; webkit-text-stroke: 0.0px white'>Distribución de pasajeros por su género</h1>"
               "<figure>"
               "<img src='https://quo.eldiario.es/wp-content/uploads/2019/10/espanoles-en-el-titanic.jpg' style='width:200px;margin-left:40px;'>"
               "<figcaption style='font-size:8px; text-align: right'>elcorreo.com</figcaption>"
                    "</figure>"
            "</div>", unsafe_allow_html=True)


    grafica1= False
    if st.button("Mostrar análisis de la gráfica 1"):
        grafica1=True

        if grafica1:

            fig_sex = px.pie(df, names = "Sex", color = "Sex", hole=.2, color_discrete_map = {"Male": 'red', "Female": 'cyan'})
            fig_sex.update_traces(text = df["Sex"].value_counts(), textinfo = "label+percent+text")
            fig_sex.update_layout(legend_title="Género",)
            #fig_sex.update_layout(title_text = "Distribución por género", title_x = 0.5)
            
            st.plotly_chart(fig_sex)

            # Análisis gráfica 1
            st.markdown(
                             """
                             <div style="border: 0px solid #ff4b4b; padding: 10px; background-color: rgba(255, 75, 75, 0.2); color: #FFFFFF;">
                                        <b> Comentario:</b><br>
                                        A bordo del Titanic viajaban más pasajeros hombres que mujeres, concretamente el 64.8%. 
                            </div>
                             """, unsafe_allow_html=True)

        if st.button("Ocultar análisis de la gráfica 1"):
                    grafica1=False

    # Usamos línea de separación
    st.markdown("""<hr style="height:2px;background-color: white;" /> """, unsafe_allow_html=True)

           
    #------------------------------------------------------------------------

    # Gráfica 2
    #st.markdown(f'<h1 style="color:#ff4b4b;font-size:24px; webkit-text-stroke: 0.5px black">{"Distribución de pasajeros por su clase"}</h1>', unsafe_allow_html=True)

    st.markdown("<div style='display:flex;align-items:left;'>"
                "<h1 style='color:#ff4b4b;font-size:24px; webkit-text-stroke: 0px black'>Distribución de pasajeros por su clase</h1>"
                "<figure>"
                "<img src='https://banderaroja.com.ve/wp-content/uploads/2017/03/titanic.jpg' style='width:230px;margin-left:40px;'>"
                "<figcaption style='font-size:8px; text-align: right'>banderaroja.com.ve</figcaption>"
                    "</figure>"
            "</div>", unsafe_allow_html=True)
    
    grafica2= False
    if st.button("Mostrar análisis de la gráfica 2"):
        grafica2=True

        if grafica2:


            ax = sns.countplot(x="Pclass", data=df, palette="pastel")
            plt.style.use("dark_background")
            style="darkgrid"
            ax.bar_label(ax.containers[0])
            ax.set_xlabel("Clase")
            ax.set_ylabel("Número de pasajeros")
            #ax.set_title("Distribución de pasajeros por su clase")
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()

            #Análisis gráfica 2
            st.markdown(
                             """
                             <div style="border: 0px solid #ff4b4b; padding: 10px; background-color: rgba(255, 75, 75, 0.2); color: #FFFFFF;">
                                        <b> Comentario:</b><br>
                                        La gran mayoría de los pasajeros a bordo del Titanic eran de clase baja.<br>
                                        La tercera clase tuvo 491 pasajeros, doblando a la primera y segunda clase juntas.
                            </div>
                             """, unsafe_allow_html=True)


        if st.button("Ocultar análisis de la gráfica 2"):
                    grafica2=False
     
    

    # Usamos línea de separación
    st.markdown("""<hr style="height:2px;background-color: white;" /> """, unsafe_allow_html=True)

    #------------------------------------------------------------------------

    # Gráfica 3
    #st.markdown(f'<h1 style="color:#ff4b4b;font-size:24px; webkit-text-stroke: 0.5px black">{"Distribución de pasajeros por su clase y género"}</h1>', unsafe_allow_html=True)
    st.markdown("<div style='display:flex;align-items:left;'>"
                "<h1 style='color:#ff4b4b;font-size:24px; webkit-text-stroke: 0px black'>Distribución de pasajeros por su clase y género</h1>"
                "<figure>"
                "<img src='https://1.bp.blogspot.com/-myC9Qq_0bDQ/Xz41ONAgS9I/AAAAAAAAJPo/iqTaMb2Yt7wx-GyOUe80e-6S25A6tlLegCLcBGAsYHQ/w1200-h630-p-k-no-nu/f3177-titanic-kate-beer.jpg' style='width:230px;margin-left:40px;'>"
                    "<figcaption style='font-size:8px; text-align: right'>eljardindellupulo.blogspot.com</figcaption>"
                    "</figure>"
            "</div>", unsafe_allow_html=True)

    grafica3= False
    if st.button("Mostrar análisis de la gráfica 3"):
        grafica3=True

        if grafica3:

            ax = sns.countplot(x="Pclass", data=df, palette="pastel", hue= "Sex")
            plt.style.use("dark_background")
            style="darkgrid"
            ax.bar_label(ax.containers[0])
            ax.bar_label(ax.containers[1])
            ax.set_xlabel("Clase")
            ax.set_ylabel("Número de pasajeros")
            #ax.set_title("Distribución de pasajeros por su clase y género")
            st.pyplot()

            #Análisis gráfica 3
            st.markdown(
                             """
                             <div style="border: 0px solid #ff4b4b; padding: 10px; background-color: rgba(255, 75, 75, 0.2); color: #FFFFFF;">
                                        <b> Comentario:</b><br>
                                        Aquí podemos ver el mismo gráfico que el anterior, pero mostrando la variable de género por separado.<br>
                                        Se sigue contemplando una diferencia muy grande de la cantidad de  pasajeros hombres de tercera clase respecto al resto. 
                            </div>
                             """, unsafe_allow_html=True)

        if st.button("Ocultar análisis de la gráfica 3"):
                    grafica3=False


   

    # Usamos línea de separación
    st.markdown("""<hr style="height:2px;background-color: white;" /> """, unsafe_allow_html=True)

    #------------------------------------------------------------------------

    # Gráfica 4
    #st.markdown(f'<h1 style="color:#ff4b4b;font-size:24px; webkit-text-stroke: 0.5px black">{"Información de las edades de los pasajeros"}</h1>', unsafe_allow_html=True)
    st.markdown("<div style='display:flex;align-items:left;'>"
                "<h1 style='color:#ff4b4b;font-size:24px; webkit-text-stroke: 0px black'>Información de las edades de los pasajeros</h1>"
                "<figure>"
                "<img src='https://elcorreoweb.es/documents/10157/0/675x448/0c2/675d400/none/10703/HUBW/image_content_17365074_20151026153705.jpg' style='width:230px;margin-left:40px;'>"
                "<figcaption style='font-size:8px; text-align: right'>elcorreoweb.es</figcaption>"
                    "</figure>"
            "</div>", unsafe_allow_html=True)

    grafica4= False
    if st.button("Mostrar análisis de la gráfica 4"):
        grafica4=True

        if grafica4:

            fig_age = px.histogram(df, x = "Age", nbins=15,text_auto=True,
            #title="Distribución de los pasajeros por edades",
            opacity=0.7,
            color_discrete_sequence=['indianred'],
            template="plotly_dark"
            )
            fig_age.update_layout(
            xaxis_title="Rangos de edad",
            yaxis_title="Frecuencia"
            )
            st.plotly_chart(fig_age)

            #Análisis gráfica 4
            st.markdown(
                             """
                             <div style="border: 0px solid #ff4b4b; padding: 10px; background-color: rgba(255, 75, 75, 0.2); color: #FFFFFF;">
                                        <b> Comentario:</b><br>
                                         Observando está gráfica podemos observar que entre 20 y 39 años se encuentran la  mayoría de los pasajeros. Sobre todo de 20 a 29 años.<br>
                                          La persona más mayor del Titanic tenía 80 años y la más pequeña apenas meses.
                            </div>
                             """, unsafe_allow_html=True)

        if st.button("Ocultar análisis de la gráfica 4"):
                        grafica4=False

    # Usamos línea de separación
    st.markdown("""<hr style="height:2px;background-color: white;" /> """, unsafe_allow_html=True)

    #------------------------------------------------------------------------

    #Gráfica 5
    #st.markdown(f'<h1 style="color:#ff4b4b;font-size:24px; webkit-text-stroke: 0.5px black">{"Distribución de los pasajeros según su edad y género"}</h1>', unsafe_allow_html=True)
    st.markdown("<div style='display:flex;align-items:left;'>"
                "<h1 style='color:#ff4b4b;font-size:24px; webkit-text-stroke: 0px black'>Distribución de los pasajeros según su edad y género</h1>"
                "<figure>"
                "<img src='https://k60.kn3.net/taringa/3/0/F/4/B/A/OjoLoco-Mix/E10.jpg' style='width:230px;margin-left:40px;'>"
                "<figcaption style='font-size:8px; text-align: right'>taringa.net</figcaption>"
                    "</figure>"
            "</div>", unsafe_allow_html=True)

    grafica5= False
    if st.button("Mostrar análisis de la gráfica 5"):
        grafica5=True

        if grafica5:

                fig_age2 = px.histogram(df, x = "Age", color= "Sex", nbins=15,text_auto=True,
                #title="Distribución de los pasajeros por edades y género",
                opacity=0.7,
                #color_discrete_sequence=['indianred'],
                template="plotly_dark"
                )
                fig_age2.update_layout(
                xaxis_title="Rangos de edad",
                yaxis_title="Frecuencia"
                )
                st.plotly_chart(fig_age2)
                

                #Análisis gráfica 5
                st.markdown(
                             """
                             <div style="border: 0px solid #ff4b4b; padding: 10px; background-color: rgba(255, 75, 75, 0.2); color: #FFFFFF;">
                                        <b> Comentario:</b><br>
                                         Mismo gráfico que el anterior añadiendo el factor de género. Destaca que no hay mayor
                                         número de mujeres en ningún rango de edad y que a partir de los 69 años solo hay hombres.
                            </div>
                             """, unsafe_allow_html=True)

        if st.button("Ocultar análisis de la gráfica 5"):
                            grafica5=False

    # Usamos línea de separación
    st.markdown("""<hr style="height:2px;background-color: white;" /> """, unsafe_allow_html=True)
  
    #------------------------------------------------------------------------

    # Gráfico 6
    #st.markdown(f'<h1 style="color:#ff4b4b;font-size:24px; webkit-text-stroke: 0.5px black">{"Distribución de los pasajeros según su embarque"}</h1>', unsafe_allow_html=True)
    st.markdown("<div style='display:flex;align-items:left;'>"
                "<h1 style='color:#ff4b4b;font-size:24px; webkit-text-stroke: 0px black'>Distribución de los pasajeros según su embarque</h1>"
                "<figure>"
                "<img src='https://s1.eestatic.com/2018/04/16/social/titanic-twitter-barcos_300233521_74164994_1706x960.jpg' style='width:230px;margin-left:40px;'>"
                "<figcaption style='font-size:8px; text-align: right'>elespanol.com</figcaption>"
                    "</figure>"
            "</div>", unsafe_allow_html=True)

    grafica6= False
    if st.button("Mostrar análisis de la gráfica 6"):
            grafica6=True

            if grafica6:

                fig_embarked = go.Figure(data=[go.Pie(labels=df["Embarked"], pull=[0.1, 0.1, 0.2])])
                #fig_embarked.update_layout(
                    # title=go.layout.Title(
                    # text="Distribución de los diferentes embarques", #<br><br><sup>S - Southampton<br>C - Cherbourg<br>Q - Queenstown </sup>",
                #     xref="paper",
                #     x=0
                # )
                # )
                st.plotly_chart(fig_embarked)


                #Análisis gráfica 6
                st.markdown(
                             """
                             <div style="border: 0px solid #ff4b4b; padding: 10px; background-color: rgba(255, 75, 75, 0.2); color: #FFFFFF;">
                                        <b> Comentario:</b><br>
                                         Podemos observar que la gran mayoría de pasajeros, un 72.5%, salió desde el puerto de Southampton.
                            </div>
                             """, unsafe_allow_html=True)

                if st.button("Ocultar análisis de la gráfica 6"):
                            grafica6=False

    # Usamos línea de separación
    st.markdown("""<hr style="height:2px;background-color: white;" /> """, unsafe_allow_html=True)
    
    #------------------------------------------------------------------------

    # Gráfica 7
    #st.markdown(f'<h1 style="color:#ff4b4b;font-size:24px; webkit-text-stroke: 0.5px black">{"Distribución de los pasajeros según el precio de su billete"}</h1>', unsafe_allow_html=True)
    st.markdown("<div style='display:flex;align-items:left;'>"
                "<h1 style='color:#ff4b4b;font-size:24px; webkit-text-stroke: 0px black'>Distribución de los pasajeros según el precio de su billete</h1>"
                "<figure>"
                "<img src='https://www.soy502.com/sites/default/files/2017/Jul/16/boleto.jpg' style='width:230px;margin-left:40px;'>"
                "<figcaption style='font-size:8px; text-align: right'>soy502.com</figcaption>"
                    "</figure>"
            "</div>", unsafe_allow_html=True)

    grafica7= False
    if st.button("Mostrar análisis de la gráfica 7"):
            grafica7=True

            if grafica7:


                fig_fare = px.scatter(df, x = "Fare",
                #title="Distribución de los pasajeros según el precio de su billete",
                opacity=1,
                color_discrete_sequence=['indianred'],
                template="plotly_dark"
                )
                fig_fare.update_layout(
                    xaxis_title="Precio del billete",
                    yaxis_title="Frecuencia"
                )

                st.plotly_chart(fig_fare)


                #Análisis gráfica 7
                st.markdown(
                             """
                             <div style="border: 0px solid #ff4b4b; padding: 10px; background-color: rgba(255, 75, 75, 0.2); color: #FFFFFF;">
                                        <b> Comentario:</b><br>
                                        En este gráfico scatter podemos observar la frecuencia de la obtención de billetes según su precio. <br>
                                        La gran mayoría de los billetes no superan los 35$ y los 3 billetes más caros se vendieron por 512.33$.
                            </div>
                             """, unsafe_allow_html=True)

            
            if st.button("Ocultar análisis de la gráfica 7"):
                                            grafica7=False

    # Usamos línea de separación
    #st.markdown("""<hr style="height:2px;background-color: white;" /> """, unsafe_allow_html=True)
    

    #------------------------------------------------------------------------

    #Análisis gráfica 8
    #st.markdown(f'<h1 style="color:#ff4b4b;font-size:24px; webkit-text-stroke: 0.5px black">{"Otra forma de ver la distribución del precio de los billetes"}</h1>', unsafe_allow_html=True)

    grafica8= False
    if st.button("Mostrar análisis de la gráfica 8"):
            grafica8=True

            if grafica8:

                fig_fare2 = px.histogram(df, x = "Fare", range_x=(0,550), nbins=15,
                title="Precio de los billetes",
                opacity=0.7,
                color_discrete_sequence=['indianred'],
                template="plotly_dark"
                )
                fig_fare2.update_layout(
                xaxis_title="Precio de los billetes",
                yaxis_title="Pasajeros que lo compraron"
                )

                st.plotly_chart(fig_fare2)


                #Análisis gráfica 8
                st.markdown(
                             """
                             <div style="border: 0px solid #ff4b4b; padding: 10px; background-color: rgba(255, 75, 75, 0.2); color: #FFFFFF;">
                                        <b> Comentario:</b><br>
                                        Este gráfico muestra la distribución de los precios de los billetes comprados por los pasajeros del Titanic.
                                        La mayoría de los pasajeros pagaron precios entre 0 y 100 dólares, con un pico en el rango entre 20 y 40 dólares.
                            </div>
                             """, unsafe_allow_html=True)

            if st.button("Ocultar análisis de la gráfica 8"):
                            grafica8=False

    # Usamos línea de separación
    st.markdown("""<hr style="height:2px;background-color: white;" /> """, unsafe_allow_html=True)
    
    #------------------------------------------------------------------------

    #Gráfica 9
    #st.markdown(f'<h1 style="color:#ff4b4b;font-size:24px; webkit-text-stroke: 0.5px black">{"Precio del billete, según la clase"}</h1>', unsafe_allow_html=True)
    st.markdown("<div style='display:flex;align-items:left;'>"
                "<h1 style='color:#ff4b4b;font-size:24px; webkit-text-stroke: 0px black'>Precio del billete, según la clase</h1>"
                "<figure>"
                "<img src='https://historia.nationalgeographic.com.es/medio/2019/01/30/salones-de-te_5b79ed9f_1200x630.jpg' style='width:230px;margin-left:90px;'>"
                "<figcaption style='font-size:8px; text-align: right'>historia.nationalgeographic.com.es</figcaption>"
                    "</figure>"
            "</div>", unsafe_allow_html=True)

    grafica9= False
    if st.button("Mostrar análisis de la gráfica 9"):
            grafica9=True

            if grafica9:

                fig2 = px.scatter(df, x="Fare", y="Pclass", color= "Sex", color_discrete_map= {'Male': 'green', 'female': 'blue'},
                #title="Precio del billete, según la clase",
                size= "Fare", size_max=12)
                fig2.update_yaxes(ticktext=["Primera clase", "Segunda clase", "Tercera clase"], tickvals=[1, 2, 3])
                st.plotly_chart(fig2)

                #Análisis gráfica 9
                st.markdown(
                             """
                             <div style="border: 0px solid #ff4b4b; padding: 10px; background-color: rgba(255, 75, 75, 0.2); color: #FFFFFF;">
                                        <b> Comentario:</b><br>
                                        Este gráfico muestra la relación entre el precio del billete y la clase de los pasajeros del Titanic.
                                        Se puede ver que la mayoría de los pasajeros de Primera Clase pagaron precios entre 0 y 300 dólares,
                                        mientras que los de Tercera Clase pagaron precios entre 0 y 100 dólares, con un pico entre 0 y 10 dólares
                            </div>
                             """, unsafe_allow_html=True)

            if st.button("Ocultar análisis de la gráfica 9"):
                            grafica9=False

    # Usamos línea de separación
    st.markdown("""<hr style="height:2px;background-color: white;" /> """, unsafe_allow_html=True)
    
    #------------------------------------------------------------------------

    # Gráfica 10
    #st.markdown(f'<h1 style="color:#ff4b4b;font-size:24px; webkit-text-stroke: 0.5px black">{"¿Dónde embarcaron los pasajeros según su clase?"}</h1>', unsafe_allow_html=True)
    st.markdown("<div style='display:flex;align-items:left;'>"
                "<h1 style='color:#ff4b4b;font-size:24px; webkit-text-stroke: 0px black'>¿Dónde embarcaron los pasajeros según su clase?</h1>"
                "<figure>"
                "<img src='https://cdn2.rsvponline.mx/files/rsvp/styles/wide/public/images/main/2020/titanic_first_class.jpg' style='width:230px;margin-left:90px;'>"
                "<figcaption style='font-size:8px; text-align: right'>rsvponline.mx</figcaption>"
                    "</figure>"
            "</div>", unsafe_allow_html=True)

    grafica10= False
    if st.button("Mostrar análisis de la gráfica 10"):
            grafica10=True

            if grafica10:

                ax1 = sns.countplot(x="Embarked", hue="Pclass", data=df, palette="pastel")
                plt.style.use("dark_background")
                ax1.bar_label(ax1.containers[0])
                ax1.bar_label(ax1.containers[1])
                ax1.bar_label(ax1.containers[2])
                ax1.set_xticklabels(["Southampton", "Cherbourg", "Queenstown"])
                #ax1.set_title("¿Dónde embarcaron los pasajeros según su clase?");
                st.pyplot()


        #Análisis gráfica 10
                st.markdown(
                             """
                             <div style="border: 0px solid #ff4b4b; padding: 10px; background-color: rgba(255, 75, 75, 0.2); color: #FFFFFF;">
                                        <b> Comentario:</b><br>
                                        Este gráfico muestra la distribución de los pasajeros del Titanic según el puerto de embarque y la clase en la que viajaban.
                                        Se puede ver que la mayoría de los pasajeros embarcaron en Southampton, seguido por Cherbourg y Queenstown.
                            </div>
                             """, unsafe_allow_html=True)

            if st.button("Ocultar análisis de la gráfica 10"):
                                    grafica10=False

    # Usamos línea de separación
    st.markdown("""<hr style="height:2px;background-color: white;" /> """, unsafe_allow_html=True)


    #------------------------------------------------------------------------

    # Gráfica 11
    #st.markdown(f'<h1 style="color:#ff4b4b;font-size:24px; webkit-text-stroke: 0.5px black">{"Relaciones familiares a bordo"}</h1>', unsafe_allow_html=True)
    st.markdown("<div style='display:flex;align-items:left;'>"
                "<h1 style='color:#ff4b4b;font-size:24px; webkit-text-stroke: 0px black'>Relaciones familiares a bordo</h1>"
                "<figure>"
                "<img src='https://ep00.epimg.net/cultura/imagenes/2012/04/13/album/1334327815_650313_1334328225_album_normal.jpg' style='width:230px;margin-left:120px;'>"
                "<figcaption style='font-size:8px; text-align: right'>elpais.com</figcaption>"
                    "</figure>"
            "</div>", unsafe_allow_html=True)

    grafica11= False
    if st.button("Mostrar análisis de la gráfica 11 - Cónyuges y hermanos"):
            grafica11=True

            if grafica11:

                fig_SibSp=px.pie(df, values=df["SibSp"].value_counts(),color_discrete_sequence=px.colors.sequential.RdBu,
                title="Pasajeros que viajaron con conyuges y/o hermanos a bordo")
                fig_SibSp.update_traces(textposition="outside", textinfo="percent+label")
                st.plotly_chart(fig_SibSp)

                #Análisis gráfica 11
                st.markdown(
                             """
                             <div style="border: 0px solid #ff4b4b; padding: 10px; background-color: rgba(255, 75, 75, 0.2); color: #FFFFFF;">
                                        <b> Comentario:</b><br>
                                        Este gráfico muestra el número de pasajeros del Titanic que viajaron con conyuges o hermanos a bordo.
                                        Se puede ver que la mayoría de los pasajeros viajaron solos, con el 68%. El 22% de los pasajeros viajaron
                                        con un conyugue o hermano, el 8% de los
                                        pasajeros viajaron con dos conyuges o hermanos y el 2% de los pasajeros viajaron con tres conyuges
                                        o hermanos.
                            </div>
                             """, unsafe_allow_html=True)

            if st.button("Ocultar análisis de la gráfica 11 - Cónyuges y hermanos"):
                                    grafica11=False

    # Usamos línea de separación
    #st.markdown("""<hr style="height:2px;border:none;color:#333;background-color: white;" /> """, unsafe_allow_html=True)



    #------------------------------------------------------------------------

    # Gráfica 12
    #st.markdown(f'<h1 style="color:#ff4b4b;font-size:24px; webkit-text-stroke: 0.5px black">{"Relaciones familiares a bordo"}</h1>', unsafe_allow_html=True)

    grafica12= False
    if st.button("Mostrar análisis de la gráfica 12 - Padres e hijos"):
            grafica12=True

            if grafica12:

                fig_Parch=px.pie(df, values=df["Parch"].value_counts(),color_discrete_sequence=px.colors.sequential.RdBu,
                title="Pasajeros que viajaron con padres y/o hijos a bordo")
                fig_Parch.update_traces(textposition="outside", textinfo="percent+label")
                st.plotly_chart(fig_Parch)

                #Análisis gráfica 12
                st.markdown(
                             """
                             <div style="border: 0px solid #ff4b4b; padding: 10px; background-color: rgba(255, 75, 75, 0.2); color: #FFFFFF;">
                                        <b> Comentario:</b><br>
                                        Igual que el anterior, pero esta vezcon padres o hijos a bordo.
                                        Se puede ver que la mayoría de los pasajeros viajaron sin padres o hijos, con el 76% de los pasajeros.
                                        Mientras, el 20% de los pasajeros viajaron con un padre o hijo y el 2% de los pasajeros viajaron con dos padres o hijos.
                            </div>
                             """, unsafe_allow_html=True)

            if st.button("Ocultar análisis de la gráfica 12 - Padres e hijos"):
                                    grafica12=False

    # Usamos línea de separación
    st.markdown("""<hr style="height:2px;border:none;color:#333;background-color: white;" /> """, unsafe_allow_html=True)



#------------------------------------------------------------------------

    # Gráfica 13
    #st.markdown(f'<h1 style="color:#ff4b4b;font-size:24px; webkit-text-stroke: 0.5px black">{"Relaciones familiares a bordo"}</h1>', unsafe_allow_html=True)
    st.markdown("<div style='display:flex;align-items:left;'>"
                "<h1 style='color:#ff4b4b;font-size:24px; webkit-text-stroke: 0px black'>Precio gastado en los billetes, según la edad y el género</h1>"
                "<figure>"
                "<img src='https://ichef.bbci.co.uk/news/640/cpsprodpb/17F4E/production/_124162189_gettyimages-1371405694.jpg' style='width:230px;margin-left:120px;'>"
                "<figcaption style='font-size:8px; text-align: right'>bbc.com</figcaption>"
                    "</figure>"
            "</div>", unsafe_allow_html=True)

    grafica13= False
    if st.button("Mostrar análisis de la gráfica 13"):
            grafica13=True

            if grafica13:

                fig_scatter_sex= px.scatter(df,x="Age", y="Fare", color="Sex")
                st.plotly_chart(fig_scatter_sex)

                #Análisis gráfica 13
                st.markdown(
                             """
                             <div style="border: 0px solid #ff4b4b; padding: 10px; background-color: rgba(255, 75, 75, 0.2); color: #FFFFFF;">
                                        <b> Comentario:</b><br>
                                        Este gráfico muestra la relación entre la edad y el precio de los billetes de los pasajeros del Titanic.
                            </div>
                             """, unsafe_allow_html=True)

            if st.button("Ocultar análisis de la gráfica 13"):
                                    grafica13=False

    # Usamos línea de separación
    st.markdown("""<hr style="height:2px;background-color: white;" /> """, unsafe_allow_html=True)




#------------------------------------------------------------------------

    # Gráfica 14
    #st.markdown(f'<h1 style="color:#ff4b4b;font-size:24px; webkit-text-stroke: 0.5px black">{"Relaciones familiares a bordo"}</h1>', unsafe_allow_html=True)
    st.markdown("<div style='display:flex;align-items:left;'>"
                "<h1 style='color:#ff4b4b;font-size:24px; webkit-text-stroke: 0px black'>Precio gastado en los billetes, según la edad y si sobrevivieron o no.</h1>"
                "<figure>"
                "<img src='https://elcorreoweb.es/documents/10157/0/675x406/0c3/675d400/none/10703/KUOS/image_content_17365071_20151026153705.jpg' style='width:230px;margin-left:120px;'>"
                "<figcaption style='font-size:8px; text-align: right'>elcorreoweb.es</figcaption>"
                    "</figure>"
            "</div>", unsafe_allow_html=True)

    grafica14= False
    if st.button("Mostrar análisis de la gráfica 14"):
            grafica14=True

            if grafica14:

                fig_scatter_sur= px.scatter(df,x="Age", y="Fare", color="Survived")
                st.plotly_chart(fig_scatter_sur)


                #Análisis gráfica 14
                st.markdown(
                             """
                             <div style="border: 0px solid #ff4b4b; padding: 10px; background-color: rgba(255, 75, 75, 0.2); color: #FFFFFF;">
                                        <b> Comentario:</b><br>
                                        Este gráfico muestra la relación entre la edad y el precio de los billetes de los pasajeros del Titanic.
                                        Se puede ver que los pasajeros que sobrevivieron generalmente pagaron precios más altos, especialmente entre los 20 y 40 años
                            </div>
                             """, unsafe_allow_html=True)


            if st.button("Ocultar análisis de la gráfica 14"):
                                    grafica14=False

    # Usamos línea de separación
    st.markdown("""<hr style="height:2px;background-color: white;" /> """, unsafe_allow_html=True)



#------------------------------------------------------------------------


    # Gráfica 15
    #st.markdown(f'<h1 style="color:#ff4b4b;font-size:24px; webkit-text-stroke: 0.5px black">{"Diferentes comparaciones entre la clase, el precio del billete y el sexo"}</h1>', unsafe_allow_html=True)
    st.markdown("<div style='display:flex;align-items:left;'>"
                "<h1 style='color:#ff4b4b;font-size:24px; webkit-text-stroke: 0px black'>Diferentes comparaciones entre la clase, el precio del billete y el género.</h1>"
                "<figure>"
                "<img src='https://sabiasquehistoria.files.wordpress.com/2020/04/titanic3.jpg' style='width:230px;margin-left:120px;'>"
                "<figcaption style='font-size:8px; text-align: right'>sabiasquehistoria.wordpress.com</figcaption>"
                    "</figure>"
            "</div>", unsafe_allow_html=True)

    grafica15= False
    if st.button("Mostrar análisis de la gráfica 15"):
            grafica15=True

            if grafica15:

                fig_lmplot=sns.lmplot(x="Age", y="Fare", row="Sex", col="Pclass",data=df)
                st.pyplot(fig_lmplot)

                #Análisis gráfica 15
                
                st.markdown(
                             """
                             <div style="border: 0px solid #ff4b4b; padding: 10px; background-color: rgba(255, 75, 75, 0.2); color: #FFFFFF;">
                                       <b> Comentario:</b><br>
                                        Este gráfico muestra la relación entre la edad y el precio de los billetes de los pasajeros del Titanic según el sexo y la clase.
                                        Se puede observar como en las 3 clases el hombre y la mujer gastan parecido en su billete.
                            </div>
                             """, unsafe_allow_html=True)


            if st.button("Ocultar análisis de la gráfica 15"):
                                    grafica15=False

    # Usamos línea de separación
    st.markdown("""<hr style="height:2px;background-color: white;" /> """, unsafe_allow_html=True)




#------------------------------------------------------------------------


    # Gráfica 16
    #st.markdown(f'<h1 style="color:#ff4b4b;font-size:24px; webkit-text-stroke: 0.5px black">{"Diferentes comparaciones entre la clase, el precio del billete y el sexo"}</h1>', unsafe_allow_html=True)
    st.markdown("<div style='display:flex;align-items:left;'>"
                "<h1 style='color:#ff4b4b;font-size:24px; webkit-text-stroke: 0px black'>Comparación en 3D sobre la edad, el precio del billete y el puerto de embarque.</h1>"
                "<figure>"
                "<img src='https://www.eluniverso.com/resizer/0sV9GyChdiBXuLYCO924r_2RUNM=/456x336/smart/filters:quality(70)/cloudfront-us-east-1.images.arcpublishing.com/eluniverso/BAQ3IZYUPBASTBKCV57J4FOP2Q.jpg' style='width:230px;margin-left:120px;'>"
                "<figcaption style='font-size:8px; text-align: right'>eluniverso.com</figcaption>"
                    "</figure>"
            "</div>", unsafe_allow_html=True)

    grafica16= False
    if st.button("Mostrar análisis de la gráfica 16"):
            grafica16=True

            if grafica16:

    
                
                fig_3d_titanic = go.Figure(data=[go.Scatter3d(x=df["Age"], y=df["Pclass"], z=df["Fare"],
                mode="markers", marker={"size": 3, "color":df["Survived"], "opacity": 1,
                    "colorscale":"inferno"},
                    showlegend=True,
                    legendgroup="Survived",
                    name= "No sobrevivió"
                    )])

                    # Update figure layout
                fig_3d_titanic.update_layout(scene = dict(
                        xaxis_title="Edad",
                        yaxis_title="Clase",
                        zaxis_title="Precio billete"),
                        legend=dict(x=0, y=1))

                    # Show figure
                st.plotly_chart(fig_3d_titanic)
                

                #Análisis gráfica 16
                
                st.markdown(
                             """
                             <div style="border: 0px solid #ff4b4b; padding: 10px; background-color: rgba(255, 75, 75, 0.2); color: #FFFFFF;">
                                        <b> Comentario:</b><br>
                                        Este gráfico muestra en un gráfico 3D la relación de supervivencia entre el precio del billete
                                        la clase y la edad. Se puede observar como a más precio del billete nos encontramos a más supervivientes.
                                        También vemos la cantidad de no sobrevivientes de la tercera clase.
                            </div>
                             """, unsafe_allow_html=True)


            if st.button("Ocultar análisis de la gráfica 16"):
                                    grafica16=False

    # Usamos línea de separación
    st.markdown("""<hr style="height:2px;background-color: white;" /> """, unsafe_allow_html=True)




#------------------------------------------------------------------------


    # Gráfica 17
    #st.markdown(f'<h1 style="color:#ff4b4b;font-size:24px; webkit-text-stroke: 0.5px black">{"Diferentes comparaciones entre la clase, el precio del billete y el sexo"}</h1>', unsafe_allow_html=True)
    st.markdown("<div style='display:flex;align-items:left;'>"
                "<h1 style='color:#ff4b4b;font-size:24px; webkit-text-stroke: 0px black'>Diagrama de pastel por niveles con diferentes condiciones.</h1>"
                "<figure>"
                "<img src='https://img.microsiervos.com/images2021/titanic-southampton.jpg' style='width:230px;margin-left:120px;'>"
                "<figcaption style='font-size:8px; text-align: right'>microsiervos.com</figcaption>"
                    "</figure>"
            "</div>", unsafe_allow_html=True)

    grafica17= False
    if st.button("Mostrar análisis de la gráfica 17"):
            grafica17=True

            if grafica17:

                fig_pastel = px.sunburst(df, path=['Sex',"Survived", 'Pclass', "Embarked"], values=df.value_counts(),
                      color_discrete_sequence=px.colors.qualitative.Dark24)
                fig_pastel.update_layout(title_text = "Diagrama de pastel por niveles", title_x = 0.5,
                    )
                fig_pastel.update_traces(textinfo="label+value")

                st.plotly_chart(fig_pastel)

                #Análisis gráfica 17
                
                st.markdown(
                             """
                             <div style="border: 0px solid #ff4b4b; padding: 10px; background-color: rgba(255, 75, 75, 0.2); color: #FFFFFF;">
                                        <b> Comentario:</b><br>
                                        El diagrama muestra la distribución entre los géneros, la supervivencia, la clase social
                                        y el puerto de embarque, y la cantidad de personas de cada categoría.
                                        Es una muy buena forma e interactiva de ver y entender mejor cómo estos factores afectaron la supervivencia en el desastre del Titanic.
                            </div>
                             """, unsafe_allow_html=True)


            if st.button("Ocultar análisis de la gráfica 17"):
                                    grafica17=False

    # Usamos línea de separación
    st.markdown("""<hr style="height:2px;background-color: white;" /> """, unsafe_allow_html=True)


    st.markdown("<h3 style='text-align: center ; color: #FFFFFF;'>Hablemos de supervivencia</h3>" ,unsafe_allow_html=True)


    #------------------------------------------------------------------------


    # Gráfica 18
    #st.markdown(f'<h1 style="color:#ff4b4b;font-size:24px; webkit-text-stroke: 0.5px black">{"Diferentes comparaciones entre la clase, el precio del billete y el sexo"}</h1>', unsafe_allow_html=True)
    st.markdown("<div style='display:flex;align-items:left;'>"
                "<h1 style='color:#ff4b4b;font-size:24px; webkit-text-stroke: 0px black'>¿Cuántos pasajeros sobrevivieron a la catástrofe?</h1>"
                "<figure>"
                "<img src='https://static.dw.com/image/15881891_303.jpg' style='width:230px;margin-left:120px;'>"
                "<figcaption style='font-size:8px; text-align: right'>dw.com</figcaption>"
                    "</figure>"
            "</div>", unsafe_allow_html=True)

    grafica18= False
    if st.button("Mostrar análisis de la gráfica 18"):
            grafica18=True

            if grafica18:

                supervivientes = df.groupby(['Survived']).size().reset_index(name='counts')
                fig_supervivientes =px.bar(supervivientes, x='Survived', y='counts',
                labels={'Survived':'Survived','counts':'PassengersId'},
                title="Pasajeros supervivientes del Titanic",
                template="plotly_dark")
                st.plotly_chart(fig_supervivientes)
                

                #Análisis gráfica 18
                
                st.markdown(
                             """
                             <div style="border: 0px solid #ff4b4b; padding: 10px; background-color: rgba(255, 75, 75, 0.2); color: #FFFFFF;">
                                        <b> Comentario:</b><br>
                                        Este sencillo gráfico de barras muestra la cantidad de pasajeros que sobrevivieron al
                                        desastre del Titanic. Podemos observar que la mayoría no lo consiguieron. 
                                        
                            </div>
                             """, unsafe_allow_html=True)


            if st.button("Ocultar análisis de la gráfica 18"):
                                    grafica18=False

    # Usamos línea de separación
    st.markdown("""<hr style="height:2px;background-color: white;" /> """, unsafe_allow_html=True)




 #------------------------------------------------------------------------


    # Gráfica 19
    #st.markdown(f'<h1 style="color:#ff4b4b;font-size:24px; webkit-text-stroke: 0.5px black">{"Diferentes comparaciones entre la clase, el precio del billete y el sexo"}</h1>', unsafe_allow_html=True)
    st.markdown("<div style='display:flex;align-items:left;'>"
                "<h1 style='color:#ff4b4b;font-size:24px; webkit-text-stroke: 0px black'>Supervivencia de los pasajeros, según su clase</h1>"
                "<figure>"
                "<img src='https://imagenes.lainformacion.com/files/twitter_thumbnail/uploads/imagenes/2019/09/04/5d6f97e6449e4.jpeg' style='width:230px;margin-left:120px;'>"
                "<figcaption style='font-size:8px; text-align: right'>lainformacion.com</figcaption>"
                    "</figure>"
            "</div>", unsafe_allow_html=True)

    grafica19= False
    if st.button("Mostrar análisis de la gráfica 19"):
            grafica19=True

            if grafica19:

                st.image("Imágenes/supervivencia de los pasajeros según su clase.png")


                #Análisis gráfica 19
                
                st.markdown(
                             """
                             <div style="border: 0px solid #ff4b4b; padding: 10px; background-color: rgba(255, 75, 75, 0.2); color: #FFFFFF;">
                                        <b> Comentario:</b><br>
                                        Este gráfico de barras realizado con seaborn nos muestra la cantidad de 
                                        pasajeros que sobrevivieron según su clase. 
                                        Destaca con creces la cantidad de pasajeros de tercera clase que no sobrevivieron.
                                        A su vez, puede parecer engañoso porque sobrevivieron más pasajeros de tercera que
                                        de segunda clase, pero es porque hay muchos más pasajeros de tercera. 
                                        En el siguiente gráfico se verá la proporción real.
                            </div>
                             """, unsafe_allow_html=True)


            if st.button("Ocultar análisis de la gráfica 19"):
                                    grafica19=False

    # Usamos línea de separación
    st.markdown("""<hr style="height:2px;background-color: white;" /> """, unsafe_allow_html=True)


#------------------------------------------------------------------------


    # Gráfica 20
    #st.markdown(f'<h1 style="color:#ff4b4b;font-size:24px; webkit-text-stroke: 0.5px black">{"Diferentes comparaciones entre la clase, el precio del billete y el sexo"}</h1>', unsafe_allow_html=True)
    st.markdown("<div style='display:flex;align-items:left;'>"
                "<h1 style='color:#ff4b4b;font-size:24px; webkit-text-stroke: 0px black'>¿En qué clase debes ir para tener más posibilidades de sobrevivir en el Titanic?</h1>"
                "<figure>"
                "<img src='https://historia.nationalgeographic.com.es/medio/2022/07/15/cpmcdtita-fe022_a9748bb4_1280x750.jpeg' style='width:230px;margin-left:120px;'>"
                "<figcaption style='font-size:8px; text-align: right'>historia.nationalgeographic.com.es</figcaption>"
                    "</figure>"
            "</div>", unsafe_allow_html=True)

    grafica20= False
    if st.button("Mostrar análisis de la gráfica 20"):
            grafica20=True

            if grafica20:

                grupo_clase = df.groupby(["Pclass", "Survived"]).size().reset_index(name="counts")
                grupo_clase["probability"] = grupo_clase.apply(lambda row: row.counts / grupo_clase[grupo_clase.Pclass == row.Pclass]["counts"].sum()*100, axis=1).round(2)
                fig_supervivientes_clase2 = px.bar(grupo_clase, x="Pclass", y="probability",
                color="Survived", labels={"Pclass":"Clase","probability":"Probabilidad de sobrevivir"},
                text_auto=True,
                title="Probabilidad de sobrevivir en el Titanic según la clase")
                st.plotly_chart(fig_supervivientes_clase2)
                
               



                #Análisis gráfica 20
                
                st.markdown(
                             """
                             <div style="border: 0px solid #ff4b4b; padding: 10px; background-color: rgba(255, 75, 75, 0.2); color: #FFFFFF;">
                                        <b> Comentario:</b><br>
                                        Este gráfico muestra la probabilidad de supervivencia según la clase social. Es la forma 
                                        más representativa de entender cómo afectó la clase social en la superviviencia del desastre.
                                        Aquí podemos ver las pocas oportunidades que tuvieron la tercera clase respecto a la primera.
                            </div>
                             """, unsafe_allow_html=True)


            if st.button("Ocultar análisis de la gráfica 20"):
                                    grafica20=False

    # Usamos línea de separación
    st.markdown("""<hr style="height:2px;background-color: white;" /> """, unsafe_allow_html=True)







#------------------------------------------------------------------------


    # Gráfica 21
    #st.markdown(f'<h1 style="color:#ff4b4b;font-size:24px; webkit-text-stroke: 0.5px black">{"Diferentes comparaciones entre la clase, el precio del billete y el sexo"}</h1>', unsafe_allow_html=True)
    st.markdown("<div style='display:flex;align-items:left;'>"
                "<h1 style='color:#ff4b4b;font-size:24px; webkit-text-stroke: 0px black'>¿Saliendo de qué puerto tienes más posibilidades de sobrevivir en el Titanic?</h1>"
                "<figure>"
                "<img src='https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/embarque-titanic-1523699983.jpg' style='width:230px;margin-left:120px;'>"
                "<figcaption style='font-size:8px; text-align: right'>esquire.com</figcaption>"
                    "</figure>"
            "</div>", unsafe_allow_html=True)

    grafica21= False
    if st.button("Mostrar análisis de la gráfica 21"):
            grafica21=True

            if grafica21:

                st.image("Imágenes/supervivencia de los pasajeros según su embarque.png")
               



                #Análisis gráfica 21
                
                st.markdown(
                             """
                             <div style="border: 0px solid #ff4b4b; padding: 10px; background-color: rgba(255, 75, 75, 0.2); color: #FFFFFF;">
                                        <b> Comentario:</b><br>
                                        Este gráfico muestra la la cantidad de pasajeros que sobrevivieron o no según del puerto de embarque.
                                        La realidad que aparentemente esto no influye en la supervivencia de la catástrofe,
                                        pero podemos observarlo como curiosidad. 
                            </div>
                             """, unsafe_allow_html=True)


            if st.button("Ocultar análisis de la gráfica 21"):
                                    grafica21=False

    # Usamos línea de separación
    st.markdown("""<hr style="height:2px;background-color: white;" /> """, unsafe_allow_html=True)






#------------------------------------------------------------------------


    # Gráfica 22
    #st.markdown(f'<h1 style="color:#ff4b4b;font-size:24px; webkit-text-stroke: 0.5px black">{"Diferentes comparaciones entre la clase, el precio del billete y el sexo"}</h1>', unsafe_allow_html=True)
    st.markdown("<div style='display:flex;align-items:left;'>"
                "<h1 style='color:#ff4b4b;font-size:24px; webkit-text-stroke: 0px black'>Probabilidad de sobrevivir en el Titanic, según el puerto de embarque</h1>"
                "<figure>"
                "<img src='https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/embarque-titanic-1523699983.jpg' style='width:230px;margin-left:120px;'>"
                "<figcaption style='font-size:8px; text-align: right'>esquire.com</figcaption>"
                    "</figure>"
            "</div>", unsafe_allow_html=True)

    grafica22= False
    if st.button("Mostrar análisis de la gráfica 22"):
            grafica22=True

            if grafica22:

                grupo_embarque = df.groupby(["Embarked", "Survived"]).size().reset_index(name="counts")
                grupo_embarque["probability"] = grupo_embarque.apply(lambda row: row.counts / grupo_embarque[grupo_embarque.Embarked == row.Embarked]["counts"].sum()*100, axis=1).round(2)
                fig_supervivientes_embarque2 = px.bar(grupo_embarque, x="Embarked", y="probability",
                color="Survived", labels={"Embarked":"Puerto de Embarque","probability":"Probabilidad de sobrevivir"},
                text_auto=True,
                title="Probabilidad de sobrevivir en el Titanic, según el puerto de embarque")
                st.plotly_chart(fig_supervivientes_embarque2)
               



                #Análisis gráfica 22
                
                st.markdown(
                             """
                             <div style="border: 0px solid #ff4b4b; padding: 10px; background-color: rgba(255, 75, 75, 0.2); color: #FFFFFF;">
                                       <b> Comentario:</b><br>
                                        En el anterior se mostraban los números de supervivientes según el puerto,
                                        en este gráfico se muestra el porcentaje real de la probabilidad de sobrevivir según del puertode embarque.
                                        Aparentemente esto no influye en la superviviencia del pasajero, pero es curioso ver la "suerte" de los
                                        embarcados en Cherbourg respecto a los demás. 
                            </div>
                             """, unsafe_allow_html=True)


            if st.button("Ocultar análisis de la gráfica 22"):
                                    grafica22=False

    # Usamos línea de separación
    st.markdown("""<hr style="height:2px;background-color: white;" /> """, unsafe_allow_html=True)




    #------------------------------------------------------------------------


    # Gráfica 23
    #st.markdown(f'<h1 style="color:#ff4b4b;font-size:24px; webkit-text-stroke: 0.5px black">{"Diferentes comparaciones entre la clase, el precio del billete y el sexo"}</h1>', unsafe_allow_html=True)
    st.markdown("<div style='display:flex;align-items:left;'>"
                "<h1 style='color:#ff4b4b;font-size:24px; webkit-text-stroke: 0px black'>¿Cuál es tu probabilidad de sobrevivir en el Titanic según el género?</h1>"
                "<figure>"
                "<img src='https://img.ecartelera.com/noticias/fotos/37000/37072/1.jpg' style='width:230px;margin-left:120px;'>"
                "<figcaption style='font-size:8px; text-align: right'>ecartelera.com</figcaption>"
                    "</figure>"
            "</div>", unsafe_allow_html=True)

    grafica23= False
    if st.button("Mostrar análisis de la gráfica 23"):
            grafica23=True

            if grafica23:

                grupo_genero = df.groupby(["Sex", "Survived"]).size().reset_index(name="counts")
                grupo_genero["probability"] = grupo_genero.apply(lambda row: row.counts / grupo_genero[grupo_genero.Sex == row.Sex]["counts"].sum()*100, axis=1).round(2)
                fig_supervivientes_genero = px.bar(grupo_genero, x="Sex", y="probability",
                color="Survived", labels={"Sex":"Género",'probability':"Probabilidad de sobrevivir"},
                text_auto=True,
                title="Probabilidad de sobrevivir en el Titanic según tu género")
                st.plotly_chart(fig_supervivientes_genero)
               



                #Análisis gráfica 23
                
                st.markdown(
                             """
                             <div style="border: 0px solid #ff4b4b; padding: 10px; background-color: rgba(255, 75, 75, 0.2); color: #FFFFFF;">
                                        <b> Comentario:</b><br>
                                        El gráfico muestra la probabilidad de supervivencia según el género. No es díficil ver la
                                        gran diferencia entre la probabilidad de sobrevivir si eres mujer o si eres hombre.
                                        Hasta un 74.2% de mujeres sobrevivieron a la catástrofe.
                            </div>
                             """, unsafe_allow_html=True)


            if st.button("Ocultar análisis de la gráfica 23"):
                                    grafica23=False

    # Usamos línea de separación
    st.markdown("""<hr style="height:2px;background-color: white;" /> """, unsafe_allow_html=True)



    #------------------------------------------------------------------------


    # Gráfica 24
    #st.markdown(f'<h1 style="color:#ff4b4b;font-size:24px; webkit-text-stroke: 0.5px black">{"Diferentes comparaciones entre la clase, el precio del billete y el sexo"}</h1>', unsafe_allow_html=True)
    st.markdown("<div style='display:flex;align-items:left;'>"
                "<h1 style='color:#ff4b4b;font-size:24px; webkit-text-stroke: 0px black'>¿Qué edad deberías tener para tener más posibilidades de sobrevivir en el Titanic?</h1>"
                "<figure>"
                "<img src='https://historia.nationalgeographic.com.es/medio/2017/04/07/los-huerfanos-del-titanic_a3402840.jpg' style='width:230px;margin-left:120px;'>"
                "<figcaption style='font-size:8px; text-align: right'>historia.nationalgeographic.com.es</figcaption>"
                    "</figure>"
            "</div>", unsafe_allow_html=True)

    grafica24= False
    if st.button("Mostrar análisis de la gráfica 24"):
            grafica24=True

            if grafica24:

                

                
                edades = df.groupby(["rango_edad", "Survived"]).size().reset_index(name="counts")
                edades["probability"] = edades.apply(lambda row: row.counts / edades[edades.rango_edad == row.rango_edad]["counts"].sum()*100, axis=1).round(2)
                
                #Figura
                fig_supervivientes_edad = px.histogram(edades, x="rango_edad", y="probability", color="Survived",
                histfunc="avg", title="Probabilidad de sobrevivir en el Titanic, según tu edad", nbins=8,
                text_auto=True,
                labels={"rango_edad":"Rango de edades","probability":"Probabilidad de sobrevivir"})
                
                st.plotly_chart(fig_supervivientes_edad)
               
            



                #Análisis gráfica 24
                
                st.markdown(
                             """
                             <div style="border: 0px solid #ff4b4b; padding: 10px; background-color: rgba(255, 75, 75, 0.2); color: #FFFFFF;">
                                        <b> Comentario:</b><br>
                                        Este histograma muestra la probabilidad de supervivencia según la edad. Si tienes más de 60 años
                                        es muy probable que no sobrevivas. Sin embargo, más de la mitad de los niños hasta 10 años sí
                                        lo consiguieron. 
                            </div>
                             """, unsafe_allow_html=True)


            if st.button("Ocultar análisis de la gráfica 24"):
                                    grafica24=False

    # Usamos línea de separación
    st.markdown("""<hr style="height:2px;background-color: white;" /> """, unsafe_allow_html=True)


   #------------------------------------------------------------------------


    # Gráfica 25
    #st.markdown(f'<h1 style="color:#ff4b4b;font-size:24px; webkit-text-stroke: 0.5px black">{"Diferentes comparaciones entre la clase, el precio del billete y el sexo"}</h1>', unsafe_allow_html=True)
    st.markdown("<div style='display:flex;align-items:left;'>"
                "<h1 style='color:#ff4b4b;font-size:24px; webkit-text-stroke: 0px black'>¿Tienes más probabilidades de sobrevivir viajando solo en el Titanic?</h1>"
                "<figure>"
                "<img src='https://pymstatic.com/60560/conversions/frases-titanic-social.jpg' style='width:230px;margin-left:120px;'>"
                "<figcaption style='font-size:8px; text-align: right'>psicologiaymente.com/</figcaption>"
                    "</figure>"
            "</div>", unsafe_allow_html=True)

    grafica25= False
    if st.button("Mostrar análisis de la gráfica 25"):
            grafica25=True

            if grafica25:

                
                solitarios = df.groupby(["viajando_solos", "Survived"]).size().reset_index(name='counts')
                solitarios["probability"] = solitarios.apply(lambda row: row.counts / solitarios[solitarios.viajando_solos == row.viajando_solos]['counts'].sum()*100, axis=1).round(2)

                #Figura
                fig_supervivientes_solos = px.bar(solitarios, x="viajando_solos", y="probability",
                text_auto=True,
                color="Survived", labels={"viajando_solos":"Viajan solos (0 = No , 1 = Sí)","probability":"Probabilidad de sobrevivir"},
                title="Probabilidad si viajas solo. Suma de la columna SibSp con la columna Parch")
                
                st.plotly_chart(fig_supervivientes_solos)
               
            



                #Análisis gráfica 25
                
                st.markdown(
                             """
                             <div style="border: 0px solid #ff4b4b; padding: 10px; background-color: rgba(255, 75, 75, 0.2); color: #FFFFFF;">
                                        <b> Comentario:</b><br>
                                        En este gráfico se muestra  la probabilidad de supervivencia según si los pasajeros
                                        viajaban solos o no. Según los datos, los pasajeros que viajaban solos tenían una menor
                                        probabilidad de sobrevivir en el desastre del Titanic. Por contra, esto sugiere que los pasajeros que viajaban
                                        con familiares o amigos tuvieron una mejor oportunidad de supervivencia.
                            </div>
                             """, unsafe_allow_html=True)


            if st.button("Ocultar análisis de la gráfica 25"):
                                    grafica25=False

    # Usamos línea de separación
    st.markdown("""<hr style="height:2px;background-color: white;" /> """, unsafe_allow_html=True)

 

    st.subheader("Conclusiones")
    
    #-----------------Conclusiones finales-------------- #
    st.markdown(
        """
    - La mayoría de los pasajeros eran hombres.<br>
    - La mayoría de los pasajeros tenían una clase baja (tercera clase).<br>
    - La mayoría de los pasajeros embarcaron en el puerto de Southampton.<br>
    - La mayoría de los pasajeros no sobrevivió al hundimiento del Titanic.<br>
    - La tasa de supervivencia de mujeres y niños hasta 10 años fue significativamente mayor que la del resto.<br>
    - Se podría decir que viajar solo fue un factor determinante en la no supervivencia de los pasajeros.<br>
    - La clase también fue un factor decisivo en la supervivencia. La tasa de la primera clase fue mayor que las clases baja y media.<br>
    - La edad y el precio del billete no tuvieron un impacto significativo en la tasa de supervivencia.<br>
    - El puerto de embarque tampoco supuso gran impacto en la tasa de supervivencia.
    
    """,unsafe_allow_html=True)
    







###################### MODELO DE PREDICCIÓN ################################




if menu =="Modelo de predicción de supervivencia":
    # Título de la pestaña Análisis
    st.markdown("<h2 style='text-align: center; background-color: #ff4b4b ; color: #FFFFFF;'>¿Sobrevivirías en el Titanic?</h2>" ,unsafe_allow_html=True)
    
    # Separación
    st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True)

    
    #Para importar el modelo
    import joblib

    #Cargamos el modelo aquí
    LR_loaded = joblib.load('titanic_regresion_logistica.pkl')

    ### Preprocesamiento-------------------------------------------------------------------------------
    #Convertimos las columnas categóricas en numéricas
    df.replace({'Sex':{'male': 0, 'female':1}, 'Embarked':{'Southampton':0, 'Cherbourg':1, 'Queenstown':2}}, inplace=True)
    df_titanic =  df[["Sex", "Pclass", "Age", "Fare", "Embarked", "Survived"]]



    # Comenzamos en la pestaña
    st.subheader('Modelo de Machine Learning elegido: **Logistic Regression**')
    st.markdown("<h5 style='text-align: left; color: #FFFFFF;'>Precisión del 0.81%</h5>" ,unsafe_allow_html=True)

    # Usamos línea de separación
    st.markdown("""<hr style="height:2px;background-color: white;" /> """, unsafe_allow_html=True)
    


    # Datos de entrada en el sidebar
    with st.sidebar:

        st.markdown("""
        <p style="text-align: center; color: #ff5a60; font-size: 30px;"><strong>Parámetros de supervivencia</strong></p>
        """, unsafe_allow_html=True)
        st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True)    #separación

        st.markdown("""
        <p style="text-align: center; color: #ffffff; background-color: #ff5a60; font-size: 20px;">Selección del género</p>
        """, unsafe_allow_html=True)
        genero =  st.text_input("**Hombre: 0 | Mujer: 1**", "0")
        genero = float(genero)
        
        st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True)    #separación
        
        st.markdown("""
        <p style="text-align: center; color: #ffffff; background-color: #ff5a60; font-size: 20px;">Selección de clase</p>
        """, unsafe_allow_html=True)
        clase =  st.text_input("**Primera, segunda o tercera clase | Indica 1, 2 o 3**", "1")
        clase = float(clase)

        st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True)   #separación
    
        st.markdown("""
        <p style="text-align: center; color: #ffffff; background-color: #ff5a60; font-size: 20px;">Selecciona la edad</p>
        """, unsafe_allow_html=True)
        year =  st.text_input("Ingresa tu edad: ", "31")
        year = float(year)

        st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True)    #separación

        st.markdown("""
        <p style="text-align: center; color: #ffffff; background-color: #ff5a60; font-size: 20px;">Precio del billete</p>
        """, unsafe_allow_html=True)
        price =  st.text_input("Ingresa el precio del billete, siendo en la época del Titanic el mínimo 0, y el máximo 500: ", "53")
        price = float(price)

        st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True)    #separación

        st.markdown("""
        <p style="text-align: center; color: #ffffff; background-color: #ff5a60; font-size: 20px;">Puerto de embarque</p>
        """, unsafe_allow_html=True)
        puerto =  st.text_input("Southampton:0, Cherbourg:1, Queenstown:2", "0")
        puerto = float(puerto)
        

    #Los datos de entrada introducidos manualmente se guardan en este diccionario
    data = {
        'Sex': genero,
        'Pclass': clase,
        'Age': year,
        'Fare': price,
        'Embarked': puerto,
        
    }

    # Convertir los datos de entrada en un DataFrame de Pandas
    input_data = pd.DataFrame([data])

    # st.dataframe(input_data)

    st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True) #separación

    # Realizar la predicción
    prediction = LR_loaded.predict(input_data)
    probs = LR_loaded.predict_proba(input_data).round(1)*100
    probabilidad = probs[0][1]
    

    # Botón para realizar la predicción
    if st.button("Realizar predicción con los parámetros elegidos"):
            st.subheader("Tienes un {:.1f}% de sobrevivir en el Titanic".format(probabilidad))
            if (prediction[0] == 0):
                st.text("Con estas variables, se podría decir que no has sobrevivido") 
                st.image("Imágenes/nosuperviviente.jpg")
                st.markdown("Imagen de diariovasco.com")
            
            else:
                st.text("Con estas variables, se podría decir que has sobrevivido")
                st.image("Imágenes/superviviente.jpg")
                st.markdown("Imagen de andina.pe")

  

    st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True)

    # Usamos línea de separación
    st.markdown("""<hr style="height:2px;background-color: white;" /> """, unsafe_allow_html=True)

    st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True)    # Separación



    #------ Explicación del modelo ---------#

    st.markdown("""
        <p style="text-align: left; color: #ff5a60; font-size: 34px;"><strong>Explicación del modelo</strong></p>
        """, unsafe_allow_html=True)

    st.markdown(
    "<font size='4' color='white'>He usado un modelo de regresión logística en mi proyecto sobre el Titanic porque se trata de un problema de clasificación binaria, es decir, predecir si un pasajero sobrevivió o no. La regresión logística es un modelo de clasificación que se basa en la regresión lineal y utiliza una funciónlogística para estimar la probabilidad de que una observación pertenezca a una de las dos categorías.</font>",
    unsafe_allow_html=True
    )

    # Captura de imagen con la precisión para acompañar
    st.image("Imágenes/clasificacion.PNG")

    st.markdown(
    "<font size='4' color='white'>Para implementar el modelo seleccioné y procesé los datos cuidadosamente, eliminando valores faltantes y transformando aquellas variables categóricas a variables numéricas. Luego, dividí mi conjunto de datos en un conjunto de entrenamiento del 80% y un conjunto de prueba del 20% restante.</font>",
    unsafe_allow_html=True
    )

    st.markdown(
    "<font size='4' color='white'>Después, entrené el modelo de regresión logística con el conjunto de entrenamiento y usé las características de los pasajeros para predecir sus resultados de supervivencia. Finalmente, evalué el rendimiento del modelo utilizando medidas de desempeño como la precisión y el f1-score para terminar implementándolo en mi aplicación de Streamlit y poder realizar predicciones interactivas.</font>",
    unsafe_allow_html=True
    )
    
    
    
    #-PROVAS
    if menu == "Dataframe":
    st.markdown("<h2 style='text-align: center;  background-color: #ff4b4b ; color: #FFFFFF;'>Dataframe</h2>" ,unsafe_allow_html=True)
    
    # Creamos el Menú vertical para las categorías
    opciones = ["Accion", "Aventura", "Deportes", "EarlyAcces", "Estrategia", "Free", "MMORPG", "RPG", "Simulacion", "Indie"]
    categoria = option_menu(
        "Selecciona una categoría:",
        opciones,
        default_index=0
    )
    
    # Agregamos un sidebar para filtrar el DataFrame por precio
    st.sidebar.header('Filtrar por precio')
    min_value, max_value = st.sidebar.slider(
        'Selecciona un rango de precio:',
        0.0, 100.0, (0.0, 100.0)
    )
    
    # Agregamos un sidebar para filtrar el DataFrame por Owners_max_text
    st.sidebar.header('Filtrar por Jugadores máximos')
    owners_options = ["Sin filtro", "500.0M", "100.0M", "50.0M", "20.0M", "10.0M", "2.0M", "1.0M", "500.0K", "200.0K", "100.0K", "50.0K", "20.0K", "0.00"]
    owners = st.sidebar.selectbox(
        "Selecciona una opción de jugadores máximos:",
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
        
    # Mostramos el Dataframe correspondiente a la categoría y filtros seleccionados
    container = st.empty()
    container.markdown("<style> .css-1v3fvcr {text-align: center !important;} </style>", unsafe_allow_html=True)
    container.dataframe(df)

    publishers = ['Electronic Arts', 'Ubisoft', 'Activision', 'Bethesda Softworks', 'Microsoft Studios', 'Square Enix', 'Sega', 'Capcom', 'Bandai Namco', 'Valve']
    
    # Agregamos un sidebar para filtrar el DataFrame por Publisher
    st.sidebar.header('Filtrar por Publisher')
    for publisher in publishers:
        if st.sidebar.button(publisher):
            # Filtramos el DataFrame por el Publisher seleccionado
            df_filtered = df[df['Publisher(s)'] == publisher]
            # Actualizamos el espacio en blanco con el nuevo dataframe filtrado
            container.dataframe(df_filtered)