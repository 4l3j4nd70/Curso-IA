# Diccionario para almacenar estudiantes y sus calificaciones
estudiantes = {}

def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ").capitalize()
    calificaciones = []
    cantidad = int(input(f"¿Cuántas calificaciones desea ingresar para {nombre}? "))
    for i in range(cantidad):
        nota = float(input(f"Ingrese calificación #{i + 1}: "))
        calificaciones.append(nota)
    estudiantes[nombre] = calificaciones
    print(f"Estudiante {nombre} agregado correctamente.\n")

def calcular_promedio(nombre):
    if nombre in estudiantes:
        notas = estudiantes[nombre]
        return sum(notas) / len(notas)
    else:
        print("El estudiante no existe.")
        return None

def mostrar_estado(nombre):
    promedio = calcular_promedio(nombre)
    if promedio is not None:
        estado = "Aprobado" if promedio >= 6 else "Reprobado"
        print(f"{nombre} tiene un promedio de {promedio:.2f} y está {estado}.\n")

def listar_estudiantes():
    if not estudiantes:
        print("No hay estudiantes registrados.\n")
        return
    print("Listado de estudiantes y sus promedios:")
    for nombre, notas in estudiantes.items():
        promedio = sum(notas) / len(notas)
        estado = "Aprobado" if promedio >= 6 else "Reprobado"
        print(f"- {nombre}: Promedio = {promedio:.2f} | Estado = {estado}")
    print()

def menu():
    while True:
        print("=== Sistema de Gestión de Estudiantes ===")
        print("1. Agregar estudiante")
        print("2. Calcular promedio de un estudiante")
        print("3. Mostrar estado de un estudiante")
        print("4. Listar todos los estudiantes")
        print("5. Salir")
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            nombre = input("Ingrese el nombre del estudiante: ").capitalize()
            promedio = calcular_promedio(nombre)
            if promedio is not None:
                print(f"Promedio de {nombre}: {promedio:.2f}\n")
        elif opcion == "3":
            nombre = input("Ingrese el nombre del estudiante: ").capitalize()
            mostrar_estado(nombre)
        elif opcion == "4":
            listar_estudiantes()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")

# Ejecutar el programa
menu()

