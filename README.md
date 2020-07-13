# Actividad Integradora 2 - Visión Computacional
## ¿En qué consiste el proyecto?
## Recolección de imagenes
En esta actividad se desarrolla la técnica de "Web Data Scraping" enfocada en automatizar el proceso de adquisición de imagenes. Mediante una palabra clave proporcionada por el usuario, el programa inserta esa palabra en el buscador de dos bases de datos: "http://image-net.org" y "https://www.shutterstock.com". Por último, una vez que se consiguen las imagenes, el programa las separa por direcciones en dos carpetas "test" y "train".


## ¿Para qué es útil?
Nuestro programa esta enfocado a imagenes, sin embargo, lo que queremos demostrar es la importancia de automatizar este tipo de procesos. Cuando se desarrolla un proyecto que requiere la captura de datos, el tiempo destinado para esta actividad puede variar dependiendo de la cantidad de datos que se requiere pero si desde un comienzo se desarrolla un programa que realice la captura de manera automatica esto nos permitiría enfocar nuestros recursos a tareas que puedan ser de mayor jerarquía. 

## ¿Cómo empezar?
Para iniciar con este programa, se necesita primero instalar el siguiente paquete:

- Selenium

Para realizar la instalación, se puede abrir la terminal y ejecutar los siguientes comandos
```
python3 pip install selenium

```
Tambien es necesario instalar el webdriver de Google Chrome.
*Nota = El web driver depende del browser que utilizaras para el proyecto.

Además no olvidar de importar los siguientes modulos: 

- urllib.request
- pandas
- numpy



## Información adicional
Si se cuenta con alguna duda o comentario, se puede contactar con los creadores del programa. Estos son:
- Noé Campos
- Daniel Garza
- Daniela García
- Juan González
- Rodrigo Medina
