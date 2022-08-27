
from collections import Counter
#Función que compara los valores repetidos

#la siguiente lista es temporal, para efectos de comprobar el funcionamiento del algoritmo
#los mintérminos insertados son sumatoria de m(1,3,4,5,9,11,12,13,14,15)

list_to_compare= [[1,0,0,0,1],[3,0,0,1,1],[4,0,1,0,0],[5,0,1,0,1],[9,1,0,0,1],[11,1,0,1,1],[12,1,1,0,0],[13,1,1,0,1],[14,1,1,1,0],[15,1,1,1,1]]
list_to_compare=[[0,0,0,0,0,0],[1,0,0,0,0,1],[2,0,0,0,1,0],[3,0,0,0,1,1],[4,0,0,1,0,0],[8,0,1,0,0,0],[10,0,1,0,1,0],[13,0,1,1,0,1],[14,0,1,1,1,0],[15,0,1,1,1,1],[17,1,0,0,0,1],[23,1,0,1,1,1],[24,1,1,0,0,0],[26,1,1,0,1,0],[27,1,1,0,1,1],[28,1,1,1,0,0],[31,1,1,1,1,1]]

for value in list_to_compare: #ciclo temporal para analizar comparaciones desde la terminal
    #print(value)
    pass

#función para agrupar en términos de 1's

def compare(list_to_compare):
    sorted_dict={} #en el diccionario agruparemos por cantidad de 1's

    for values in list_to_compare: 
        max_position=len(list_to_compare[0])
        consider=values[1:max_position] #el término cero es el valor del mintérmino, por eso se ignora
        #max position se define según la cantidad de bits en la expresión, ya que estos cambian según lo insertado a la función
        counter = Counter(consider) #el counter nos indica la cantidad de ceros que hay en la lista

        if counter[1] not in sorted_dict: #si aún no existe la llave de la cantidad de 1s, se crea
            sorted_dict[counter[1]]=[values]
        elif counter[1] in sorted_dict: #si ya existe la llave en el diccionario, se accede al value y se le agrega a la lista el binario
            new_list= sorted_dict[counter[1]]
            new_list.append(values)
            sorted_dict[counter[1]]=new_list
        else:
            print("Algún valor está fuera de índice o no es número") #esta validación nos permite observar en la terminal si el algoritmo no está siendo ejecutado correctamente
    
    print(sorted_dict)

    return sorted_dict 

#la siguiente función comparará los grupos previamente ordenados por cantidad de 1s

    #con el fin de poder agrupar correctamente los términos que tienen diferencias 
    #es necesario crear una lista con listas, primera lista contiene los mintérminos, segunda lista contiene los binarios
    #segunda lista, tiene otra lista interna con los binarios separados ejm lista=[[[1,3],[1,0,0,1],[0,1,1,0]]]
  
def compare_groups(groups_to_compare):
    comparison_keys=list(groups_to_compare.keys()) #lista con todas las llaves existentes según cantidad de 1s
    #no se puede ciclar de 1 en 1 porque si no existe un grupo con 2 1s el ciclo se cae, es necesario tener explícitamente los grupos existentes
    groups=[]
    max_position=len(list_to_compare[0]) #dado que la cantidad de bits cambia por cantidad de mintérminos, el programa debe ser responsivo y ciclar hasta la cantidad de bits existentes
    for position in range(0,len(comparison_keys)-1): #accedemos a cada key

        key=comparison_keys[position]
        next_key=comparison_keys[position+1]

        diff_count=0
        diff_position=None
        
        for i in range(0,len(groups_to_compare[key])): #accedemos a cada value
            
            upper_comparison=groups_to_compare[key][i] #almacena el bit del mintérmino a analizar
            lower_comparison=groups_to_compare[next_key] #almacena el bit del siguiente mintérmino a analizar


            for j in range(0,len(groups_to_compare[next_key])): #accedemos a cada lista en el value

                lower_comparison=list(lower_comparison) 
                print(upper_comparison, lower_comparison[j]) 
                diff_count=0
                for k in range (1,max_position): #accedemos a cada bit en la lista
                    #print(upper_comparison[k],lower_comparison[j][k])

                    if (upper_comparison[k]) is not (lower_comparison[j][k]): #compara si los bits son iguales o no
                        diff_count+=1
                        diff_position=k
                    
                if diff_count==1: #si solo existe una diferencia en la misma posición, se almacena con una X el valor y se agrega a la nueva lista
                    x_insert=list(lower_comparison[j])
                    x_insert[diff_position]='x'
                    groups.append([[upper_comparison[0],lower_comparison[j][0]],x_insert]) 

    for i in groups: #ciclo temporal para observar los mintérminos comparados en la terminal
        print(i)
    print(groups)

compare_groups(compare(list_to_compare))