# echoes-drive-utility
Cómo ejecutar este programa (comprobado su funcionamiento en Ubuntu y Windows 7 y 10 64 bits)

1. Descargar e instalar Python (2.6 o posterior): https://www.python.org/downloads/
2. Instalar la librería de Google para su API: https://developers.google.com/api-client-library/python/start/installation
3. Abrir Echoes y hacer click en la pestaña "ABOUT". Ahí verás el directorio de trabajo que está siendo utilizado.
4. Volver a la carpeta del programa, abrir el fichero "configuración.txt", introducir la ruta al directorio de trabajo y guardar.
5. Por último desde la consola ejecutar el módulo principal con la instrucción: python main.py

Después de esto esto se abrirá en tu navegador una página en la que se te pide que inicies sesión en tu cuenta de Gmail y hecho esto la aplicación solicita que le des permiso de acceso y edición al Drive de la cuenta en que iniciaste sesión. Una vez hecho esto se descargará un archivo token.json que te dará acceso permanente sin volver a solicitar permisos cada vez que ejecutes el script.
