# Práctico 6: Estructuras de datos complejos
# Alumno: Angel Fernando TORRES

# 1)
import pprint
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
pprint.pprint(precios_frutas)

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
pprint.pprint(precios_frutas)

# 2)
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 1800
pprint.pprint(precios_frutas)

# 3)
pprint.pprint(precios_frutas.keys())

# 4)
class Persona:
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad
    
    def saludar(self):
        print(f"Hola, soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")

# 5) Crear una clase llamada Circulo que contenga el atributo radio y los métodos calcular_area y
# calcular_perimetro. Dichos métodos deben calcular el parámetro correspondiente.
class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return 3.14 * (self.radio ** 2)
    
    def calcular_perimetro(self):
        return 2 * 3.14 * self.radio

# 6)
class Pila:
    def __init__(self):
        self.elementos = []
    
    def apilar(self, elemento):
        self.elementos.append(elemento)
    
    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        return None
    
    def esta_vacia(self):
        return (len(self.elementos) == 0)

def esta_balanceado(userInput):
    pila = Pila()
    pares = {")": "(", "]": "[", "}": "{"}
    for caracter in userInput:
        if caracter in pares.values(): # Signos que abren ({[
            pila.apilar(caracter)
        elif caracter in pares.keys(): # Signos que cierran )}]
            if pila.esta_vacia() or pila.desapilar() != pares[caracter]:
                return False
    return pila.esta_vacia()
print(esta_balanceado("(){}[]"))
print(esta_balanceado("([()])"))
print(esta_balanceado("({[()]})"))
print(esta_balanceado("([()]{})"))
print(esta_balanceado("(()]{})"))
print(esta_balanceado("({[()])"))
print(esta_balanceado("([()]})"))
print(esta_balanceado("(()"))
print(esta_balanceado(")"))
print(esta_balanceado(""))

# 7)
from collections import deque
class Cola:
    def __init__(self):
        self.elementos = deque()
    
    def encolar(self, elemento):
        self.elementos.append(elemento)
    
    def desencolar(self):
        return self.elementos.popleft() if not self.esta_vacia() else "La cola está vacía"
    
    def esta_vacia(self):
        return len(self.elementos) == 0
    
    def ver_frente(self):
        return self.elementos[0] if not self.esta_vacia() else "La cola está vacía"
    
    def ver_cola(self):
        return list(self.elementos)

cola = Cola()
cola.encolar("Cliente #1")
cola.encolar("Cliente #2")
cola.encolar("Cliente #3")
print("Cola inicial: ", cola.ver_cola())
print("Se cansó y se fue de la cola: ", cola.desencolar())
print("Se cansó y se fue de la cola: ", cola.desencolar())
cola.encolar("Cliente #4")
cola.encolar("Cliente #5")
print("Siguiente turno: ", cola.ver_frente())
print("Esperan impacientes: ", cola.ver_cola()[1:]) # Muestra todos los elementos menos el primero

# 8)
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
    
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end= ' -> ')
            actual = actual.siguiente
        print("None")

lista = ListaEnlazada()
lista.insertar(3)
lista.insertar(2)
lista.insertar(1)
lista.mostrar()

# 9
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

    def invertir(self):
        anterior = None
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        self.cabeza = anterior

lista = ListaEnlazada()
lista.insertar(3)
lista.insertar(2)
lista.insertar(1)
print("Lista original:")
lista.mostrar()
lista.invertir()
print("Lista invertida:")
lista.mostrar()