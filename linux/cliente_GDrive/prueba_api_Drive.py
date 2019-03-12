from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient.http import MediaFileUpload
import pickle

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/drive'

class interfazGDrive():
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('drive', 'v3', http=creds.authorize(Http()))

    def crearDirectorio(self,nombre_directorio):
        pass
        
    def subirArchivo(self, nombre_archivo, ruta, tipo_archivo):
    #Sube un archivo determinado a Google Drive
        file_metadata = {'name': nombre_archivo}
        media = MediaFileUpload(ruta, mimetype= tipo_archivo)
        file = self.service.files().create(body=file_metadata,\
            media_body=media, fields='id').execute()
        #return file

    def getListaArchivos(self):
        results = self.service.files().list(fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])
        lista_archivos = []
        if not items:
            return
        else: 
            for item in items:
                lista_archivos.append(item['name'])
            return lista_archivos
'''
ruta= 'C:/Users/servinet/Downloads/foto.jpg'
miInterfaz=interfazGDrive()
miInterfaz.subirArchivo('foto.jpg', ruta, 'image/jpeg')
print(miInterfaz.getListaArchivos())
'''


