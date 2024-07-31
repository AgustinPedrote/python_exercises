# Imprimir
def imprimir(number: int):
    if number >= 0:
        print(number)
        imprimir(number -1)

imprimir(20)

# Factorial (5! = 5 × 4 × 3 × 2 × 1 = 120)
def factorial(number: int) -> int:
    if number < 0:
        print("Los números negativos no son validos")
        return 0
    elif number == 0:
        return 1
    else:
        return number * factorial(number - 1)

print(factorial(5))

# Fibonacci (5 (2 + 3))
def fibonacci(number: int) -> int:
    if number <= 0:
        print("La posición tiene que ser mayor que cero")
        return 0
    elif number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

print(fibonacci(3))