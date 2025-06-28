print("--------------------------------------------------------------------------")
print("**** EJERCICIO 5 ****")
print("PROMEDIO DE CALIFICACIONES")
notas = []
entrada = input("ingrese una nota de 0 a 5 pero numeros enteros y si quieres que se te de el promedio de las notas ingresa (salir): ")
while entrada.lower() != "salir":
    nota = int(entrada)
    if 0 <= nota <= 5:
        notas.append(nota)
        entrada = input("ingrese otra nota o ingrese (salir) para darte el promedio final: ")
    else:
        print("Nota invalida")
        entrada = input("ingrese otra nota o ingrese (salir) para darte el promedio final: ")
if notas : 
    promedio =sum(notas) / len(notas)
    print(f"el promedio de sus notas fue {promedio}")
else: 
    print("No ingresastes notas validas")
print("--------------------------------------------------------------------------")
print("**** EJERCICIO 6 ****")
print("TABLA DE MULTIPLICAR INTERACTIVA")
