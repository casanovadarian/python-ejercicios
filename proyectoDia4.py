#Agenda telefonica
print("Escoja una de las siguientes opciones: ")
print("1. Annadir un contacto")
print("2. Buscar un contacto")
print("3. Editar un contacto")
print("4. Eliminar un contacto")
print("5. Mostrar todos los contactos")

opcion = input()
agenda = {"Dayi": 54341658, "Mami": 58728212}

if opcion == "1" :
    nombre = input("Nombre del contacto: ")
    telefono = input("Numero de telefono: ")
    agenda = {nombre:telefono}
    print("Contacto annadido")

elif opcion == "2":
    busqueda = input("Teclee el nombre de la persona: ")
    if busqueda in agenda:
        print("Telefono: {}".format(agenda.get(busqueda)))
    else: 
        print("Ese nombre no esta en su agenda.")

elif opcion == "3":
    nombreMod = input("Nombre del contacto a modificar: ")
    if nombreMod in agenda:
        telefonoMod = input("Telefono a modificar: ")
        agenda[nombreMod] = telefonoMod
        print("Contacto modificado.")
    else: 
        print("Ese nombre no esta en su agenda.")

elif opcion == "4":
    eliminar = input("Contacto a eliminar: ")
    if eliminar in agenda:
        agenda.pop(eliminar)
        print("Contacto eliminado.")
    else:
        print("Ese nombre no esta en su agenda.")
    
elif opcion == "5":
    print(agenda)

else:
    print("Opcion invalida")