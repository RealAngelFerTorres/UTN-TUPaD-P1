# Práctico 4: Estructuras repetitivas
# Alumno: Angel Fernando TORRES

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range(101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.
userInput = int(input("Ingrese un número entero: "))
count = 0
while userInput > 0:
    userInput //= 10
    count += 1
print("La cantidad de dígitos es:", count)

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
if num1 > num2:
    num1, num2 = num2, num1
sum = 0
for i in range(num1 + 1, num2):
    sum += i
print("La suma de los números comprendidos entre los ingresados es: ", sum)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.
sum = 0
num = int(input("Ingrese un número entero (0 para salir): "))
while num != 0:
    sum += num
    num = int(input("Ingrese un número entero (0 para salir): "))
print("La suma total es:", sum)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
number = random.randint(0, 9)
attempts = 0
guess = -1
while guess != number:
    guess = int(input("Adivine el número entre 0 y 9: "))
    attempts += 1
print("Le tomó ", attempts,"intento/s")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
for i in range(100, -1, -2):
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
userInput = int(input("Ingrese un número entero positivo: "))
sum = 0
for i in range(userInput + 1):
    sum += i
print("La suma de los números comprendidos entre 0 y ", userInput, "es: ", sum)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
quantity = 100
even = 0
odd = 0
negative = 0
positive = 0
for i in range(quantity):
    userInput = int(input("Ingrese un número entero: "))
    if userInput % 2 == 0:
        even += 1
    else:
        odd += 1
    if userInput < 0:
        negative += 1
    elif userInput > 0:
        positive += 1
print("Números pares:", even)
print("Números impares:", odd)
print("Números negativos:", negative)
print("Números positivos:", positive)

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
quantity = 100
sum = 0
for i in range(quantity):
    userInput = int(input("Ingrese un número entero: "))
    sum += userInput
print("La media de los números ingresados es: ", sum / quantity)

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
userInput = input("Ingrese un número entero: ")
reversedNumber = ""
for i in range(len(userInput) -1, -1, -1):
    reversedNumber += userInput[i]
print("El número invertido es: ", reversedNumber)