print("")#imprime el espacio en blanco 
print("Martinez Tagle Luis Angel 3w 1196 este es el programa 4: Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono ")#imprime el nombre del programador  y titulo del programa 
print("")#imprime el espacio en blanco 

# Pedir al usuario que ingrese su nombre, edad, dirección y teléfono
nombre = input(" Carnalito Por favor, ingresa tu nombre o si no vas a ver: ")
edad = input("echame la mano y Ingresa tu edad : ")
direccion = input("Ingresa tu dirección, calmado no te voy a robar: ")
telefono = input("Ingresa tu número de teléfono precios@: ")

# Crear un diccionario con la información proporcionada
informacion_usuario = {
    "nombre": nombre,
    "edad": edad,
    "dirección": direccion,
    "teléfono": telefono
}

# Mostrar la información por pantalla
print(f"{informacion_usuario['nombre']} tiene {informacion_usuario['edad']} años, vive en {informacion_usuario['dirección']} y su número de teléfono es {informacion_usuario['teléfono']}.")
