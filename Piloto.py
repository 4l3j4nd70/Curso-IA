""""
# Generar las tablas de multiplicar del 2 al 10
for i in range(2, 11):  # Iterar desde 2 hasta 10
    print(f"Tabla del {i}:")
    for j in range(1, 11):  # Iterar desde 1 hasta 10
        print(f"{i} x {j} = {i * j}")
    print("-" * 20)  # Separador entre tablas
"""
"""
# Diccionario para almacenar los estudiantes y sus calificaciones
estudiantes = {}

# Función para agregar un estudiante
def agregar_estudiante(nombre, calificaciones):
    estudiantes[nombre] = calificaciones

# Función para calcular el promedio de un estudiante
def calcular_promedio(nombre):
    if nombre in estudiantes:
        calificaciones = estudiantes[nombre]
        return sum(calificaciones) / len(calificaciones)
    else:
        return None

# Función para mostrar el estado del estudiante
def estado_estudiante(nombre):
    promedio = calcular_promedio(nombre)
    if promedio is not None:
        return "Aprobado" if promedio >= 6 else "Reprobado"
    else:
        return "Estudiante no encontrado"

# Función para listar todos los estudiantes y sus promedios
def listar_estudiantes():
    for nombre, calificaciones in estudiantes.items():
        promedio = calcular_promedio(nombre)
        estado = estado_estudiante(nombre)
        print(f"Estudiante: {nombre}, Promedio: {promedio:.2f}, Estado: {estado}")

# Menú principal
while True:
    print("\nSistema de Gestión de Estudiantes")
    print("1. Agregar estudiante")
    print("2. Calcular promedio de un estudiante")
    print("3. Mostrar estado de un estudiante")
    print("4. Listar todos los estudiantes")
    print("5. Salir")
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        nombre = input("Nombre del estudiante: ")
        calificaciones = list(map(float, input("Ingresa las calificaciones separadas por comas: ").split(",")))
        agregar_estudiante(nombre, calificaciones)
        print(f"Estudiante {nombre} agregado con éxito.")
    elif opcion == "2":
        nombre = input("Nombre del estudiante: ")
        promedio = calcular_promedio(nombre)
        if promedio is not None:
            print(f"El promedio de {nombre} es: {promedio:.2f}")
        else:
            print("Estudiante no encontrado.")
    elif opcion == "3":
        nombre = input("Nombre del estudiante: ")
        estado = estado_estudiante(nombre)
        print(f"Estado de {nombre}: {estado}")
    elif opcion == "4":
        listar_estudiantes()
    elif opcion == "5":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
"""
"""
# Solicitar 10 números al usuario
numeros = []
print("Ingresa 10 números:")

for i in range(10):
    numero = float(input(f"Ingresa el número {i + 1}: "))
    numeros.append(numero)

# Calcular el promedio
promedio = sum(numeros) / len(numeros)

# Mostrar el promedio
print(f"El promedio de los números ingresados es: {promedio:.2f}")
"""