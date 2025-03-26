num1 = int(input("Intruduce el primer numero: "))
num2 = int(input("Intruduce el segundo numero: "))
num3 = int(input("Intruduce el tercer numero: "))

if num1 > num2 and num1 > num3:
    print("el numero mayor es: ",num1)
elif num2 > num1 and num2 > num3:
    print("el numero mayor es: ",num2)
elif num3 > num1 and num3 > num2:
    print("el numero mayor es: ",num3)
else:
    print("no se pudo establecer el mayor")