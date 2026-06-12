numeros = [1, 2, 3, 4, 5, 9]
for i in numeros:
    print(i)

#Ejercicio 2
paises = ['Francia', 'Alemania', 'España', 'Italia', 'Portugal', 'Chile']

for pais in paises:
    if 'a' in pais:
        print(pais)
    
#Ejercicio 3
colores = ['rojo', 'azul', 'verde']
prendas = ['camisa', 'pantalones', 'sombrero']

for color in colores:
    for prenda in prendas:
        print(f"{prenda} color {color}")