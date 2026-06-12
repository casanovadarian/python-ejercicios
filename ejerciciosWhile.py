count = 0
while count < 10:
    count += 1
    print(count)

#Ejercicio 2
count = -1
while count < 15:
    count += 1
    if count == 5 or count == 10:
        continue
    print(count)

#Ejercicio 3
count = 1
while count >= 1:
    if count % 4 == 0:
        break
    print(count)
    count += 1