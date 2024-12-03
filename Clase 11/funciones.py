def saludar():
    print("Hola, buen día, o buenas tardes, o buenas noches.")

saludar()

def sumar(a, b):
    resultado = a + b
    
    print("El resultado de la suma es:", resultado)

sumar(234, 111)

def saludar(nombre):
    print("Hola", nombre)

saludar("Manuel")

def saludar(nombre="NN"):
    print("Hola", nombre)

saludar()
saludar("Bicho")

sumar(b=7, a=2)

def sumar(a, b):
    resultado = a + b

    return resultado

total = sumar(5, 3)

print("El total es:", total)

def calcular_ventas_producto1():
    ventas = 10

    return ventas

def calcular_ventas_producto2():
    ventas = 15
    
    return ventas

def calcular_ventas_totales():
    total = calcular_ventas_producto1() + calcular_ventas_producto2()

    return total

ventas_totales = calcular_ventas_totales()

print("Las ventas totales son:", ventas_totales)

