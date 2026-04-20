texto = input("Ingrese un texto con al menos 10 palabras: ")

caracteres = len(texto)
caracteresSinEspacio = caracteres - texto.count(" ")
vocales = texto.count("a") + texto.count("e") + texto.count("i") + texto.count("o") + texto.count("u")
palabras = texto.strip().count(" ")+1
primerEspacio = texto.find(" ")
textoSinPref = texto[primerEspacio:]
texto_guion = texto.replace(" ", "-")
texto_inv = texto.swapcase()

print("El numero total de caracteres en el texto es: {}.".format(caracteres))
print("El numero total de caracteres sin contar loe espacios es: {}.".format(caracteresSinEspacio))
print("El numero total de vocales en el texto es: {}.".format(vocales))
print("El numero total de palabras en el texto es: {}.".format(palabras))
print(textoSinPref)
print(texto_guion)
print(texto_inv)
