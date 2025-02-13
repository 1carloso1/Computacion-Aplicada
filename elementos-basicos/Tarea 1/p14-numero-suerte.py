cumpleanios = input("Intruduce tu fecha de nacimiento con 4 digitos: ")

digitos = []
suma = 0
for digito in cumpleanios:
    digitos.append(digito)
    suma = suma + int(digito)
    print(digito)
print(f"La suma de los digitos es: {suma}")