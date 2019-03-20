# echoes-drive-utility
Cómo ejecutar este programa (comprobado su funcionamiento en Ubuntu y Windows 7 y 10 64 bits)

1. Descargar e instalar Python (2.7 o >3.6): https://www.python.org/downloads/
2. Instalar pip: https://pip.pypa.io/en/latest/installing/
3. Instalar la librería de Google para su API: https://developers.google.com/api-client-library/python/start/installation
4. Instalar inotify_simple para python: https://pypi.org/project/inotify_simple/
5. Abrir Echoes y hacer click en la pestaña "ABOUT". Ahí verás el directorio de trabajo que está siendo utilizado.
6. Volver a la carpeta del programa, abrir el fichero "properties.py" e introducir la ruta del directorio de trabajo en la variable path y guardar.
7. Desde la consola ejecutar el módulo principal (main2.py para Raspberry, el otro no funcionará en Arch (se encuentra en proceso de desarrollo)) con la instrucción: python main.py/main2.py

Y listo. Los archivos nuevos que aparezcan en el directorio se subirán automáticamente a la carpeta de Google Drive.

