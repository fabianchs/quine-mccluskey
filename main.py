
from collections import Counter
#Función que compara los valores repetidos

#la siguiente lista es temporal, para efectos de comprobar el funcionamiento del algoritmo
#los mintérminos insertados son sumatoria de m(1,3,4,5,9,11,12,13,14,15)

list_to_compare= [[1,0,0,0,1],[3,0,0,1,1],[4,0,1,0,0],[5,0,1,0,1],[9,1,0,0,1],[11,1,0,1,1],[12,1,1,0,0],[13,1,1,0,1],[14,1,1,1,0],[15,1,1,1,1]]

for value in list_to_compare:
    print(value)

#función para agrupar en términos de 1's

def compare(list_to_compare):
    sorted_dict={}

    for values in list_to_compare:
        consider=values[1:5]
        counter = Counter(consider)

        if counter[1] not in sorted_dict:
            sorted_dict[counter[1]]=[values]
        elif counter[1] in sorted_dict:
            new_list= sorted_dict[counter[1]]
            new_list.append(values)
            sorted_dict[counter[1]]=new_list
    
    print(sorted_dict)



    return 0


compare(list_to_compare)