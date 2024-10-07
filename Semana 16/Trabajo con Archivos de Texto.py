
# Escritura de Archivo de Texto

# Escribimos al menos tres líneas de notas personales
contenido = [
    "L1: Hoy aprendi a trabajar con archivos en Python.\n",
    "L2: Me siento mas comodo Y Feliz con la programacion.\n",
    "L3: Seguire practicando para mejorar mis habilidades en programacion.\n"
]
# Ruta del archivo
nueva_ruta = "C:/Users/Yelena Pc/PycharmProjects/Yelenasu/Semana 16/my_notes.txt"

# Abrimos el archivo en modo escritura ('w') y escribimos el contenido línea por línea
with open(nueva_ruta, 'w') as archivo:
    archivo.writelines(contenido)  # Escribimos todas las líneas del contenido

# Lectura de Archivo de Texto

# Abrimos el archivo nuevamente en modo lectura ('r')
with open(nueva_ruta, 'r') as archivo:
    # Leemos el contenido línea por línea utilizando un bucle
    linea = archivo.readline()
    while linea:  # Mientras haya líneas por leer
        print(linea.strip())  # Mostramos cada línea (strip() elimina saltos de línea innecesarios)
        linea = archivo.readline()  # Leemos la siguiente línea

# El archivo se cierra automáticamente al salir del bloque 'with'

