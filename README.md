# Práctica 1: Topología y ciclo de vida de los datos
Webscraper a la web de pisos.com

## Descripción
Esta práctica se ha realizado bajo el contexto de la asignatura Tipología y ciclo de vida de los datos, perteneciente al Máster en Ciencia de Datos de la Universitat Oberta de Catalunya. En ella, se aplican técnicas de web scraping mediante el lenguaje de programación Python para extraer así datos de las webs Pisos.com y datos.gob.es y generar un dataset.

## Miembros del equipo
La actividad ha sido realizada por Andrea Giralt y Manuel Fernandez. 

## Documento con las respuestas
* [Documento con la memoria de la práctica en pdf](docs/memoria.pdf)

## Video explicativo
* [Enlace al video explicativo](https://drive.google.com/file/d/1hQHQwDLWJeYcxgqUthmUtMuxVzqhWgd8/view?usp=sharing)

## Ejecutar el spider
Desde una terminal, lanzar el comando.
En una terminal compatible con linux (WSL2 o macOS) Para ver los comandos disponibles ejecutamos:

```bash
make help 
```

El sistema nos mostrará por pantalla las siguientes opciones:
```
🚀 local : build and launch local environment
🖥️ console : open a python console
🕷️ spider: runs the complete spider
🕷️ zones: runs zones spider
🕷️ previews: runs previews spider
🕷️ details: runs details spider
💾 csv: dump into csv
🗂️ dump : dump database
🏁 start : starts environment
🛑 stop : stops environment
🗑️ remove : remove all containers
```

* ```local```:Arranca los contenedores docker necesarios para ejecutar el spider.
* ```console```: Inicia una consola dentro del contenedor de python (Es útil si se quiere ejecutar una parte del *spider*)
* ```spider```: Lanza todas las tares del spider al completo.
* ```zones```: Importa las zonas del mapa de Mallorca.
* ```previews```: Extrae la información que aparece en los listados de búsquedas.
* ```details```: Extrae información complementaria como coordenadas en el mapa, propietario del anuncio...
* ```csv```: Genera el csv ```data/real_states.csv``` con la información extraida de las web de pisos.com
* ```dump```: Realiza un dump de la base de datos.
* ```start```: Arranca el entorno
* ```stop```: Para el entorno.
* ```remove```: Borra todos los contenedores.


## Script ```parser```
Para acceder al contenedor de python, ejecutamos la instrucción:
```
make console
```
Una vez dentro, ejecutamos la siguiente instrucción para ver qué opciones nos da el comando ```parser```:
```
./parser -h
```
Nos aparecerán las siguientes opciones:
```
usage: parser [-h] [-a] [-z] [-p] [-d] [-u] [-c]

Scraper de la web pisos.com (Mallorca)

options:
  -h, --help          show this help message and exit
  -a, --all           Importa todo
  -z, --zones         Importa las zonas de Mallorca.
  -p, --previews      Importa datos básicos de los anuncios
  -d, --details       Importa los detalles de los anuncios.
  -u, --unemployment  Importa el paro registrado por municipios.
  -c, --csv           Crea un csv con los resultados.
```

