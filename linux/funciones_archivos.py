import os, io, pickle

def comprobarCambios(ruta, nom_fichero):
	
	#Adquisicion de los datos registrados de la carpeta
	lista_cambios = []
	lista_actual = os.listdir(ruta)
	lista_guardada = leerFichero(nom_fichero)
	#Comprobacion de los cambios en el directorio
	for i in lista_actual:
		if not i in lista_guardada:
			lista_cambios.append(i)
		else:
			continue
	return lista_cambios

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

def leerFichero(nom_fichero):
	fichero = open(nom_fichero, "ab+")
	if os.path.getsize(nom_fichero) > 0:
		fichero.seek(0)
		lista_guardada=pickle.load(fichero)
		fichero.close()
	return lista_guardada

def guardarEnFichero(lista, nom_fichero):
    f = open(nom_fichero,"wb")
    pickle.dump(lista,f)
    f.close()