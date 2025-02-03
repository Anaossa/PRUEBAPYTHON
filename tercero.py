
frutas = ("fresas","papaya","naranja","papaya")


print(frutas.count("papaya"))
print(frutas.index("papaya"))

temporal = list(frutas)

print(frutas)
print(temporal)

temporal.pop(2)
print(temporal)

frutas = tuple(temporal)
print(frutas)
del frutas
print(frutas)


#Parte final de la clase