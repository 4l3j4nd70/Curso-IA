#Estructuras de control de flujo : condicional (if) - (for) - (else) - (while) - Tabular para que se cumpla la condicion.
"""
edad = int(input("¿Cual es tu edad?:"))
if edad >= 18:
    print("Eres mayor de edad.")
    print("Puedes votar.")
else:
    print("Eres menor de edad.")
    print("No puedes votar.")
"""
"""
Salario = int(input("¿Cuanto es su sueldo?:"))
if Salario <= 1500000:
    Salario = Salario + 200000
    print("Recibes aux de transporte")
    print("Tu salario es:",Salario)
else: 
    print("No recibes aux de transporte")
"""
"""
salario = int(input("¿Cual es tu sueldo?:"))
if salario < 1000000:
    salario = salario + 200000
    print( "Tu salario es:",salario)
elif salario >= 1000000 and salario < 1500000:
    salario = salario + 100000
    print("Tu salario es:",salario )
else: 
    print("tu sueldo es:",salario)
    print("No tienes derecho a bono.")
"""
# si es menor a 6 años esta en la primera infancia 
#si es mayor o igual a 6 y es menor a 13 es infancia 
#si esta entre mayor o igual a 13 y menor a 18 adolescencia 
# y si es mayor  igual a 18 adultes
"""
edad = int(input("¿Cual es tu edad?:"))
if edad <= 0 and edad < 6:
    print("No ha nacido.")
elif edad > 0 and edad < 6:
    print("Primera infancia.")
elif edad >= 6 and edad < 13:
    print("Infancia.")
elif edad >=13 and edad < 18: 
    print ("Adolescencia.")
elif edad >=18: 
    print("Adultes.")
"""
"""
for a in  range (1,11):
    print(f"tabla del {a}:")
    for b in range(1,11):
        print(f"{a} x {b} = {a*b}")
    print("")    
"""
"""
semana = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    7: "Domingo"
}
numero = int(input("Ingresa un número del 1 al 7: "))
if 1 <= numero <= 7:
    print(f"El día correspondiente es: {semana[numero]}")
else:
    print("Número inválido. Por favor ingresa un número entre 1 y 7.")
"""
"""
texto = input("Ingrese un texto:")
letra = input("Ingrese letra que quiere contar:")
if len(letra) !=1:
    print("ingrese solo una letra.")
else: 
    contador = 0 
    indice = 0 
    posiciones= []
texto = texto.lower()
letra = letra. lower()
while indice < len(texto):
    if texto [indice]== letra:
        contador +=1
        posiciones.append(indice)
    indice +=1
print(f"la letra '{letra}' aparece {contador} veces en el texto.")
if posiciones:
    print(f"Se encunetra en las posiciones: {posiciones}") 
"""
"""
tabla= int(input("Ingrese un numero:"))
for a in range (1,11):
        print(f"{tabla} x {a} = {tabla*a}")
"""
"""
txt = input("Ingrese el texto :")
contador=0
for x in txt:
    if x.isalpha():
        contador+= 1
    print(x)
    print(f"\nCantidad de letras en el texto: {contador}")
"""

    
    
    