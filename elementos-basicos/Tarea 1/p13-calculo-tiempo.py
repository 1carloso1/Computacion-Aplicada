horas = int(input("Intruduce la cantidad de horas que deseas convertir: "))

dias = horas/24
minutos = 60*horas
segundos = pow(60,2)*horas

print(F"{horas} horas tiene un equivalente a: \n  -{dias} dias\n  -{minutos} minutos\n  -{segundos} segundos")