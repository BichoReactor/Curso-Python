"""
Ejercicio 2: Calculadora de propinas

Escribe un programa en Python que calcule la propina que se debe dejar en un restaurante.

El script debe solicitar al usuario el monto total de la cuenta y el porcentaje de propina que desea dejar.

Utilizando operadores aritméticos, calcula la cantidad de propina y el total a pagar (incluyendo la propina).

Finalmente, muestra los resultados en la pantalla.
"""

print("CÁLCULO DE PROPINA")
print("------------------")

monto_cuenta       = float(input("Ingrese el monto total de la cuenta: "))
porcentaje_propina = int(input("Ingrese el procentaje de propina que desea dejar: "))

monto_propina = monto_cuenta / porcentaje_propina
monto_total   = monto_cuenta + monto_propina

print(f"El monto de la cuenta es {monto_cuenta}.")
print(f"Se desea dejar una propina del {porcentaje_propina}%.")
print()
print(f"La propina sería de {monto_propina}.")
print(f"El monto total a pagar sería de {monto_total}.")