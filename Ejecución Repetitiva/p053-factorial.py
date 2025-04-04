# Imprime el factorial de un número

print("Calcula el factorial de un número \n")

n = int(input("Ingresa el número del cuál deseas factorial? "))
f = 1
print(f"{n}! = ", end=" ")

for i in range(1, n+1):
    f = f * i
    print(i, end=" ")  
    if i != n:  # Evitar imprimir "x" después del último número
        print("x", end=" ")
    

print(f"\nEl factorial es: {f}")