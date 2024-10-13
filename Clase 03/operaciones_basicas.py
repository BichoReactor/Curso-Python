"""
Ejercicio 1: Operaciones básicas

1. Crea un programa que solicite al usuario dos números enteros.

2. Realiza las siguientes operaciones: suma, resta, multiplicación, y módulo.

3. Muestra el resultado de cada operación en un formato claro y amigable.

Asegúrate de incluir mensajes personalizados que expliquen cada resultado, por ejemplo: "La suma de tus números es: X".
"""

numero1 = int(input("Ingresa un número entero: "))
numero2 = int(input("Ingrese otro número entero: "))

suma           = numero1 + numero2
resta          = numero1 - numero2
multiplicacion = numero1 * numero2
modulo         = numero1 % numero2

print(f"Estos son los resultados obtenidos a partide de los números {numero1} y {numero2}.")
print()
print(f"La suma de {numero1} y {numero2} es {suma}.")
print(f"La resta de {numero1} y {numero2} es {resta}.")
print(f"La multiplicación de {numero1} y {numero2} es {multiplicacion}.")
print(f"El módulo de {numero1} y {numero2} es {modulo}.")