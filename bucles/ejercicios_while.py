print("****EJERCICIOS CON WHILE****")
print("-----------------------------------------------------")
print("EJERCICIO 1")
print("SUMA HASTA CERO")
total = 0
num = int(input("ingrese un numero y si quieres finalizar ingrese(0): "))
while num != 0 :
    num = int(input("ingrese otro numero y si quieres finalizar ingrese(0): "))
    total += num
print("se cuencia terminada")
print(f"el resultado de la suma fue {total}")
print("-----------------------------------------------------")
print("EJERCICIO 2")
print("CONTRASEÑA CORRECTA")
clave = 1927
contraseña = int(input("ingresa la contraseña de 4 digitos  por favor: "))
while contraseña != 1927:
    print("contraseña incorrecta")
    contraseña = int(input("ingrese la contraseña de 4 digitos por favor: "))
print("contraseña correcta, acceso concedidio")
print("-----------------------------------------------------")
print("EJERCICIO 3")
print("LISTA DE COMPRAS")
lista = []
prd = input("ingrese un producto el cual quieras agregar a la lista(fin para finalizar y imprimir la lista): ").lower()
while prd != "fin" :
    lista.append(prd)
    prd = input("ingrese un producto el cual quieras agregar a la lista(fin para finalizar y imprimir la lista): ").lower()
print(f"la lista quedo de la siguiente manera:{lista}")
print("-----------------------------------------------------")
print("EJERCICIO 4")
print("CONTADOR DE PARES Y IMPARES")
contador = 0
pares = 0
impares = 0
while contador < 10 : 
    num = int(input("ingrese un numero para saber si es par o impar: "))
    if num %2 == 0: 
         pares += 1
    else: 
        impares += 1
    contador += 1 
print(f"el total de numeros pares es de:{pares}")
print(f"el total de numeros impares es de:{impares}")
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
contador = 1 
num = int(input("ingresa un numero para multiplicar: "))
while contador <= 10 :
    procedimiento = num * contador
    print(f"{num} * {contador} = {procedimiento}")
    contador += 1
print("--------------------------------------------------------------------------")
print("**** EJERCICIO 7 ****")
print("ADIVINA EL NUMERO")
num_secret = 17
adivina = int(input("ingresa un numero para vez si lo adivinas: "))
while adivina != "17":
    if num_secret > adivina: 
       print("el numero secreto es mayor que el numero que seleccionaste")
       adivina = int(input("intenta de nuevo: "))
    elif num_secret < adivina:
        print("el numero secreto es menor que el numero que seleccionaste")
        adivina = int(input("intenta de nuevo: "))
    elif num_secret == adivina: 
        print("felicidades haz adivinado el numero")
        break
print("--------------------------------------------------------------------------")
print("**** EJERCICIO 8 ****")
print("TUPLA DE FRUTAS")
tupla = ("fresa","cereza","banano")
adivina_frt =input("adivina una fruta de las 3 frutas seleccionados: ")
while adivina_frt not in tupla:
    print("no adivinastes ninguna de las 3 frutas")
    adivina_frt =input("intenta de nuevo: ")
print("felicidades haz adivinado")
print("--------------------------------------------------------------------------")
print("**** EJERCICIO 9 ****")
print("DICCIONARIO DE TRADUCION")
diccionario = {
    "hola": "hello",
    "gracias": "thank you",
    "adiós": "goodbye",
    "por favor": "please",
    "comida": "food"}
while True:
    palabra = input("Escribe una palabra en español (o salir para terminar): ").lower()
    
    if palabra == "salir":
        print("Programa finalizado.")
        break
    if palabra in diccionario:
        print(f"La traducción de '{palabra}' es '{diccionario[palabra]}'.")
    else:
        print("Palabra no encontrada en el diccionario.")
print("--------------------------------------------------------------------------")
print("**** EJERCICIO 10 ****")
print("CALCULADORA BASICA")


print("--------------------------------------------------------------------------")
print("**** EJERCICIO 11 ****")
print("REGISTRO DE EDAD")
personas = {}
while True:
    nombre = input("Ingresa el nombre (o 'salir' para terminar): ").lower()
    if nombre == "salir":
        break
    edad = input(f"Ingresa la edad de {nombre}: ")
    personas[nombre] = edad
print("Diccionario de nombres y edades:")
print(personas)

