import pickle

nom_fichero = "registro_drive"

texto = "pepe.jpg"
f = open(nom_fichero,"wb")
#f.seek(0)
pickle.dump(texto,f)
f.close()

f = open(nom_fichero,"ab+")
f.seek(0)
lista_leida = pickle.load(f)
f.close()
print(lista_leida)
