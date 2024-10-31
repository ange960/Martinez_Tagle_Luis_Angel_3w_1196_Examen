print("")#imprime el espacio en blanco 
print("Martinez Tagle Luis Angel 3w 1196 este es el programa 3: pregunta al usuario la nota que ha sacado en cada asignatura")#imprime el nombre del programador  y titulo del programa 
print("")#imprime el espacio en blanco 


asignaturas = ["formacion civica y etica", "programacion ", "ecosisitemas ", "Historia", "Lengua"]  # Lista de asignaturas


notas = []  # Inicializar una lista para las notas

# Preguntar al usuario por la nota de cada asignatura
for asignatura in asignaturas:
    nota = input(f"Ingrese la nota que has sacado en {asignatura}: ")
    notas.append(nota)

# Mostrar las notas por pantalla
for i in range(len(asignaturas)):
    print(f"En {asignaturas[i]} has sacado {notas[i]}")
