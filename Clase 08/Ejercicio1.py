"""
Registro de ventas por día

Desarrollá un programa que permita registrar las ventas diarias de un comercio durante 5 días.
Al finalizar, el sistema debe mostrar el total de ventas realizadas en cada día y el promedio de ventas.

Tips:
- Usá un bucle while que permita al usuario ingresar el monto de las ventas diarias.
- Asegurate de validar que el monto ingresado sea un valor positivo.

Usá un acumulador para la suma de las ventas.
"""

venta_diaria   = 0
venta_total    = 0
venta_promedio = 0

dias_total = 5

contador_dias = 1

while contador_dias <= 5:
    venta_diaria = int(input(f"Ingrese las ventas del día {contador_dias}: "))
    
    if venta_diaria > 0:
        venta_total = venta_total + venta_diaria
        contador_dias += 1
    else:
        print("Debe ingresar un valor mayor a 0 (cero).")

venta_promedio = venta_total / dias_total

print(f"El promedio de ventas de los {dias_total} fue de {venta_promedio}")