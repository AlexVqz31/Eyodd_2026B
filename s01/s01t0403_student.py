
"""
NOTAS
identifico el tamaño de la entrada "n"
el tamaño de la entrada es el numero de estudiantes
2. es ver cuanto crece el numero de operaciones
en mi algoritmo conforme
crece el tamño de entrada
agrego las bigO identificadas
tenindo en cuenta la cota superior asinotica
O(n) + O(4) = O(n+4) = O(n)

"""

student_list_01 = ['jordan','ana','alejo','jessica']
student_list_02 = ['santiago','demian','fernando','paulina']

#verificando presencia de estudiante
def check_student(input_student, student_list):
    for student in student_list:
      if input_student == student:
        print("estudiante encontrado")
        return student 

    #si no encuentr o al estudiante 
    print("estudiante no encontrado")
    return None 
# probando
check_student("ana",student_list_01)   