# Práctico 3: Estructuras condicionales
# Alumno: Angel Fernando TORRES

# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”
age = int(input("Ingrese su edad: "))
if age >= 18:
    print("Es mayor de edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.
userInput = int(input("Ingrese su nota: "))
if userInput >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar
userInput = int(input("Ingrese un número: "))
if userInput % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años
userInput = int(input("Ingrese su edad: "))
if userInput < 12:
    print("Niño/a")
elif userInput < 18:
    print("Adolescente")
elif userInput < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.
userInput = input("Ingrese su contraseña: ")
if len(userInput) >= 8 and len(userInput) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6) Escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
import random
from statistics import mode, median, mean
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Debugger: Print numbers and calculations
# print("Lista de números aleatorios:", numeros_aleatorios)
# print("Moda: ", moda)
# print("Mediana: ", mediana)
# print("Media: ", media)

if (media > mediana) and (mediana > moda):
    print("Sesgo positivo")
elif (media < mediana) and (mediana < moda):
    print("Sesgo negativo")
elif (media == mediana) and (mediana == moda):
    print("No hay sesgo")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.
userInput = input("Ingrese una frase o palabra: ")
if userInput[-1] in "aeiouAEIOU":
    userInput += "!"
print(userInput)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.
userName = input("Ingrese su nombre: ")
userInput = int(input("Elija un número: 1, 2 o 3: "))
if userInput == 1:
    userName = userName.upper()
elif userInput == 2:
    userName = userName.lower()
elif userInput == 3:
    userName = userName.title()
print(userName)

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala)
userInput = float(input("Ingrese la magnitud del terremoto: "))
if userInput < 3:
    print("Muy leve (imperceptible)")
elif userInput < 4:
    print("Leve (ligeramente perceptible)")
elif userInput < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif userInput < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif userInput < 7:
    print("Muy Fuerte (puede causar daños significativos)")

# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
# Periodo del año; Estación en el hemisferio norte;Estación en el hemisferio sur;
# Desde el 21 de diciembre hasta el 20 de marzo (incluidos); Invierno; Verano;
# Desde el 21 de marzo hasta el 20 de junio (incluidos); Primavera; Otoño;
# Desde el 21 de junio hasta el 20 de septiembre (incluidos); Verano; Invierno;
# Desde el 21 de septiembre hasta el 20 de diciembre (incluidos); Otoño; Primavera;
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.
hemisphere = input("Ingrese su hemisferio (N/S): ")
month = int(input("Ingrese el mes (1-12): "))
day = int(input("Ingrese el día (1-31): "))
print("Usted se encuentra en la estación de", end=" ")
if (hemisphere == "N"):
   if (month == 12 and dia >= 21) or (1 <= month <= 2) or (month == 3 and dia <= 20):
       print ("invierno")
   elif (month == 3 and dia >= 21) or (4 <= month <= 5) or (month == 6 and dia <= 20):
       print ("primavera")
   elif (month == 6 and dia >= 21) or (7 <= month <= 8) or (month == 9 and dia <= 20):
       print ("verano")
   elif (month == 9 and dia >= 21) or (10 <= month <= 11) or (month == 12 and dia <= 20):
       print ("otoño")
elif (hemisphere == "S"):
    if (month == 12 and day >= 21) or (1 <= month <= 2) or (month <= 3 and day <= 20):
        print("verano")
    elif (month == 3 and day >= 21) or (4 <= month <= 5) or (month <= 6 and day <= 20):
        print("otoño")
    elif (month == 6 and day >= 21) or (7 <= month <= 8) or (month <= 9 and day <= 20):
        print("invierno")
    elif (month == 9 and day >= 21) or (10 <= month <= 11) or (month <= 12 and day <= 20):
        print("primavera")