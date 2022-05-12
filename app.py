#llamar librerias
from dash import Dash, html,dcc #Libreria para servidor web de Data science

#Declarar Objetos Principales
app = Dash(__name__)

#Configurar el sitio web
app.layout = html.Div([html.H1('Trabajo Emanuel Rios Silva'),
                       html.Div('Emanuel Rios Silva Parte 2')])

#Funcion Principal
if __name__ == '__main__':
  #Asi se carga el objeto principal a la interfaces de red con el puerto 80
  app.run_server(host='0.0.0.0',port=80)
  
  
