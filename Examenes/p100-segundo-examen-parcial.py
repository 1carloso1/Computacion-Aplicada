# Segundo examen parcial
empleados = []

print("Mueblería Muebles Dico")
print("Sistema de Procesamiento de Empleados")
print("Captura de datos de los empleados\n")

# Validaciones
def es_nombre_valido(nombre):
    return nombre.replace(" ", "").isalpha()

def es_edad_valida(edad):
    return edad.isdigit() and int(edad) > 0

def es_sexo_valido(sexo):
    return sexo.lower() in ['m', 'f']

def es_sueldo_valido(sueldo):
    try:
        return float(sueldo) > 0
    except ValueError:
        return False

# Captura de datos
while True:
    nombre = input("Nombre del empleado (Para terminar presiona solo enter): ").strip()
    if not nombre:
        break

    while not es_nombre_valido(nombre):
        nombre = input("Por favor, ingrese un nombre válido (solo letras): ").strip()
    
    edad = input(f"Edad de {nombre}: ").strip()
    while not es_edad_valida(edad):
        edad = input(f"Por favor, ingrese una edad válida (número positivo): ").strip()
    edad = int(edad)
    
    sexo = input(f"Sexo de {nombre} (m o f): ").strip().lower()
    while not es_sexo_valido(sexo):
        sexo = input(f"Por favor, ingrese un sexo válido (m o f): ").strip().lower()
    
    pasatiempos = input(f"Pasatiempos de {nombre} (separados por coma y espacio): ").split(', ')
    while not all(p.strip() for p in pasatiempos):
        pasatiempos = input(f"Por favor, ingrese pasatiempos válidos para {nombre} (separados por coma y espacio): ").split(', ')
    
    sueldo = input(f"Sueldo de {nombre}: ").strip()
    while not es_sueldo_valido(sueldo):
        sueldo = input(f"Por favor, ingrese un sueldo válido (número positivo): ").strip()
    sueldo = float(sueldo)

    empleados.append({
        'nombre': nombre,
        'edad': edad,
        'sexo': sexo,
        'pasatiempos': pasatiempos,
        'sueldo': sueldo
    })

# Mostrar datos
print("\nDatos almacenados en la lista de diccionarios:")
for empleado in empleados:
    print(empleado)

# Tabla
print("\nTabla de datos:")
print(f"{'Nombre':<15} {'Edad':<5} {'Sexo':<10} {'Salario':<10} {'Pasatiempos'}")
for e in empleados:
    sexo_str = 'Masculino' if e['sexo'] == 'm' else 'Femenino'
    pasatiempos_str = ', '.join(e['pasatiempos'])
    print(f"{e['nombre']:<15} {e['edad']:<5} {sexo_str:<10} {e['sueldo']:<10.2f} {pasatiempos_str}")

# Estadísticas
total = len(empleados)
hombres = sum(1 for e in empleados if e['sexo'] == 'm')
mujeres = total - hombres

pasatiempos_contador = {}
for e in empleados:
    for p in e['pasatiempos']:
        p = p.strip()
        pasatiempos_contador[p] = pasatiempos_contador.get(p, 0) + 1

suma_edad = sum(e['edad'] for e in empleados)
prom_edad = suma_edad / total if total else 0

suma_sueldo = sum(e['sueldo'] for e in empleados)
prom_sueldo = suma_sueldo / total if total else 0

mayor = max(empleados, key=lambda e: e['edad'], default=None)
menor = min(empleados, key=lambda e: e['edad'], default=None)

# Resumen
print("\nResumen:")
print(f"Total de empleados: {total}")
print(f"Hombres: {hombres}")
print(f"Mujeres: {mujeres}")
print("Pasatiempos más frecuentes:")
for p, c in pasatiempos_contador.items():
    print(f"  - {p}: {c} empleado(s)")

print(f"Suma de edades: {suma_edad}, Promedio: {prom_edad:.1f} años")
print(f"Suma de sueldos: ${suma_sueldo:.2f}, Promedio: ${prom_sueldo:.2f}")
if mayor and menor:
    print(f"{mayor['nombre']} es el mayor ({mayor['edad']} años), {menor['nombre']} es el menor ({menor['edad']} años).")
