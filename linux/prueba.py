def tipoArchivo(nombre_archivo):
	i = nombre_archivo.find(".")
	formato = nombre_archivo[i:len(nombre_archivo)]
	print("El formato es: " + formato)
	switcher = {
		'.html': 'text/html',
		'.csv': 'text/csv',
		'.jpg': 'image/jpeg',
		'.png': 'image/png',
		'.plt': 'unknown'
	}
	tipo = switcher.get(formato, "unknown")
	return tipo

print(tipoArchivo("pene.png"))