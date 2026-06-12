def imprimir_mensaje():
    print("¡Estoy aprendiendo funciones en Python!")


imprimir_mensaje()

#Ejercicio 2
def saludar_usuario(nombre):
    print(f"Hola {nombre}")

saludar_usuario("Pedro")

#Ejercicio 3
def calcular_area_rectangulo(largo, ancho):
    area = largo * ancho
    return area

print(f"El area es: {calcular_area_rectangulo(4, 6)}")