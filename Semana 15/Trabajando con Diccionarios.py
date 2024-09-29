# Crear un Diccionario
informacion_personal = {
    "nombre": "Elias Arriaga",
    "edad": 18,
    "ciudad": "Cuenca",
    "profesion": "Ingeniero"
}

# Acceder y Modificar Valores
# Accedemos al valor asociado con la clave "ciudad"
print("Ciudad original:", informacion_personal["ciudad"])

# Modificamos la ciudad
informacion_personal["ciudad"] = "Ambato"
print("Ciudad modificada:", informacion_personal["ciudad"])

# Agregar una nueva clave-valor para "profesion"
informacion_personal["profesion"] = "Medico"

# Verificar Existencia de Claves
if "telefono" not in informacion_personal:
    # Si no existe, la agregamos con un número ficticio
    informacion_personal["telefono"] = "0988754789"

# Eliminar una Clave
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el Diccionario Final
print("Diccionario final:", informacion_personal)

#Añadimos un for para indexar los valores y que muestren su clave y su valor
for index, (clave, valor) in enumerate(informacion_personal.items()):
    print(f"{index}: {clave} -> {valor}")