# Calcular el area de un circulo

import math
print('Calculando el area de un circulo:\n')
print('Dame el radio: ')

radio = float(input())
area = math.pi * radio ** 2
print(f'El circulo de radio {radio} tiene un area de {area}')