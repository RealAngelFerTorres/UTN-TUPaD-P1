# Práctico 1: Estructuras secuenciales
# Alumno: Angel Fernando TORRES

# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla
name = input("Ingrese su nombre: ")
print(f"Hola {name}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.
name = input("Ingrese su nombre: ")
surname = input("Ingrese su apellido: ")
age = input("Ingrese su edad: ")
location = input("Ingrese su lugar de residencia: ")
print(f"Soy {name} {surname}, tengo {age} años y vivo en {location}.")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro
radius = float(input("Ingrese el radio del círculo: "))
area = 3.14 * radius ** 2
perimeter = 2 * 3.14 * radius
print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimeter}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.
seconds = int(input("Ingrese una cantidad de segundos: "))
hours = seconds // 3600
print(f"{seconds} segundos equivalen a {hours} hora/s.")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla 
# la tabla de multiplicar de dicho número
number = int(input("Ingrese un número: "))
print(f"{number} x 1 = {number * 1}")
print(f"{number} x 2 = {number * 2}")
print(f"{number} x 3 = {number * 3}")
print(f"{number} x 4 = {number * 4}")
print(f"{number} x 5 = {number * 5}")
print(f"{number} x 6 = {number * 6}")
print(f"{number} x 7 = {number * 7}")
print(f"{number} x 8 = {number * 8}")
print(f"{number} x 9 = {number * 9}")
print(f"{number} x 10 = {number * 10}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos
number1 = int(input("Ingrese el primer número: "))
number2 = int(input("Ingrese el segundo número: "))
print(f"{number1} + {number2} = {number1 + number2}")
print(f"{number1} / {number2} = {number1 - number2}")
print(f"{number1} * {number2} = {number1 * number2}")
print(f"{number1} - {number2} = {number1 / number2}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo: 𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 / (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2
height = int(input("Ingrese su altura en kg: "))
weight = int(input("Ingrese su peso en metros: "))
imc = weight / (height ** 2)
print(f"Su índice de masa corporal es: {imc}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
# 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5
# 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32
celsius = float(input("Ingrese una temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.
number1 = float(input("Ingrese el primer número: "))
number2 = float(input("Ingrese el segundo número: "))
number3 = float(input("Ingrese el tercer número: "))
average = (number1 + number2 + number3) / 3
print(f"El promedio de los números es: {average}")