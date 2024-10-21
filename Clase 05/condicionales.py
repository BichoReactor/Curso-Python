nota = float(input("Nota: "))

if nota >= 7:
    print("Aprobado.")

edad = float(input("Edad: "))

if edad >= 18:
    print("Podés pasar.")
else:
    print("No admitido.")
    
if nota >= 6:
    print("¡Aprobaste!")
    
    if nota >= 9:
        print("¡Excelente calificación!")
    else:
        if nota >= 7.5:
            print("Muy buen trabajo.")
        else:
            print("Buen esfuerzo, pero hay margen de mejora.")
else:
    print("No alcanzaste la calificación mínima para aprobar.")

if nota >= 6:
    print("¡Aprobaste!")
    if nota >= 9:
        print("¡Excelente calificación!")
    elif nota >= 7.5:
        print("Muy buen trabajo.")
    else:
        print("Buen esfuerzo, pero hay margen de mejora.")
else:
    print("No alcanzaste la calificación mínima para aprobar.")