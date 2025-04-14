# Práctico 5: Funciones
# Alumno: Angel Fernando TORRES

# 1) Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.
# Functions
def greeting():
    print("Hola, mundo!")
# Main
greeting()

# 2) Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de-
# volver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.
# Functions
def saludar_usuario(nombre):
    print("Hola, " + nombre + "!")
# Main
saludar_usuario(input("Ingrese su nombre: "))

# 3) Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe-
# dir los datos al usuario y llamar a esta función con los valores in-
# gresados.
# Functions
def informacion_personal(nombre, apellido,edad, residencia):
    print("Soy " + nombre + " " + apellido + ", tengo " + str(edad) + " años y vivo en " + residencia + ".")
# Main
informacion_personal(input("Ingrese su nombre: "), 
                     input("Ingrese su apellido: "), 
                     int(input("Ingrese su edad: ")), 
                     input("Ingrese su residencia: "))

# 4) Crear dos funciones: calcular_area_circulo(radio) que reciba el ra-
# dio como parámetro y devuelva el área del círculo. calcular_peri-
# metro_circulo(radio) que reciba el radio como parámetro y devuel-
# va el perímetro del círculo. Solicitar el radio al usuario y llamar am-
# bas funciones para mostrar los resultados.
# Functions
def calcular_area_circulo(radio):
    return 3.14 * radio ** 2
def calcular_perimetro_circulo(radio):
    return 2 * 3.14 * radio
# Main
radio = float(input("Ingrese el radio del círculo: "))
print("El área del círculo es: " + str(calcular_area_circulo(radio)))
print("El perímetro del círculo es: " + str(calcular_perimetro_circulo(radio)))

# 5) Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mos-
# trar el resultado usando esta función.
# Functions
def segundos_a_horas(segundos):
    print("La cantidad de horas es: " + str(segundos // 3600) + " hora/s.")
# Main
segundos_a_horas(float(input("Ingrese la cantidad de segundos: ")))

# 6) Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la fun-
# ción.
# Functions
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{str(numero)} x {str(i)} = {str(numero * i)}")
# Main
tabla_multiplicar(int(input("Ingrese un número: ")))

# 7) Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resulta-
# do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re-
# sultados de forma clara.
# Functions
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Error: División por cero"
    return (suma, resta, multiplicacion, division)
# Main
tupla = operaciones_basicas(int(input("Ingrese el primer número: ")),
                     int(input("Ingrese el segundo número: ")))
print("La suma es: " + str(tupla[0]))
print("La resta es: " + str(tupla[1]))
print("La multiplicación es: " + str(tupla[2]))
print("La división es: " + str(tupla[3]))

# 8) Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun-
# ción para mostrar el resultado con dos decimales.
# Functions
def calcular_imc(peso, altura):
    return peso / (altura ** 2)
# Main
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso, altura)
print("Su IMC es: " + str(round(imc, 2)))

# 9) Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.
# Functions
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32
# Main
celsius = float(input("Ingrese la temperatura en Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print("La temperatura en Fahrenheit es: " + str(round(fahrenheit, 2)))

# 10) Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.
# Functions
def calcular_promedio(a, b, c):
    return (a + b + c) / 3
# Main
promedio = calcular_promedio(int(input("Ingrese el primer número: ")),
                     int(input("Ingrese el segundo número: ")),
                     int(input("Ingrese el tercer número: ")))
print("El promedio es: " + str(promedio))