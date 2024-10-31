print("")#imprime el espacio en blanco 
print("Martinez Tagle Luis Angel 3w 1196 este es el programa 2: nos da  los créditos de las asignaturas de un curso  ")#imprime el nombre del programador  y titulo del programa 
print("")#imprime el espacio en blanco 


creditos_asignaturas = {'Ecosistemas': 5, 'Metodologias': 9, 'Programacion ': 10}  # Definir el diccionario con los créditos de las asignaturas

# Mostrar los créditos de cada asignatura
for asignatura, creditos in creditos_asignaturas.items():
    print(f"{asignatura} tiene {creditos} créditos")

# Calcular el número total de créditos del curso
total_creditos = sum(creditos_asignaturas.values())
print(f"El número total de los  créditos del curso es: {total_creditos}")