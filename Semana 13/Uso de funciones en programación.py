# Definir la Función
def calcular_promedio_ciudades(datos_temperaturas):
    promedios = {}

    for ciudad, semanas in datos_temperaturas.items():
        total_temperaturas = 0
        cantidad_temperaturas = 0

        for semana in semanas:
            for registro in semana:
                total_temperaturas += registro["temperatura"]
                cantidad_temperaturas += 1

        promedio = total_temperaturas / cantidad_temperaturas
        promedios[ciudad] = promedio

    return promedios


def mostrar_promedios(promedios):
    print("Promedio de temperaturas por ciudad:")
    for ciudad, promedio in promedios.items():
        print(f"{ciudad}: {promedio:.2f}°C")


# Datos de temperaturas: 3 ciudades durante 4 semanas
temperaturas = {
    "Quito": [
        [  # Semana 1
            {"dia": "Lunes", "temperatura": 15},
            {"dia": "Martes", "temperatura": 18},
            {"dia": "Miércoles", "temperatura": 20},
            {"dia": "Jueves", "temperatura": 16},
            {"dia": "Viernes", "temperatura": 15},
        ],
        [  # Semana 2
            {"dia": "Lunes", "temperatura": 18},
            {"dia": "Martes", "temperatura": 19},
            {"dia": "Miércoles", "temperatura": 20},
            {"dia": "Jueves", "temperatura": 13},
            {"dia": "Viernes", "temperatura": 18},
        ],
        [  # Semana 3
            {"dia": "Lunes", "temperatura": 18},
            {"dia": "Martes", "temperatura": 12},
            {"dia": "Miércoles", "temperatura": 15},
            {"dia": "Jueves", "temperatura": 18},
            {"dia": "Viernes", "temperatura": 17},
        ],
        [  # Semana 4
            {"dia": "Lunes", "temperatura": 20},
            {"dia": "Martes", "temperatura": 23},
            {"dia": "Miércoles", "temperatura": 22},
            {"dia": "Jueves", "temperatura": 18},
            {"dia": "Viernes", "temperatura": 15},
        ]
    ],
    "Cuenca": [
        [  # Semana 1
            {"dia": "Lunes", "temperatura": 20},
            {"dia": "Martes", "temperatura": 21},
            {"dia": "Miércoles", "temperatura": 20},
            {"dia": "Jueves", "temperatura": 22},
            {"dia": "Viernes", "temperatura": 21}
        ],
        [  # Semana 2
            {"dia": "Lunes", "temperatura": 21},
            {"dia": "Martes", "temperatura": 19},
            {"dia": "Miércoles", "temperatura": 20},
            {"dia": "Jueves", "temperatura": 20},
            {"dia": "Viernes", "temperatura": 21}
        ],
        [  # Semana 3
            {"dia": "Lunes", "temperatura": 20},
            {"dia": "Martes", "temperatura": 21},
            {"dia": "Miércoles", "temperatura": 22},
            {"dia": "Jueves", "temperatura": 24},
            {"dia": "Viernes", "temperatura": 17}
        ],
        [  # Semana 4
            {"dia": "Lunes", "temperatura": 20},
            {"dia": "Martes", "temperatura": 23},
            {"dia": "Miércoles", "temperatura": 22},
            {"dia": "Jueves", "temperatura": 18},
            {"dia": "Viernes", "temperatura": 15}
        ],
    ],
    "Manta": [
        [  # Semana 1
            {"dia": "Lunes", "temperatura": 28},
            {"dia": "Martes", "temperatura": 30},
            {"dia": "Miércoles", "temperatura": 31},
            {"dia": "Jueves", "temperatura": 28},
            {"dia": "Viernes", "temperatura": 29}
        ],
        [  # Semana 2
            {"dia": "Lunes", "temperatura": 27},
            {"dia": "Martes", "temperatura": 29},
            {"dia": "Miércoles", "temperatura": 30},
            {"dia": "Jueves", "temperatura": 30},
            {"dia": "Viernes", "temperatura": 31}
        ],
        [  # Semana 3
            {"dia": "Lunes", "temperatura": 30},
            {"dia": "Martes", "temperatura": 31},
            {"dia": "Miércoles", "temperatura": 32},
            {"dia": "Jueves", "temperatura": 34},
            {"dia": "Viernes", "temperatura": 27}
        ],
        [  # Semana 4
            {"dia": "Lunes", "temperatura": 30},
            {"dia": "Martes", "temperatura": 23},
            {"dia": "Miércoles", "temperatura": 22},
            {"dia": "Jueves", "temperatura": 28},
            {"dia": "Viernes", "temperatura": 25}
        ]
    ]
}

# Calcular y mostrar los promedios
promedios = calcular_promedio_ciudades(temperaturas)
mostrar_promedios(promedios)