import os

print("*****Bienvenidos al juego del ahorcado******")
print("#### Jugador 1 ####")

palabra = input("Ingrese la palabra secreta: ")
longitud = palabra.__len__()
palabra_encriptada = list('*' * longitud)
vidas = 5
mensaje = ""
letra_quemada = ""

def jugador_2(palabra_encriptada, longitud, vidas, mensaje, letra_quemada):
    os.system("clear")
    print("#### Jugador 2 ####")
    print(f"La palabra tiene {longitud} letras:")
    print(f" {palabra_encriptada}                   vidas: {vidas}")
    print(f"letras falladas:{letra_quemada}") 
    print(mensaje)
    letra = input("Introduzca la letra: ")
    return letra


while vidas >= 1 :
    letra = jugador_2(palabra_encriptada, longitud, vidas, mensaje, letra_quemada)
    
    if palabra.count(letra) == 0 :
        mensaje = "La palabra no tiene esa letra, ha perdido una vida"
        vidas = vidas - 1
        letra_quemada = letra_quemada + " " + letra
    else:
        for i in range(longitud):
            if palabra[i] == letra:
                palabra_encriptada[i] = letra
                mensaje = "Bien!!!! haz dado en el blanco con la letra "+letra

os.system("clear")
print("Lo siento, ha agotado los chances")
print("GAME OVER")