objetos = ['hola', 3, 4.5, True]
print(objetos)

objetos.append(False)
print(objetos)

objetos.append(1)
print(objetos)

objetos.pop(1)
print(objetos)

for elemento in objetos:
    print(elemento)

print(objetos[::-1])