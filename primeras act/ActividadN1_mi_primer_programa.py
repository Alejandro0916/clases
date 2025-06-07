nombre = input("¿Cual es tu nombre?: ")
nota_1 = float(input("Indica la nota 1: "))
nota_2 = float(input("Indica la nota 2: "))
nota_3 = float(input("Indica la nota 3: "))

nota_final = ( nota_1 * 0.2) + (nota_2 * 0.3) + (nota_3  * 0.5)
print( nombre + " " + "tu nota final fue: ",nota_final)
