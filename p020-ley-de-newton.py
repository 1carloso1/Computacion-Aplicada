# segunda ley de newton (fuerza = masa * aceleracion)
print('Calculando los valores de la segunda ley de newton')
print('[1] calcular la fuerza')
print('[2] calcular la masa')
print('[3] calcular la aceleracion')
op = int(input('Elige una opcion ? '))
if op==1:
    print('\ncalculando la fuerza ..')
    m = int(input('dame la masa? '))
    a = int(input('dame la aceleración? '))
    f = m * a
    print(f'la fuerza es {f}')
elif op==2:
    print('\ncalculando la masa ..')
    f = int(input('dame la fuerza? '))
    a = int(input('dame la aceleración? '))
    m = f / a
    print(f'la mase es {m}')
elif op==3:
    print('\ncalculando la aceleración ..')
    f = int(input('dame la fuerza? '))
    m = int(input('dame la masaa? '))
    a = f / m
    print(f'la aceleración es {a}')
else :
    print('Opcion invalida !!')