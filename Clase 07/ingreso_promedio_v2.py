# Ejercicio 2 (Clase 2): Calcular el ingreso promedio de los primeros 6 meses del año actual

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio")
ingresos = []
ingresos.clear()
contador_meses = 0
acumulador     = 0

while contador_meses < len(meses):
    ingreso = float(input(f"Ingrese el monto del mes {meses[contador_meses]}: "))
    
    elemento = [meses[contador_meses], ingreso]
    ingresos.append(elemento)
    
    acumulador += ingreso
    
    contador_meses += 1
    
promedio = acumulador / len(meses)

print()
print(f"El promedio del ingreso de los primeros {len(meses)} meses es {promedio:.2f}")
print()

i = 0

while i < len(ingresos):
    print(f"{meses[i]}: {ingresos[i][1]}")
    i += 1