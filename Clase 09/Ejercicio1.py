"""
Suma de números naturales

Desarrolla un programa en Python que calcule la suma de los números naturales hasta un número dado utilizando un bucle for.
La suma de los números naturales hasta el número n se define como la suma de todos los números enteros positivos desde 1 hasta n.
Por ejemplo, la suma de los números naturales hasta 6 es 1 + 2 + 3 + 4 + 5 + 6 = 21.

Tips:

¡Usá range()!

El programa debe pedir un número entero n y devolver la suma de los números naturales hasta n.
"""

numero_ingresado = int(input("Ingrese un número entero y mayor a cero: "))

suma_total = 0

for numero in range(numero_ingresado+1):
    suma_total = suma_total + numero

print(f"La suma total de los números naturales hasta {numero_ingresado} es {suma_total}")    