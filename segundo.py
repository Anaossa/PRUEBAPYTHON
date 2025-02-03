
frutas = ["naranja","papaya","pera"]
tamaño = len(frutas)
print(tamaño)
frutas.append("manzana")
print(frutas)
frutas[1]="fresa"
print(frutas)
frutas.insert(1,"mandarina")
print(frutas)
"""""
frutas.clear()
print(frutas)
del frutas
print(frutas)
"""""

#Continuaciónn de la Clase de Python

frutas2 = frutas.copy()
print(frutas2)
frutas2.append("durazno")
print(frutas)
print(frutas2)
#frutas3 = frutas
#frutas3.append("mango")
#print(frutas3)
print(frutas)
cantidad = frutas.count("fresa")
print(cantidad)
carros = ["renault","mazda","chevrolet"]
frutas.extend(carros)
print(frutas)

print(frutas.index("pera"))
frutas.pop(5)
print(frutas)
frutas.remove("fresa")
print(frutas)
frutas.reverse()
print(frutas)
frutas.sort()
print(frutas)
print(frutas[-1])

#Más ejemplos