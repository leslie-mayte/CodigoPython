#Abrir un archivo
miArchivo = open("miArchivo.txt","w")

#Obetener informacion de esre archivo
print("Name:", miArchivo.name)
print("esta cerrado:", miArchivo.closed)
print("modo abierto:", miArchivo.mode)

#Escribir algo al archivo
miArchivo.write ("Me encanta Python")
miArchivo.write("Me encanta Disney")
miArchivo.close()

#Agregar el archivo
miArchivo = open("miArchivo.txt","a")
miArchivo.write("y tambien c++")

