# Lee datos y envia un saludo

print('Leyendo datos y enviando un saludo:\n')
nombre = input('Dame tu nombre: ') # lee cadena
edad = int(input('Dame la edad: ')) # lee cadena y convierte a entero
peso = float(input('Dame tu peso: ')) # lee una cadena y convierte a float
print(f'{nombre} bienvenido a python, tu edad es {edad}, tu peso es {peso}')
print(type(nombre))
print(type(edad))
print(type(peso))