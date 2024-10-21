apellido  = "López"
nombre    = "Manuel"
dirección = "Una Calle 123"
password  = "$3ytR&%|"
edad      = "99"
nada      = ""

dia1 = "Lunes"
dia2 = 'Martes'

print("Soy el 'Bicho Reactor'")
print('Soy el "Bicho Reactor"') # Mi perro "Dinamita"

risa      = 'ja'
carcajada = risa * 5
linea     = "-" * 10

print(carcajada)
print(linea)

nombre = input("Ingrese su nombre: ")
saludo = "Hola " + nombre

print(saludo)

var1 = 3 + 5
var2 = "3" + "5"
# var3 = 3 + "5" 
var4 = str(3) + "5"
var5 = 3 + int("5")

nombre = 'Manuel López'

print(len(nombre))

print(nombre[0])
print(nombre[5])
print(nombre[-1])
print(nombre[-2])

frase = "Yo me llamo Manuel López"

subcadena = frase[0:11]

print("Subcadena desde el inicio hasta el índice 11:", subcadena)

subcadena = frase[:11]

print("Subcadena desde el inicio hasta el índice 11:", subcadena)

subcadena = frase[12:]

print("Subcadena desde el índice 12 hasta el final:", subcadena)

subcadena = frase[::2]

print("Subcadena obtenida:", subcadena)