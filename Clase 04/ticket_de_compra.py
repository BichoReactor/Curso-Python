"""
Ejercicio 1: Ticket de compra:

1. Escribir un programa que solicite el nombre, la cantidad y el valor unitario de tres productos.

2. Luego, debe calcular el importe de IVA (21%) de cada producto.

3. Por último, debe mostrar en la terminal el ticket de la operación con todos los datos de la compra.
"""

# Ingreso de valores por pantalla:
print("Ticket de compra")
print("----------------")
print()
producto1_nombre         = input("Ingrese el nombre del producto 1: ")
producto1_cantidad       = int(input("Ingrese la cantidad del producto 1: "))
producto1_valor_unitario = float(input("Ingrese el valor unitario del producto 1: "))
print()
producto2_nombre         = input("Ingrese el nombre del producto 2: ")
producto2_cantidad       = int(input("Ingrese la cantidad del producto 2: "))
producto2_valor_unitario = float(input("Ingrese el valor unitario del producto 2: "))
print()
producto3_nombre         = input("Ingrese el nombre del producto 3: ")
producto3_cantidad       = int(input("Ingrese la cantidad del producto 3: "))
producto3_valor_unitario = float(input("Ingrese el valor unitario del producto 3: "))

# Cálculo de IVA:
IVA = 0.21
producto1_iva_unitario = producto1_valor_unitario * IVA 
producto2_iva_unitario = producto2_valor_unitario * IVA 
producto3_iva_unitario = producto3_valor_unitario * IVA 

producto1_total = (producto1_valor_unitario + producto1_iva_unitario) * producto1_cantidad
producto2_total = (producto2_valor_unitario + producto2_iva_unitario) * producto2_cantidad
producto3_total = (producto3_valor_unitario + producto3_iva_unitario) * producto3_cantidad

ticket_total = producto1_total + producto2_total + producto3_total

# Tiket de la compra
print()
print("Ticket")
print("------")
print(f"Producto 1:")
print(f"{producto1_nombre}")
print(f"Precio por unidad: {producto1_valor_unitario:.2f}")
print(f"IVA por unidad: {producto1_iva_unitario:.2f}")
print(f"Cantidad: {producto1_cantidad}")
print(f"Total Producto 1:\t{producto1_total:.2f}")
print()
print(f"Producto 2:")
print(f"{producto2_nombre}")
print(f"Precio por unidad: {producto2_valor_unitario:.2f}")
print(f"IVA por unidad: {producto2_iva_unitario:.2f}")
print(f"Cantidad: {producto2_cantidad}")
print(f"Total Producto 2:\t{producto2_total:.2f}")
print()
print(f"Producto 3:")
print(f"{producto3_nombre}")
print(f"Precio por unidad: {producto3_valor_unitario:.2f}")
print(f"IVA por unidad: {producto3_iva_unitario:.2f}")
print(f"Cantidad: {producto3_cantidad}")
print(f"Total Producto 3:\t{producto3_total:.2f}")
print()
print(f"Total Ticket:\t{ticket_total:.2f}")