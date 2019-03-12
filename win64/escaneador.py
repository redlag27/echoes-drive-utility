import os, io, pickle
import time

def escaneo(ruta, nombre_archivo):
	
	#Adquisición de los datos registrados de la carpeta
	lista_cambios=[]
	lista_actual = os.listdir(ruta)
	fichero = open(nombre_archivo, "rb")

	if os.path.getsize(nombre_archivo) > 0:
		lista_guardada=pickle.load(fichero)
		fichero.close()
		#Comprobaación de los cambios en el directorio
		for i in lista_actual:
			if i in lista_guardada:
				continue
			else:
				lista_cambios.append(i)
	time.sleep(1)
	return lista_cambios

	