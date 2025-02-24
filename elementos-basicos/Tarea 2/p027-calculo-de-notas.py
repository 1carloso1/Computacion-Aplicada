cal1 = int(input("Intruduce la primera calificacion: "))
cal2 = int(input("Intruduce la segunda calificacion: "))
cal3 = int(input("Intruduce la tercera calificacion: "))
cal4 = int(input("Intruduce la cuarta calificacion: "))
cal5 = int(input("Intruduce la quinta calificacion: "))

prom = (cal1+cal2+cal3+cal4+cal5)/5

if prom < 6:
    print("Quedas reprobado")
elif prom >=6 and prom <7:
    print("Pasas de panzazo")
elif prom >=7 and prom <8:
    print("Muy bien, puedes mejorar")
elif prom >=8 and prom <9:
    print("Excelente sigue así")
elif prom >=9:
    print("Perfecto tu esfuerzo valió la pena")