"""
Valor y referencia
"""

# Tipos de dato por valor son aquellos en los que se trabaja con copias del valor original.
my_int_a = 10
my_int_b = my_int_a
my_int_b = 20
print(my_int_a)
print(my_int_b)

# Tipos de dato por referencia son aquellos en los que las variables almacenan referencias a los datos en lugar de los datos mismos.
my_list_a = [10, 20]
my_list_b = my_list_a
my_list_b.append(30)
print(my_list_a)
print(my_list_b)

# Funciones con datos por valor
def my_int_func(my_int: int):
    my_int = 20
    print(my_int)

my_int_c = 10
my_int_func(my_int_c)
print(my_int_c)

# Funciones con datos por referencia
def my_list_func(my_list: list):
    my_list.append(30)

    my_list_d = my_list
    my_list_d.append(40)

    print(my_list)
    print(my_list_d)


my_list_c = [10, 20]
my_list_func(my_list_c)
print(my_list_c)