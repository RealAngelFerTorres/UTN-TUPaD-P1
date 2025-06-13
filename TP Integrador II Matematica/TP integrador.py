from datetime import datetime

# ***** PARTE A *****

# - Ingreso de DNIs
DNIs = {
    "Fer": 33847368,
    "Marcos": 47925241,
    "Alicia": 39514287,
    "Beatriz": 40998356,
    "Charlie": 42552164
}

# - Generación automática de los conjuntos de dígitos únicos
def obtener_digitos_unicos(dni):
    # Recibe un número de DNI y devuelve un conjunto con sus dígitos únicos.
    # Ejemplo: 33847368 → {3, 4, 6, 7, 8}
    digitos = set()
    for caracter in str(dni):
        digitos.add(int(caracter))
    return digitos
# Crear los conjuntos de dígitos únicos para cada persona
conjuntos = {}
print("--- Conjuntos de dígitos únicos por persona ---")
for nombre, dni in DNIs.items():
    conjunto_digitos = obtener_digitos_unicos(dni)
    conjuntos[nombre] = conjunto_digitos
    print(f"{nombre}: {conjunto_digitos}")

# - Cálculo y visualización de: unión, intersección, diferencias y diferencia simétrica
F = conjuntos["Fer"]
M = conjuntos["Marcos"]

print("\n--- Operaciones entre Fer y Marcos ---")
print("Unión:", F | M)
print("Intersección:", F & M)
print("Diferencia F - M:", F - M)
print("Diferencia simétrica:", F ^ M)

# - Conteo de frecuencia de cada dígito en cada DNI
print("\n--- Frecuencia de dígitos en cada DNI ---")
for nombre, dni in DNIs.items():
    frecuencia = {}
    for d in str(dni):
        frecuencia[d] = frecuencia.get(d, 0) + 1
    print(f"{nombre}: {frecuencia}")

# - Suma total de dígitos
print("\n--- Suma total de los dígitos de cada DNI ---")
for nombre, dni in DNIs.items():
    suma = sum(int(d) for d in str(dni))
    print(f"{nombre}: {suma}")

# - Evaluación de condiciones lógicas
print("\n--- Evaluación de condiciones lógicas ---")

# "Si algún dígito aparece en al menos 4 conjuntos, se considera un dígito frecuente"
from collections import Counter

contador_global = Counter()
for conj in conjuntos.values():
    contador_global.update(conj)

frecuentes = [d for d, c in contador_global.items() if c >= 4]
if frecuentes:
    print("Dígitos frecuentes (en ≥ 4 conjuntos):", frecuentes)

# "Si existe al menos un conjunto que comparte más de la mitad de sus elementos con 
# otro, se considera una coincidencia fuerte"
print("\n--- Coincidencias fuertes entre conjuntos ---")
nombres = list(conjuntos.keys())

# Recorremos todas las combinaciones posibles de pares de personas (sin repetir)
for i in range(len(nombres)):
    for j in range(i + 1, len(nombres)):
        nombre_1 = nombres[i]
        nombre_2 = nombres[j]

        conjunto_1 = conjuntos[nombre_1]
        conjunto_2 = conjuntos[nombre_2]

        # Calculamos la intersección (elementos en común)
        elementos_comunes = conjunto_1 & conjunto_2

        # Definimos qué se considera "más de la mitad compartida"
        umbral = max(len(conjunto_1), len(conjunto_2)) / 2

        # Si la cantidad de elementos comunes supera el umbral, hay coincidencia fuerte
        if len(elementos_comunes) > umbral:
            print(f"{nombre_1} y {nombre_2} comparten más de la mitad: {elementos_comunes}")


# ***** PARTE B *****

# - Ingreso de los años de nacimiento
años_nacimiento = {
    "Fer": 1988,
    "Marcos": 2007,
    "Alicia": 1999,
    "Beatriz": 2002,
    "Charlie": 2004
}

# - Contar cuántos nacieron en años pares e impares
pares = 0
impares = 0
for año in años_nacimiento.values():
    if año % 2 == 0:
        pares += 1
    else:
        impares += 1

print("\n--- Cantidad de nacidos en años pares e impares ---")
print(f"Años pares: {pares}")
print(f"Años impares: {impares}")

# - Si todos nacieron después del 2000, mostrar "Grupo Z"
print("\n--- Grupo Z o no? ---")
if all(año > 2000 for año in años_nacimiento.values()):
    print("Grupo Z")
else:
    print("Hay integrantes nacidos antes del 2000")

# - Implementar una función para determinar si un año es bisiesto
def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

# - Si alguno nació en año bisiesto, mostrar "Tenemos un año especial"
if any(es_bisiesto(año) for año in años_nacimiento.values()):
    print("\n--- Tenemos un año especial (bisiesto) ---")

# - Calcular el producto cartesiano entre el conjunto de años y el conjunto de edades actuales.
año_actual = datetime.now().year
edades = {nombre: año_actual - año for nombre, año in años_nacimiento.items()}

# Crear conjuntos para producto cartesiano
conjunto_años = set(años_nacimiento.values())
conjunto_edades = set(edades.values())

print("\n--- Producto cartesiano entre años y edades ---")
producto_cartesiano = []
for año in conjunto_años:
    for edad in conjunto_edades:
        producto_cartesiano.append((año, edad))
        print((año, edad))
