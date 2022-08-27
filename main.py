
from collections import Counter
#Función que compara los valores repetidos

#la siguiente lista es temporal, para efectos de comprobar el funcionamiento del algoritmo
#los mintérminos insertados son sumatoria de m(1,3,4,5,9,11,12,13,14,15)

list_to_compare= [[1,0,0,0,1],[3,0,0,1,1],[4,0,1,0,0],[5,0,1,0,1],[9,1,0,0,1],[11,1,0,1,1],[12,1,1,0,0],[13,1,1,0,1],[14,1,1,1,0],[15,1,1,1,1]]

for value in list_to_compare:
    #print(value)
    pass

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

    return sorted_dict 




#la siguiente función comparará los grupos previamente ordenados por cantidad de 1s


    #con el fin de poder agrupar correctamente los términos que tienen diferencias 
    #es necesario crear una lista con listas, primera lista contiene los mintérminos, segunda lista contiene los binarios
    #segunda lista, tiene otra lista interna con los binarios separados ejm lista=[[[1,3],[1,0,0,1],[0,1,1,0]]]
  


def compare_groups2(groups_to_compare):
    comparison_keys=list(groups_to_compare.keys())
    groups=[]
    
    for position in range(0,len(comparison_keys)-1):

        key=comparison_keys[position]
        next_key=comparison_keys[position+1]

        diff_count=0
        diff_position=None
        
        for i in range(0,len(groups_to_compare[key])):
            
            upper_comparison=groups_to_compare[key][i]
            lower_comparison=groups_to_compare[next_key]


            for j in range(0,len(groups_to_compare[next_key])):

                lower_comparison=list(lower_comparison)
                print(upper_comparison, lower_comparison[j])
                diff_count=0
                for k in range (1,5):
                    #print(upper_comparison[k],lower_comparison[j][k])

                    if (upper_comparison[k]) is not (lower_comparison[j][k]):
                        print(upper_comparison[k],lower_comparison[j][k],'this')
                        diff_count+=1
                        diff_position=k
                    
                if diff_count==1:
                    x_insert=list(lower_comparison[j])
                    x_insert[diff_position]='x'
                    groups.append([[upper_comparison[0],lower_comparison[j][0]],x_insert]) 


    print("gr to com",groups_to_compare)
    for i in groups:
        print(i)
    print(groups)




            




        

compare_groups2(compare(list_to_compare))