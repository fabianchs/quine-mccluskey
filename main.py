
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
def compare_groups(groups_to_compare):
    key_to_compare=1
    quant_of_comparisons=list(groups_to_compare.keys()) #no se puede ir de 1 en 1 con la cantidad de ceros
    #porque puede existir una expresión que no tenga 2 unos
    print (quant_of_comparisons,"HERE")
    groups=[]

    for i in quant_of_comparisons:
        for group in groups_to_compare[i]:
            #estamos recorriendo los de la cant de 1s
            print(i,"group")
            actual_bin_position=group[1:5]
            
            for row in groups_to_compare[quant_of_comparisons[i-1]]:
                diff_count=0
                diff_position=None
                consider_from_row=row[1:5]

                if True:
               
                    for position in range(0,3):
                        if consider_from_row[position]!=actual_bin_position[position]:
                            diff_count+=1
                            diff_position=position
                        
                    if diff_count==1:
                        insert=consider_from_row
                        insert[position]='x'
                        groups.append([[group[0],row[0]],insert])
                        diff_count=0
                        diff_position=None



                
                #if i==quant_of_comparisons[0]:
                 #   print("salto",i,quant_of_comparisons[0])
                #else:
                 #   consider= row[1:5]
                  #  print(consider,"row")
                #print(set(row).difference(set(groups_to_compare[key_to_compare+2]))) #retorna la cantidad de diferencias entre los binarios
                #llave 1 la comparamos con grupo de llave siguiente 
        print("group change")
        key_to_compare+=1
        print(groups)
    #con el fin de poder agrupar correctamente los términos que tienen diferencias 
    #es necesario crear una lista con listas, primera lista contiene los mintérminos, segunda lista contiene los binarios
    #segunda lista, tiene otra lista interna con los binarios separados ejm lista=[[[1,3],[1,0,0,1],[0,1,1,0]]]
  

    return 0

compare_groups(compare(list_to_compare))