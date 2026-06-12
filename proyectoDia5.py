def tablas(numero, limite):
    print(f"#### Tabla del {numero} hasta el {limite} ####")
    for n in range(1, limite+1):
        mult = numero * n
        print(f"{numero} X {n} = {mult}")

def solicitud():
    numero = int( input( "Ingrese el numero para multiplicar: " ) )
    limite = int( input( "Ingrese el numero limite: " ) )
    tablas(numero, limite)

salida = "no"
while True:
    print("Este programa genera tablas de multiplicar")
    solicitud()
    salida = input("Desea salir? (y/n): ")
    if salida.lower() == "y":
        break 
