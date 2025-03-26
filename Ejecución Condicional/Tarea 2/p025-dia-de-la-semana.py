semana = {1:"Lunes", 2:"Martes", 3:"Miercoles", 4:"Jueves", 5:"Viernes",6:"Sabado", 7:"Domingo"}
dia = int(input("Introduce el número del día de la semana: "))
if dia < 1 or dia > 7:
    print("Dia invalido")
else:
    print(f"El día correspondiente es: {semana[dia]}")

  