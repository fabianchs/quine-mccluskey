
from collections import Counter
#Función que compara los valores repetidos

#la siguiente lista es temporal, para efectos de comprobar el funcionamiento del algoritmo
#los mintérminos insertados son sumatoria de m(1,3,4,5,9,11,12,13,14,15)

list_to_compare= [[1,0,0,0,1],[3,0,0,1,1],[4,0,1,0,0],[5,0,1,0,1],[9,1,0,0,1],[11,1,0,1,1],[12,1,1,0,1],[13,1,1,0,1],[14,1,1,1,0],[15,1,1,1,1]]

for value in list_to_compare:
    print(value)

#función para agrupar en términos de 1

def compare(list_to_compare):
    zeros_count=1
    sorted_dict={}

    for values in list_to_compare:
     
        counter = Counter(values)
        print(counter)
            
    
    sorted_dict[str(zeros_count)]="insert sorted values"

    return 0


compare(list_to_compare)