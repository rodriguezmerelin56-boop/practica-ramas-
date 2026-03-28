# crear archivo_ejemplo.py


# Crear y escribir en un archivo
with open("datos.txt", "w") as archivo:
    archivo.write("Nombre: Jose \n")
    archivo.write("Edad: 30\n")
    archivo.write("País: República Dominicana\n")

print("Archivo creado y datos guardados correctamente.")

# Leer el archivo
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()

print("\nContenido del archivo:")
print(contenido)

