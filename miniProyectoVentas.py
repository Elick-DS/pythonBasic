dateUser = []
articulo = []

while True:
        
    nombre = str(input("Ingresa tu nombre: "))

    dateUser.append((nombre))
    
    addres = str(input("Ingresa tu dirección: "))

    dateUser.append((addres))

    while True:
        try:
            numIden = int(input("Ingresa tu identificación: "))
            dateUser.append((numIden))
            break
        except ValueError:
            print("Ingresa un valor válido para la identificación.")
    while True:
        try:
            tel = int(input("Ingresa tu número móvil: "))
            dateUser.append((tel))
            break
        except ValueError:
            print("Ingresa un valor válido para móvil.")
    break

def catalogo(cont = 0, sumArt=int(input("Indica cuántos dispositivos vas a comprar: "))):

    while cont < sumArt:

        try:    
            opcion = int(input("Indica el tipo de dispositivo en el cuál estás interesado \n 1.RESONADOR \n 2.ANGIOGRAFIA \n 3.RADIOGRAFÍA \n Opción: "))
        
            if opcion == 1:
                resonador  =  {1:  ['MAGNETOM',  'Sola',  1.5,  1000],  2:  ['MAGNETOM',  'Altea',  1.5,1200], 3: ['MAGNETOM', 'Amira', 1.5, 1300], 4: ['MAGNETOM', 'Sempra', 1.5, 2000] }

                print(f"| RESONADOR      | MODELO       | TESLAS       | PRECIO       |")
                print("-------------------------------------------------------------")
                print(f"| 1.{resonador[1][0]:<12} | {resonador[1][1]:<12} | {resonador[1][2]:<12} | {resonador[1][3]:<12} |")
                print("-------------------------------------------------------------")
                print(f"| 2.{resonador[2][0]:<12} | {resonador[2][1]:<12} | {resonador[2][2]:<12} | {resonador[2][3]:<12} |")
                print("-------------------------------------------------------------")
                print(f"| 3.{resonador[3][0]:<12} | {resonador[3][1]:<12} | {resonador[3][2]:<12} | {resonador[3][3]:<12} |")
                print("-------------------------------------------------------------")
                print(f"| 4.{resonador[4][0]:<12} | {resonador[4][1]:<12} | {resonador[4][2]:<12} | {resonador[4][3]:<12} |")
                print("-------------------------------------------------------------")

                articulo.append(resonador[int(input("Selecciona el número de dispositivo que deseas comprar: "))])

                cont += 1

            elif opcion == 2:

                angiografia = {1: ['Artis', 'zee', 1000], 2:['Artis', 'one', 1100], 3:['Artis', 'Q', 2000], 4: ['Artis','icono', 1500]}

                print("------------------------------------------------")
                print(f"| ANGIOGRAFIA    | MODELO       | PRECIO       |")
                print("------------------------------------------------")
                print(f"| 1.{angiografia[1][0]:<12} | {angiografia[1][1]:<12} | {angiografia[1][2]:<12} | ")
                print("------------------------------------------------")
                print(f"| 2.{angiografia[2][0]:<12} | {angiografia[2][1]:<12} | {angiografia[2][2]:<12} | ")
                print("------------------------------------------------")
                print(f"| 3.{angiografia[3][0]:<12} | {angiografia[3][1]:<12} | {angiografia[3][2]:<12} | ")
                print("------------------------------------------------")
                print(f"| 4.{angiografia[4][0]:<12} | {angiografia[4][1]:<12} | {angiografia[4][2]:<12} | ")
                print("------------------------------------------------")

                articulo.append(angiografia[int(input("Selecciona el número de ispositivo que deseas comprar: "))])

                cont += 1

            if opcion == 3:

                radiografia  =  {1:['YSIO',  'FAST',  1300],  2:  ['MULTIX',  'myExam',  1220],  3:['Multix','Select', 2050]}

                print("------------------------------------------------")
                print(f"| RADIOGRAFÍA    | MODELO       | PRECIO       |")
                print("------------------------------------------------")
                print(f"| 1.{radiografia[1][0]:<12} | {radiografia[1][1]:<12} | {radiografia[1][2]:<12} | ")
                print("------------------------------------------------")
                print(f"| 2.{radiografia[2][0]:<12} | {radiografia[2][1]:<12} | {radiografia[2][2]:<12} | ")
                print("------------------------------------------------")
                print(f"| 3.{radiografia[3][0]:<12} | {radiografia[3][1]:<12} | {radiografia[3][2]:<12} | ")
                print("------------------------------------------------")

                articulo.append(radiografia[int(input("Selecciona el número de ispositivo que deseas comprar: "))])

                cont += 1

            else:
                print("Ingresa una de las 3 opciones que se piden")
        
        except ValueError:
            print("Ingresa valor correcto")

        for i in articulo:
            print(f"SE AÑADIÓ: \nACTIVO: {i[0]:<10}|MODELO: {i[1]:<10}|PRECIO: {i[-1]:<10}")

catalogo()

total = 0
cont = 0
for i in articulo:
   total += articulo[cont][-1]

   cont+=1
    
print(f"------------------------------------------ \n             FACTURA DE COMPRA \n------------------------------------------ \nFecha: 31/03/2022 \nNombre de cliente: {dateUser[0]}")
print(f"Dirección de cliente: {dateUser[1]}")
print(f"Identificación de cliente: {dateUser[2]}")
print(f"Número móvil de cliente: {dateUser[3]}")
print(f"------------------------------------------ \n             ARTICULOS \n------------------------------------------")
for i in articulo:
   print(f"ACTIVO: {i[0]:<10}|MODELO: {i[1]:<10}|PRECIO: {i[-1]:<10}")
print("------------------------------------------")
print(f"Precio total de la compra: {total}")
    

    


    

    









