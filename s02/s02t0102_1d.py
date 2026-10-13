#importando el modulo array de 
# la biblioteca array 
from array import array as arr 

def print_array(imput):
    print("[", end="")
    for element in imput:
        print(element, end=", ")
    print("\b]")

my_array = arr('i', [10,22,300,3,7,10,22,42,32,17])
print_array(my_array)

#buscar el elemento 42 en el arreglo
num_to_search = 42
counter = 0
for integer in my_array:
    if integer == num_to_search:
        print("Número encontrado")
        #sirve para terminar el ciclo for
        break
    
    counter += 1
    if counter == len(my_array):
        print("Número no encontrado")