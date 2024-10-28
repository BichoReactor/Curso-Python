"""
Bucles + Contadores + Acumuladores
"""

# While:
condicion = True

while condicion:
    check = input("Ingrese 'X' para salir o cualquier otra letra para continuar: ").lower()
    
    if check == "x":
        condicion = False

# Contador:
contador = 0

while contador < 10:
    print(contador)
    contador += 1
    
# Acumulador:
contador = 0
acumulador = 0

while contador < 6:
    valor = float(input("Ingrese un valor: "))
    acumulador += valor
    contador += 1

print(f"Acumulación total: {acumulador}")

# Ejercicio 2 (Clase 2): Calcular el ingreso promedio de los primeros 6 meses del año actual
CANTIDAD_MESES = 6

contador_meses = CANTIDAD_MESES
acumulador     = 0
mes            = 1

while contador_meses > 0:
    ingreso = float(input(f"Ingrese el monto del mes {mes}: "))
    
    acumulador += ingreso
    
    mes            += 1
    contador_meses -= 1
    
promedio = acumulador / CANTIDAD_MESES

print(f"El promedio del ingreso de los primeros {CANTIDAD_MESES} meses es {promedio:.2f}")

cadena = "Me llamo Manuel López"
indice = 0

while indice < len(cadena):
    print(f"cadena[{indice}]: {cadena[indice]}")
    indice += 1