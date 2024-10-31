print("")#imprime el espacio en blanco 
print("Martinez Tagle Luis Angel 3w 1196 este es el programa 1: almacena las asignaturas de un curso  ")#imprime el nombre del programador  y titulo 
print("")#imprime el espacio en blanco 

# Crear una lista con las asignaturas del curso
asignaturas = ["formacion civica y etica", "educacion fisica  ", "ciencias naturales ", "historia ", "español  "]


notas = {}     # Crear un diccionario para almacenar las notas de cada asignatur

# Pedir al usuario la nota de cada asignatura
for asignatura in asignaturas:
    nota = float(input("Ingresa la nota de " + asignatura + ": "))
    notas[asignatura] = nota

# Eliminar las asignaturas aprobadas de la lista
for asignatura, nota in notas.items():
    if nota >= 5.0:
        asignaturas.remove(asignatura)


print("Las asignaturas que el muchachon debe repetir son las que vera a continuacion :( :") # Mostrar las asignaturas que el usuario tiene que repetir
for asignatura in asignaturas:
    print(asignatura)


