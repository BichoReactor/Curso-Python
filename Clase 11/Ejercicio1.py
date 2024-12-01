"""
Gestión de descuentos

Imaginá que en tu tienda querés implementar un sistema de descuentos automáticos.
Vas a desarrollar un programa que permita calcular el precio final de un producto después de aplicar un descuento.

Para hacerlo:

1. Crea una función que reciba como parámetros el precio original del producto y el porcentaje de descuento,
    y que retorne el precio final con el descuento aplicado.

2. Luego, pedí que se ingrese el precio y el porcentaje de descuento.
    Mostrá el precio final después de aplicar el descuento.
"""

def precio_final_con_descuento(precio, descuento_porcentaje):
    descuento = (descuento_porcentaje * precio) / 100
    
    precio_final = precio - descuento
    
    return precio_final

producto_precio    = float(input("Ingrese el precio del producto: "))
producto_descuento = float(input("Ingrese el descuento del producto: "))

producto_precio_final = precio_final_con_descuento(producto_precio, producto_descuento)

print(f"El precio final del producto ({producto_precio}) con el descuento de {producto_descuento}% aplicado es de {producto_precio_final}")