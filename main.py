
from collections import Counter
#Función que compara los valores repetidos

#la siguiente lista es temporal, para efectos de comprobar el funcionamiento del algoritmo
#los mintérminos insertados son sumatoria de m(1,3,4,5,9,11,12,13,14,15)

list_to_compare= [[1,0,0,0,1],[3,0,0,1,1],[4,0,1,0,0],[5,0,1,0,1],[9,1,0,0,1],[11,1,0,1,1],[12,1,1,0,0],[13,1,1,0,1],[14,1,1,1,0],[15,1,1,1,1]]

for value in list_to_compare:
    print(value)

#función para agrupar en términos de 1's

def compare(list_to_compare):
    sorted_dict={} #en el diccionario agruparemos por cantidad de 1's

    for values in list_to_compare: 
        consider=values[1:5] #el término cero es el valor del mintérmino, por eso se ignora 
        counter = Counter(consider) #el counter nos indica la cantidad de ceros que hay en la lista

        if counter[1] not in sorted_dict:
            sorted_dict[counter[1]]=[values]
        elif counter[1] in sorted_dict:
            new_list= sorted_dict[counter[1]]
            new_list.append(values)
            sorted_dict[counter[1]]=new_list
        else:
            print("Algún valor está fuera de índice o no es número") #esta validación nos permite observar en la terminal si el algoritmo no está siendo ejecutado correctamente
    
    print(sorted_dict)

    return 0 #recodar retirar el cero y enviar esta expresión al próximo paso del algoritmo


compare(list_to_compare)

def compare_groups(groups_to_compare):
    return 0