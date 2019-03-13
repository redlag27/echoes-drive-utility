# echoes-drive-utility
Cómo ejecutar este programa (comprobado su funcionamiento en Ubuntu y Windows 7 y 10 64 bits)

1. Descargar e instalar Python (2.6 o posterior): https://www.python.org/downloads/
2. Instalar la librería de Google para su API: https://developers.google.com/api-client-library/python/start/installation
3. Abrir Echoes y hacer click en la pestaña "ABOUT". Ahí verás el directorio de trabajo que está siendo utilizado.
4. Volver a la carpeta del programa, abrir el fichero "configuración.txt", introducir la ruta al directorio de trabajo y guardar.
5. Por último desde la consola ejecutar el módulo principal con la instrucción: python main.py

Se abrirá en tu navegador una página en la que se te pide que inicies sesión en tu cuenta de Gmail (más bien cuenta de gmail del proyecto) y hecho esto la aplicación solicita que le des permiso de acceso y edición al Drive de dicha cuenta. Después se descargará un archivo token.json que se guardará en la carpeta del programa y que sirve para darte acceso permanente sin volver a solicitar permisos cada vez que ejecutes el script.

Programa en desarrollo (supongo que sobra decirlo (?) )
