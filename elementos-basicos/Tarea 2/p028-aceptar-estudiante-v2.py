# aceptar estudiante en base a cierto criterios
print('Universidad Kitty Kat SA de CV')
nombre = input('dame tu nombre > ')

sexo = input('Ingresa tu sexo (h/m) > ')

if sexo != "m":
    print ("Solo aceptamos mujeres en la universidad")
else:
    edad = int(input('dame tu edad > '))
    if edad<21:
        print('Eres mujer, pero no tienes la edad, solo mayores a 21')
    else :
        print('dame 3 calificaciones > ')
        c1, c2, c3 = float(input()), float(input()), float(input())
        promedio = (c1+c2+c3)/3
        if promedio<8 or promedio>9.5 :
            print('Eres mujer, tienes la edad, pero tu promedio no alcanza solo promedios de 8 a 9.5')
        else :
            print(f'{nombre} bienvenida a la Universidad Kitty Kat, tu edad {edad} y promedio {promedio} lo permiten')