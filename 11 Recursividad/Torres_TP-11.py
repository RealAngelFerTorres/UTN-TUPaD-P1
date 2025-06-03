# Práctico 11: Recursividad
# Alumno: Angel Fernando TORRES

# 1) Crea una función recursiva que calcule el factorial de un número. Luego, 
# utiliza esa función para calcular y mostrar en pantalla el factorial de todos 
# los números enteros entre 1 y el número que indique el usuario
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# Main
userInput = int(input("Ingrese un número entero positivo: "))
print(f"El factorial de {userInput} es: {factorial(userInput)}")

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci 
# en la posición indicada. Posteriormente, muestra la serie completa hasta la 
# posición que el usuario especifique.
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
# Main
userInput = int(input("Ingrese la posición en la serie de Fibonacci: "))
print(f"Serie de Fibonacci hasta la posición {userInput}: ")
for (userInput) in range(userInput + 1):
    print(f"Posición {userInput}:", fibonacci(userInput))

# 3) Crea una función recursiva que calcule la potencia de un número base 
# elevado a un exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1).
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

# Main
userInputBase = int(input("Ingrese la base: "))
userInputExponente = int(input("Ingrese el exponente: "))
print("Resultado: ", potencia(userInputBase, userInputExponente))

# 4) Crear una función recursiva en Python que reciba un número entero 
# positivo en base decimal y devuelva su representación en binario como una 
# cadena de texto.
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
# Main
userInput = int(input("Ingrese un número entero positivo en base decimal: "))
if userInput == 0:
    print("El número en binario es 0")
else:
    print(f"El número en binario es: {decimal_a_binario(userInput)}")

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False
# si no lo es. Requisitos: La solución debe ser recursiva. 
# No se debe usar [::-1] ni la función reversed().
def es_palindromo(palabra):
    # Caso base: si la palabra tiene 0 o 1 caracteres, es un palíndromo
    if len(palabra) <= 1:
        return True
    # Compara el primer y último carácter
    if palabra[0] != palabra[-1]:
        return False
    # Llama recursivamente a la subcadena sin los extremos
    return es_palindromo(palabra[1:-1])
# Main
userInput = input("Ingrese una palabra (sin espacios ni tildes): ").lower()
if es_palindromo(userInput):
    print(f"La palabra '{userInput}' es un palíndromo.")
else:
    print(f"La palabra '{userInput}' no es un palíndromo.")

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)
# Main
userInput = int(input("Ingrese un número entero positivo: "))
print("La suma de los dígitos de es: ", suma_digitos(userInput))

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo 
# coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente 
# hasta llegar al último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques 
# en el nivel más bajo y devuelva el total de bloques que necesita para 
# construir toda la pirámide.
def contar_bloques(n):
    if n == 0:
        return 0
    else:
        return n + contar_bloques(n - 1)
# Main
userInput = int(input("Ingrese el número de bloques en el nivel más bajo: "))
print("Se necesitan estos bloques: ", contar_bloques(userInput))

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que 
# reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y 
# devuelva cuántas veces aparece ese dígito dentro del número.
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    ultimo_digito = numero % 10
    if ultimo_digito == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)
# Main
userInputNumero = int(input("Ingrese un número entero positivo: "))
userInputDigito = int(input("Ingrese un dígito (0-9): "))
if 0 <= userInputDigito <= 9:
    resultado = contar_digito(userInputNumero, userInputDigito)
    print(f"El dígito {userInputDigito} aparece {resultado} vez/veces en el número {userInputNumero}.")