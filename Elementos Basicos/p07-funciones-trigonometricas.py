# Uso de las funciones trigonometricas en python
import math
print('Calculo de las funciones trigonometricas')
print('Dame un angulo : ')
angulo = int(input())
seno = math.sin(angulo)
coseno = math.cos(angulo)
tangente = math.tan(angulo)
grados = math.degrees(angulo)
salida=(f'Resumen de funciones:\nEl seno es {seno}\nEl coseno es {coseno}\nLa tangente es {tangente}\nEl angulo {angulo} en radianes equivale a {grados}\n')
print(salida)