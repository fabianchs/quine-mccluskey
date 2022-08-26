#Funcion para abrir y leer el archivo de texto

#Con el comando "with" se utiliza para que el archivo se cierre una vez que se termina de utilizar el mismo.
#Se abre el archivo como file para que a la hora de realizar 
with open("list.txt") as file:
    min = file.read()
    print(min)

max = min
for index in range ( len ( max ) ):
    if max[index] != ",":
        print ( max[index])

 