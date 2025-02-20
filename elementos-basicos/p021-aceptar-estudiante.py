# aceptar estudiante en base a cierto criterios
print('Universidad Patito SA de CV')
nombre = input('dame tu nombre > ')
edad = int(input('dame tu edad > '))
if edad<18 :
    print('solo aceptamos mayores de 18')
else :
    print('dame 2 calificaciones > ')
c1, c2 = int(input()), int(input())
if c1<8 or c2<8 :
    print('solo aceptamos alumnos con calificaciones mayores a 8')
else :
    print(f'{nombre} bienvenid@ a la Universidad Patito, tu edad {edad} y calificaciones {c1} y {c2} lo permiten')