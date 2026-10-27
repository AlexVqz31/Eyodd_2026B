# git push origin main

from array import array as arr 
#importando una funcion de otro archivo
from s02t0102_1d import print_array

my_array = arr('i', [10,20,30,40,50,60,70,80, 90,100])

print("---ANTES DE LA ELIMINACION---")
print_array(my_array)
print("________________________________")
# elimuinacion 

try :
    my_array.remove(5)
except ValueError:
    print("El elemento no se encuentra en el arreglo")
print("---DESPUES DE LA ELIMINACION---")
print_array(my_array)

