"""
frutas = ["manzana", "banana", "naranja", "kiwi", "mango"]
verduras = ["zanahoria", "brócoli", "espinaca", "coliflor", "lechuga"]
print(len(frutas))
frutas.append("sandía")
print(frutas)
print(frutas[1:3])
#frutas.clear()
print(frutas.count("manzana"))
frutas2 = frutas
print(frutas)
frutas2 = frutas.copy()
frutas2.clear()
frutas.extend(verduras)
print(frutas.index("kiwi"))
#frutas[1] = "fresa"
frutas.insert(1, "fresa")
frutas.pop(1)
frutas.remove("banana")
frutas.reverse()
frutas.sort()
print(frutas)  
i = 0
while i < len(frutas):
    print(frutas[i])
    i += 1

for x in frutas:
    print(x)
"""