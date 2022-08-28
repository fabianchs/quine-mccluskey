#Funcion para abrir y leer el archivo de texto

#Con el comando "with" se utiliza para que el archivo se cierre una vez que se termina de utilizar el mismo.
#Se abre el archivo como file para que a la hora de realizar 

"""
with open("list.txt") as mt:
    minterms = mt.read().split(',')

print(minterms)
for i in minterms:
    bin = format(int(i), "b")
    print('El mintermino es: ', i,'Equivale a: ',bin)

"""
"4,23,64"
"4 a binario, un append a la lista entonces queda [mintérmino, lista de binarios]"
"bin(4)"

literals=7
minterms=[[4,0,1,0,0],[23,1,0,1,1,0],[64,1,0,0,0,0,0,0]]

print (minterms)

for i in range(0, len(minterms)):
            while len(minterms[i])<=literals:
                        minterms[i].insert(1,0)
            
print(minterms)









