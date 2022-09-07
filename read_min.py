#Funcion para abrir y leer el archivo de texto

#Con el comando "with" se utiliza para que el archivo se cierre una vez que se termina de utilizar el mismo.
#Se abre el archivo como file para que a la hora de realizar 
minterms=""

def read():
    with open("list.txt","r") as mt:
        literals = mt.readline(1)
        minterms = mt.readlines(2)
        minterms=minterms[1]
        minterms=minterms.split(',')

        final=[]
        
        for i in minterms:
            final.append((int(i)))
        
        minterms=final
        print(minterms)
        return minterms

read()









