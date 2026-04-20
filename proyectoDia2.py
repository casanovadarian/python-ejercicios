nombre = "Darian Casanova"
fecha = "11/4/2026"
saludo = "Buenas tardes"
bienvenida = saludo + " " + nombre + ". Hoy es " + fecha
dolares = 210.00
cantidadEuros = dolares * 0.88
billetes10 = cantidadEuros // 10
billetes1 =  (cantidadEuros % 10) // 1
monedas = ((cantidadEuros % 1) *100)//1
despedida = "Vuelve pronto " + nombre


print(bienvenida)
print("")
print("Usted va a entregar esta cantidad de dolares: ")
print(dolares)
print("")
print("Usted va a recibir esta cantidad de euros: ")
print(cantidadEuros)
print("")
print("le seran entragados en billetes de 10: ")
print(billetes10)
print("")
print("billetes de 1: ")
print(billetes1)
print("")
print("y monedas: ")
print(monedas)
print("")
print(despedida)