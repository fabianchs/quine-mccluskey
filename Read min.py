#Funcion para abrir y leer el archivo de texto

#Con el comando "with" se utiliza para que el archivo se cierre una vez que se termina de utilizar el mismo.
#Se abre el archivo como file para que a la hora de realizar 

with open("list.txt") as mt:
    minterms = mt.read().split(',')

print(minterms)
for i in minterms:
    bin = format(int(i), "b")
    print('El mintermino es: ', i,'Equivale a: ',bin)











