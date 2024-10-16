"""
Consigna: 
Crear un programa que solicite al usuario dos números enteros.
Que tenga un menú de opciones con operaciones matemáticas.
Y que informe el resultado.
"""

# Entrada:
numero_1 = int(input("Ingrese el número 1: "))
numero_2 = int(input("Ingrese el número 2: "))

print("Seleccione la operación que desea realizar:")
print("-------------------------------------------")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("-------------------------------------------")

print()

opcion = int(input("Su elección: "))

print(f"Usted eligió la opción {opcion}")

if opcion == 1:
    suma = numero_1 + numero_2
    print(f"El resultado de la suma es {suma}")    
elif opcion == 2:
    resta = numero_1 - numero_2
    print(f"El resultado de la resta es {resta}")
elif opcion == 3:
    multiplicacion = numero_1 * numero_2
    print(f"El resultado de la multiplicación es {multiplicacion}")
elif opcion == 4:
    division = numero_1 / numero_2
    print(f"El resultado de la división es {division}")
else:
    print("Opción no válida.")