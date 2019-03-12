from cliente_GDrive.prueba_api_Drive import*
from escaneador import escaneo
import io, os
import threading
import time

def tipoArchivo(nombre_archivo):
	i = nombre_archivo.find(".")
	formato = nombre_archivo[i:len(nombre_archivo)]
	switcher = {
		'.html': 'text/html',
		'.csv': 'text/csv',
		'.jpg': 'image/jpeg',
		'.png': 'image/png',
	}
	tipo = switcher.get(formato, None)
	return tipo

class Observador(threading.Thread):
	permiso_acceso = threading.Event() #Necesario para evitar un posible acceso simultáneo al registro
	__stop = False
	__archivos_a_subir = []
	__ruta = ""
	__nombre_fichero = ""

	def __init__(self,ruta_dir, nom_fichero):
		threading.Thread.__init__(self)
		self.__ruta = ruta_dir
		self.__nombre_fichero = nom_fichero
	def start(self):
		#self.permiso_acceso.set()
		threading.Thread.start(self)
	def run(self):
		while not self.__stop:
			self.permiso_acceso.wait()
			self.__archivos_a_subir = escaneo(self.__ruta,self.__nombre_fichero)
			if self.__archivos_a_subir:
				self.permiso_acceso.clear() #Porque ahora el hilo principal pasará a trabajar con el fichero
			else:
			time.sleep(1)   
	def cerrar(self):
		self.__stop=True
	def getArchivos(self):
		return self.__archivos_a_subir

miCliente = interfazGDrive()

archivos_a_subir = []
#Configuración de inicio
f= open("configuracion.txt","r")
ruta = f.read()
f.close()
if not os.path.exists(ruta):
	print("La ruta expecificada en el fichero de\
	 configuración no existe")
	exit()
miObservador = Observador(ruta, "registro_drive")
miObservador.start()
miObservador.permiso_acceso.set()
time.sleep(4)
miObservador.cerrar()
miObservador.join()

'''while True:
	if not miObservador.permiso_acceso.is_set():
		archivos_a_subir = miObservador.getArchivos()
		cont=1
		for i in archivos_a_subir:
			ruta_archivo = os.path.join(ruta,i)
			miCliente.subirArchivo(i, ruta_archivo, tipoArchivo(i))
			print("[" + str(cont) + "]-" +i + ": subido.")
			cont+=1
		#Registra los cambios
		miCliente.registrarListaArchivos(miCliente.getListaArchivos(), "registro_drive")
		
		#Vuelve a ceder el control al observador
		miObservador.permiso_acceso.set()
	else:
		print("[Principal]: el observador no ha notificado cambios.")	
		'''