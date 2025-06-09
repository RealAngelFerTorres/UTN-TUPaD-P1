def busqueda_lineal(lista, objetivo):
    """
    Recorre secuencialmente la lista para encontrar el objetivo.
    Retorna el índice del elemento, o -1 si no se encuentra.
    """
    for indice, valor in enumerate(lista):
        if valor == objetivo:
            return indice  # Elemento encontrado
    return -1  # Elemento no encontrado

# Ejemplo de uso:
numeros = [4, 2, 7, 1, 9]
posicion = busqueda_lineal(numeros, 7)
print("Búsqueda Lineal: El número 7 se encuentra en la posición:", posicion)




def busqueda_binaria(lista, objetivo):
    """
    Realiza búsqueda binaria sobre una lista ordenada.
    Retorna el índice del objetivo o -1 si no se encuentra.
    """
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio  # Elemento encontrado
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# Ejemplo de uso:
numeros_ordenados = sorted(numeros)
posicion = busqueda_binaria(numeros_ordenados, 7)
print("Búsqueda Binaria: El número 7 se encuentra en la posición:", posicion)




def burbuja(lista):
    """
    Ordena la lista utilizando el algoritmo de burbuja.
    Compara cada par de elementos y los intercambia si están en orden incorrecto.
    """
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

print("Ordenamiento Burbuja:", burbuja(numeros.copy()))




def insercion(lista):
    """
    Ordena la lista implementando el algoritmo de inserción.
    Desplaza cada elemento a su posición correcta en una sublista ordenada.
    """
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and clave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

print("Ordenamiento por Inserción:", insercion(numeros.copy()))




def seleccion(lista):
    """
    Ordena la lista utilizando el método de selección.
    Encuentra el elemento mínimo en el listado y lo sitúa en la primera posición.
    """
    for i in range(len(lista)):
        indice_min = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[indice_min]:
                indice_min = j
        lista[i], lista[indice_min] = lista[indice_min], lista[i]
    return lista

print("Ordenamiento por Selección:", seleccion(numeros.copy()))




def merge_sort(lista):
    """
    Implementa el algoritmo Merge Sort que utiliza la técnica 'divide y vencerás'.
    Divide la lista en mitades, ordena recursivamente y combina las mitades ordenadas.
    """
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        
        merge_sort(izquierda)
        merge_sort(derecha)
        
        i = j = k = 0
        # Combina las dos mitades
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1
        # Agrega los elementos restantes de la izquierda (si los hay)
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
        # Agrega los elementos restantes de la derecha (si los hay)
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
    return lista

print("Ordenamiento Merge Sort:", merge_sort(numeros.copy()))





import random

def esta_ordenada(lista):
    """
    Verifica si la lista está ordenada.
    """
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

def bogo_sort(lista):
    """
    Aplica el Bogo Sort, que reordena aleatoriamente la lista hasta obtenerla ordenada.
    Este algoritmo se utiliza únicamente con fines didácticos.
    """
    intentos = 0
    while not esta_ordenada(lista):
        random.shuffle(lista)
        intentos += 1
    print("Número de intentos (mezclas):", intentos)
    return lista

print("Ordenamiento Bogo Sort:", bogo_sort(numeros.copy()))