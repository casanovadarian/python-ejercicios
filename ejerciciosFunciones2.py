def solicitar_nombre():
    nombre = input("Ingrese su nombre: ")
    return nombre

def saludar():
    nombre = solicitar_nombre()
    print(f"¡Hola {nombre}!")

#saludar()

#Ejercicio 2
def pedir_numeros():
    a = input("ingrese un numero: ")
    a = int(a)
    b = input("ingrese otro numero: ")
    b = int (b)
    return a, b

def sumar():
    numero1, numero2 = pedir_numeros()
    suma = numero1 + numero2
    print(f"La suma es: {suma} para {numero1} y {numero2}")

#sumar()

#Ejercicio 3
def solicitar_numero():
    num = input("ingrese un numero entero positivo: ")
    num = int(num)
    if  (num < 0 or num % 1 != 0):
        print(f"Error!!! El numero {num} no es un entero positivo")
    else:    
        return num

def calcular_factorial(n):
    fact = 1
    while n > 0:
        fact *= n
        n -= 1
    return fact

def mostrar_resultado():
    n = solicitar_numero()
    resultado = calcular_factorial(n)
    print(f"El factorial de {n} es {resultado}")

mostrar_resultado()