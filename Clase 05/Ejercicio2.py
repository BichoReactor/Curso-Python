"""
Compra con descuentos

Escribe un programa que solicite al usuario el monto total de la compra y la cantidad de artículos que está comprando. 
El programa debe determinar el descuento aplicable según las siguientes reglas:

- Si la cantidad de artículos comprados es mayor o igual a 5 y el monto total es mayor a $10000, aplica un descuento del 15%.

- Si la cantidad de artículos comprados es menor a 5 pero mayor o igual a 3, aplica un descuento del 10%.

- Si la cantidad de artículos comprados es menor a 3, no se aplica descuento.

Al final, el programa debe imprimir el monto total de la compra después de aplicar cualquier descuento o simplemente el monto original si no hay descuento.
"""

print("Compra con descuentos")
print("---------------------")
print()
monto_total    = float(input("Ingrese el monto total de la compra: "))
articulos_cant = int(input("Ingrese la cantidad de artículos: "))
print()

descuento_porcentaje = 0

if articulos_cant >= 5 and monto_total > 10000:
    descuento_porcentaje = 15
elif 3 <= articulos_cant < 5:
    descuento_porcentaje = 10

descuento_monto = (monto_total * descuento_porcentaje) / 100

print(f"El monto final de la compra es {monto_total-descuento_monto}")

