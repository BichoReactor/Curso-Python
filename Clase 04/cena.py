"""
¡Salimos a cenar!
Vamos a escribir un programa que calcule el costo total de una salida a cenar para un grupo de personas.
En el mismo se pide la cantidad de personas, el precio promedio del plato y una propina fija del 10%.
"""

personas     = int(input("¿Cuántas personas van a cenar?: "))
precio_plato = float(input("¿Cuál es el precio promedio del plato?: "))

total_cena = personas * precio_plato
propina    = total_cena * 0.10

total_con_propina = total_cena + propina

print("Total de la cena (sin propina): ", total_cena)
print("Propina (10%): ", propina)
print("Total a pagar (con propina): ", total_con_propina)