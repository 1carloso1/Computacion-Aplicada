# Conversión de temperaturas de Centigrados a Farenheit
print('Conversión de temperaturas de centigrados a farenheit ...')
opcion = str.upper( input('Convertir a [C]entigrados o convertir a [F]ahrenheit') )
if opcion == 'C':
    print("\nConvirtiendo a Centigrados ...")
    temp = float(input('Grados Fahrenhit ?'))
    res = (temp - 32) * 5 / 9
    print(f'{temp} grados Fahrenheit, equivalen a {res} grados Centigrados')
else :
    print('\nConviritiendo a Farenhet...')
    temp = float(input("Dame los Centgrados ?"))
    res = ( temp * 9 / 5 ) + 32
    print(f'{temp} grados Fahrenheit, equivalen a {res} grados Centigrados')