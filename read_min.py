#Funcion para abrir y leer el archivo de texto

#Con el comando "with" se utiliza para que el archivo se cierre una vez que se termina de utilizar el mismo.
#Se abre el archivo como file para que a la hora de realizar 
minterms=""
literals=""
def read_lit():
    with open("list.txt","r") as mt:
        literals = int(mt.readline(1))
    return literals

def read():
    with open("list.txt","r") as mt:
        minterms = mt.readlines(2)
        minterms=minterms[1]
        minterms=minterms.split(',')

        final=[]
        
        for i in minterms:
            final.append((int(i)))
        
        minterms=final
        print(minterms)
        return minterms

txt_minterms=read()
txt_literals=read_lit()

print(txt_literals)








