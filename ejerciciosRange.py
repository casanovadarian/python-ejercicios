for i in range(2, 21, 2):
    print(i)

#Ejercicio 2
suma = 0
numeros = range(1, 101)
for i in numeros:
    suma =  suma + i
print(suma)

#Ejercicio 3
texto = "aprendizaje"
for i in range(len(texto)):
    print(f"Indice {i}: {texto[i]}")