#Entrar 3 valores y decir cual es el menor

x, y, z = int(input("entre x: ")), int(input("entre y: ")), int(input("entre z: "))

if x <= y and x <= z:
    print(f"{x} es el menor de los valores")

elif y <= x and y <= z:
    print(f"{y} es el menor de los valores")

elif z <= x and z <= y:
    print(f"{z} es el menor de los valores")

else:
    print("Debe colocar valores numericos enteros")