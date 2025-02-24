lista_numeros = {1:"I", 2:"II", 3:"III", 4:"IV", 5:"V",6:"VI", 7:"VII", 8:"VIII", 9:"IX", 10:"X"}
num = int(input("Introduce el número que deseas convertir a romano: "))
if num < 0 or num > 10:
    print("El numero pasa del limite establecido")
else:
    print(f"El numero romano es: {lista_numeros[num]}")