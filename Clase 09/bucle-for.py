cadena = "Yo me llamo Manuel López."

for variable_temporal in cadena:
    print(variable_temporal)

frutas = ["manzana", "pera", "kiwi", "mandarina", "banana", "uva", "frutilla", "naranja", "durazno", "melón"]

for fruta in frutas:
    print(fruta)
    
productos = [["manzana", 10], ["pera", 100], ["kiwi", 20], ["mandarina", 1000], ["banana", 80], ["uva", 10000], ["frutilla", 1], ["naranja", 70]]
    
for producto in productos:
    print(producto)
    
for producto in productos:
    print(f"Fruta: {producto[0]} - Cantidad: {producto[1]}")

for mes in range(3):
    print("mes: ", mes)

for indice, fruta in enumerate(productos):
    print(f"Fruta[{indice}]: {fruta}")
