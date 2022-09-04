minterms=[0, 1, 2, 3, 4, 8, 10, 13, 14, 15, 17, 23, 24, 26, 27, 28, 31,32] # ejemplo
literals=6
def converse_bin(minterms):
        
    list_bin_str = []  # esta lista nos va a dar los binarios en str      
    list_bin_int = []  # esta lista nos convierte list_bin_str en minteros
    list_minterms = [] # Aqui lo agregamos a una matriz
    
    for i in minterms:      
        list_bin_str += (format(i, "b"))
        list_bin_int = list(map(int, list_bin_str))
        list_minterms.append(list_bin_int)
        list_bin_str = [] #se debe limpiar esta variable
        
    return add_minterms(list_minterms, minterms)

def add_minterms(list_minterms, minterms): #funcion para agregar el mintermino a la matriz
    
    for i in range(0, len(list_minterms)): 
        n = 0 # condicion que me entra al while - bandera - true
        while n < 1: 
            n += 1  # condicion que me saca del while - bandera - false
            list_minterms[i].insert(0,minterms[i])

    print(list_minterms)

    return list_minterms

def add_zeros(bins):

    for i in range(0, len(bins)):
            while len(bins[i])<=literals:
                        bins[i].insert(1,0)
    
    return bins
print(minterms)


print(add_zeros(converse_bin(minterms)))
