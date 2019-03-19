# -*- coding utf-8 -*-

from cliente_GDrive.prueba_api_Drive import*
from funciones_archivos import* 
import properties
ruta = properties.path

import os
import inotifyx
import time

#Configuracion de inicio
miCliente = interfazGDrive()
nom_fichero = "registro_drive"

if not os.path.exists(ruta):
	print("La ruta expecificada en el fichero de configuracion no existe.")
	exit()

#Guarda los datos de GDrive en el fichero local al principio del programa
lista_archivos= miCliente.getListaArchivos()
guardarEnFichero(lista_archivos, nom_fichero)

#Ciclo principal
fd = inotifyx.init()
while True:
	try:
		wd = inotifyx.add_watch(fd, ruta, inotifyx.IN_CREATE)
		events = inotifyx.get_events(fd)
		archivos_a_subir = comprobarCambios(ruta, nom_fichero)
		if archivos_a_subir:
			print("Se subiran estos archivos: ")
			print(archivos_a_subir)
			#Sube cada archivo de la lista a Drive
			for i in archivos_a_subir:
				ruta_archivo = os.path.join(ruta,i)
				miCliente.subirArchivo(i, ruta_archivo, tipoArchivo(i))
				print(str(archivos_a_subir.index(i)+1) + ") " +i + ": subido.")
			#Registra los cambios en el fichero
			lista_archivos += archivos_a_subir
			guardarEnFichero(lista_archivos, nom_fichero)
			print("Archivos registrados con exito")
			del archivos_a_subir[:]
		else:
			continue
	except KeyboardInterrupt:
		break

	#finally:
	#	os.close(fd)
os.close(fd)