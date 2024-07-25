"""
EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
"""

# Operadores aritméticos
print(f"Suma: 2 + 3 = {2 + 3}")
print(f"Resta: 2 - 3 = {2 - 3}")
print(f"Multiplicación: 2 * 3 = {2 * 3}")
print(f"División: 2 / 3 = {2 / 3}")
print(f"Módulo: 2 % 3 = {2 % 3}")
print(f"Exponente: 2 ** 3 = {2 ** 3}")
print(f"División entera: 2 // 3 = {2 // 3}")

# Operadores de comparación
print(f"Igualdad: 2 == 3 = {2 == 3}")
print(f"Desigual: 2 != 3 = {2 != 3}")
print(f"Mayor que: 2 > 3 = {2 > 3}")
print(f"Menor que: 2 < 3 = {2 < 3}")
print(f"Mayor o igual que: 2 >= 3 = {2 >= 3}")
print(f"Menor o igual que: 2 <= 3 = {2 <= 3}")

# Operadores lógicos
print(f"AND &: True & False = {True & False}")
print(f"OR ||: True || False = {True or False}")
print(f"NOT !: !False = {not False}")

# Operadores de pertenencia
print(f"'u' in 'mouredev' = {'u' in 'Agustin'}")
print(f"'b' not in 'mouredev' = {'b' not in 'Agustin'}")

# Operadores de identidad
my_number = 666
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")

'''
Estructuras de control
'''

# Condicionales
my_string = "Agus"

if my_string == "Agustín":
    print("my_string es 'Agustín'")
elif my_string == "Agus":
    print("my_string es 'Agus'")
else:
    print("my_string no es 'Agustín' ni 'Agus'")

# Iterativas
for i in range(11):
    print(i)
    
i = 0

while i <= 10:
    print(i)
    i += 1
    
# Manejo de excepciones
try:
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")
    
