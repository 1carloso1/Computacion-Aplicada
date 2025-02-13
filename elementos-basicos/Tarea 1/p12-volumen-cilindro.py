import math

radio = float(input("Intruduce el radio del cilindro en cm: "))
altura = float(input("Intruduce la altura del cilindro en cm: "))

volumen = math.pi*pow(radio,2)*altura

print(f"El volumen del cilindro es de {volumen} cm^3")