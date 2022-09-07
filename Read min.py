#Funcion para abrir y leer el archivo de texto

#Con el comando "with" se utiliza para que el archivo se cierre una vez que se termina de utilizar el mismo.
#Se abre el archivo como file para que a la hora de realizar 
minterms=""

with open("list.txt","r") as mt:
    literals = mt.readline(1)
    minterms = mt.readlines(2)
    minterms=minterms[1]
    minterms=list(minterms)

    final=[]
    
    for i in minterms:
        if i!=",":
            final.append(format(int(i)))

print(literals,"\n",minterms)
"""
for i in minterms:
    bin = format(int(i), "b")
    print('El mintermino es: ', i,'Equivale a: ',bin)

"""
"4,23,64"
"4 a binario, un append a la lista entonces queda [mintérmino, lista de binarios]"
"bin(4)"











