"""
frutas = {"pera","papaya","mora","kiwi"}
frutas2 = {"papaya","piña","mora"}
print(frutas)
frutas.add("banano")
print(frutas)
#En los conjuntos no hay orden y se usan llaver{}
frutas.remove("kiwi")
print(frutas)
tropicales = frutas.copy()
print(tropicales)
print(frutas.difference(frutas2))
frutas.discard("banano")
print(frutas)
print(frutas.intersection(frutas2))
frutas.pop()
print(frutas)
frutas.remove("kiwi")
print(frutas)
"""
"""
frutas = {"manzana","banana","naranja","kiwi","manzana"}
frutas2 = {"banana","naranja","kiwi"}
print(frutas.issubset(frutas2))
print(frutas.issuperset(frutas2))
print(frutas.union(frutas2))
print(frutas.intersection(frutas2))
print(len(frutas))
"""