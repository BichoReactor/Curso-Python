"""
Ejercicio 2: Consumo de Combustible:

Realizar una aplicación en Python que a partir de la cantidad de litros de combustible que consume un coche por cada 100 km de recorrido, 
calcule el costo de cada litro de combustible y la longitud del viaje realizado (en kilómetros).
Mostrar un detalle de los litros consumidos y el dinero gastado.
"""

print("Consumo de Combustible")
print("----------------------")
while True:
    litros_por_100km = float(input("Ingresá la cantidad de litros que consume el coche por cada 100 km: "))
    costo_por_litro  = float(input("Ingresá el costo de cada litro de combustible: "))
    longitud_viaje   = float(input("Ingresá la longitud del viaje en kilómetros: "))

    litros_consumidos = (litros_por_100km * longitud_viaje) / 100
    dinero_gastado    = litros_consumidos * costo_por_litro

    print("Litros de combustible consumidos: ", litros_consumidos)
    print("Dinero gastado en combustible: $", dinero_gastado)
    
    opcion = input("Para terminar ingrese una X ").upper()
    
    if opcion == "X":
        break
