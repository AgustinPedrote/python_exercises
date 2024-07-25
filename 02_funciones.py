"""
Funciones definidas por el usuario
"""

# Simple
def funcion():
    print("Hola, Python!")

funcion()

# Con retorno
def funcion2():
    return "Hola, Python!"

print(funcion2())

# Con argumento
def funcion3(name):
    print(f"Hola, {name}!")

funcion3("Python")

# Con argumentos
def funcion3(first, second):
    print(f"Hola, {first} {second}!")

funcion3("Amigo", "Python")

# Con un argumento predeterminado
def funcion3(name = "Python"):
    print(f"Hola, {name}!")

funcion3()

# Con argumentos y return
def funcion3(first, second):
    return print(f"Hola, {first} {second}!")

funcion3("Amigo", "Python")

# Con retorno de varios valores
def multiple_return():
    return "Hola", "Python"

primero, segundo = multiple_return()
print(primero)
print(segundo)

# Con un número variable de argumentos
def variable_argumentos(*names):
    for name in names:
        print(f"Hola, {name}!")

variable_argumentos("first", "second", "third", "fourth")

# Con un número variable de argumentos con palabra clave
def variable_clave(**names):
    for key, value in names.items():
        print(f"{value}({key})!")

variable_clave(
    language="Python",
    name="Agus",
    alias="AgusDev",
    age=40
)

"""
Funciones dentro de funciones
"""
def outer_function():
    def inner_function():
        print("Función interna")
    inner_function()

outer_function()

"""
Funciones del lenguaje (built-in)
"""
print(len("Hola"))
print(type(36))
print("AgusDev".upper())

"""
Variables locales y globales
"""
global_var = "Python"

def hello_python():
    local_var = "Hola"
    print(f"{local_var}, {global_var}")

print(global_var)
# print(local_var) No se puede acceder desde fuera de la función

hello_python()