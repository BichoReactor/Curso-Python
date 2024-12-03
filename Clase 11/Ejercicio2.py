"""
Cálculo de promedio de ventas

Desarrollá un programa que permita calcular el promedio de ventas de la tienda. Para esto:

1. Creá una función que reciba como parámetro una lista de ventas diarias y devuelva el promedio de esas ventas.

2. Solicitá a la persona que ingrese las ventas de cada día durante una semana (7 días). Usá la función para calcular y
mostrar el promedio de ventas al finalizar.
"""

def ventas_promedio(ventas):
    return sum(ventas) / len(ventas)

i = 1

ventas_semanales = []

while (i <= 7):
    venta_diaria = float(input(f"Ingrese el total de ventas del día {i}: "))
    
    ventas_semanales.append(venta_diaria)
    
    i += 1

ventas_promedio = ventas_promedio(ventas_semanales)

print(f"El promedio de ventas de la semana fue {ventas_promedio:.2f}")