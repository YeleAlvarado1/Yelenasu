#CALCULO DE DESCUENTO DE COMPRA
# DEFINIR FUNCION CON PARAMETROS
def saludo (nombre):
    print( f'Hola Bienvenido!', nombre)

#LLAMAR FUNCION
saludo("Ing Gustavo")

# DEFINIR FUNCION CALCULAR DESCUENTO
def calcular_descuento(total_compra, porcentaje_descuento=10):
    descuento1 = total_compra * porcentaje_descuento / 100
    monto_final1 = total_compra - descuento1
    return monto_final1, descuento1

# SOLICITAR EL INGRESO DE PRECIO
precio = float(input('Ingrese el precio total de la compra: '))

# LLAMAR FUNCION CON MONTO FINAL Y DESCUENTO
monto_final, descuento = calcular_descuento(precio)
print(f"Descuento 10%: ${descuento:.2f}")
print(f"Monto final a pagar: ${monto_final:.2f}")
print(f"Gracias por tu compra")
