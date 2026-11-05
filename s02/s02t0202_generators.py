"""
generators

los generadores son funciones que pueden
pausar en ejecucion

cuando se invoca un funcion generadora
devuelve un objeto generador (aka iterador)

el codigo dentro de la funcion no se ejecuta 
de imediato, solo se compila.

la funcion se ejecuta unicamente cuando
iteras sobre el generador

"""

def my_generador():
    yield 1
    yield 2
    yield 3 
    yield 4
    yield 1
    yield 2
    yield 3 
    yield 4
    yield 1
    yield 2
    yield 3 
    yield 4
    yield 1
    yield 2
    yield 3 
    yield 4
    
print(list(my_generador()))

#se invoca funcion genreadora
my_iterator = my_generador()

# se itera manualmente sobre el generador
#print(next(my_iterator)) #imprime 1
#print(next(my_iterator)) #imprime 2
#print(next(my_iterator)) #imprime 3
#print(next(my_iterator)) #imprime 4

for value in my_iterator: 
    print(value)
