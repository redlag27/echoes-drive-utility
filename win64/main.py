from cliente_GDrive.prueba_api_Drive import*
from funciones_archivos import* 
import time

#Configuración de inicio
miCliente = interfazGDrive()

f= open("configuracion.txt","r")
ruta = f.read()
f.close()
nom_fichero = "registro_drive"
if not os.path.exists(ruta):
	print("La ruta expecificada en el fichero de\
	 configuración no existe")
	exit()
#Guarda los datos de GDrive en el fichero local al principio del programa
lista_archivos= miCliente.getListaArchivos()
guardarEnFichero(lista_archivos, nom_fichero)

#Ciclo principal
while True:	
	archivos_a_subir = comprobarCambios(ruta, nom_fichero)
	if archivos_a_subir:
		print("Se subirán estos archivos: ")
		print(archivos_a_subir)
		#Sube cada archivo de la lista a Drive
		for i in archivos_a_subir:
			ruta_archivo = os.path.join(ruta,i)
			miCliente.subirArchivo(i, ruta_archivo, tipoArchivo(i))
			print(str(archivos_a_subir.index(i)+1) + ") " +i + ": subido.")
		#Registra los cambios en el fichero
		lista_archivos += archivos_a_subir
		guardarEnFichero(lista_archivos, nom_fichero)
		print("Archivos registrados con éxito")
		archivos_a_subir.clear()
	else:
		print("No hay nuevos archivos para subir.")
		time.sleep(2.5)