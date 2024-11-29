# Diccionario de productos con nombre y cantidad

productos = {
    "Manzanas": 50,
    "Peras"   : 30,
    "Bananas" : 40
}

print(productos["Manzanas"])

print(productos.get("Peras", 0))
print(productos.get("Uvas", 0))

productos["Naranjas"] = 25
productos["Manzanas"] = 60

print(productos)

del productos["Bananas"]

print(productos)

print("Inventario de productos:")

for producto, cantidad in productos.items():
    print("Producto:", producto, "- Cantidad en stock:", cantidad)
    
for clave in productos.keys():
    print("Producto:", clave)

for valor in productos.values():
    print("Cantidad:", valor)
    
cantidad_bananas = productos.pop("Bananas", "No hay bananas")

print("Cantidad de bananas eliminadas:", cantidad_bananas)

print(productos)

productos.clear()

print(productos)

productos = {
    "Manzanas": 50,
    "Peras"   : 30,
    "Bananas" : 40
}

del productos

productos = {
    "Manzanas": 50,
    "Peras"   : 30,
    "Bananas" : 40
}

inventario = {"Manzanas": 50, "Peras": 30, "Bananas": 40}

ventas_dia = {}

for _ in range(3):
    producto = input("Ingresá el producto vendido: ")
    cantidad_vendida = int(input("Ingresá la cantidad vendida: "))

    if producto in inventario:
        ventas_dia[producto] = cantidad_vendida
    else:
        print("Producto no encontrado en inventario.")