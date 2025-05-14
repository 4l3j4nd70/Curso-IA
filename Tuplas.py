"""
frutas =("manzana","banana","naranja","kiwi","mango")
print(len(frutas))
print(frutas[2])
print(frutas[:3])
print(frutas.count("manzana"))
print(frutas.index("kiwi"))
"""
"""
empleados = ("Juan","Pedro","Maria","Ana","Luis")
copia = list(empleados)
print(copia)
copia.remove("Maria")
empleados = tuple(copia)
print(empleados)
"""
"""
Inicio = input("Ingresa números enteros separados por espacios: ")
numeros = list(map(int, Inicio.split()))
pares = []
impares = []
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print("Números pares:", pares)
print("Números impares:", impares)
if len(pares) == 0:
    print("Todos los números son impares.")
elif len(impares) == 0:
    print("Todos los números son pares.")
else:
    print("Hay una mezcla de números pares e impares.")
"""