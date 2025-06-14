print("*******TALLER DE CONDICIONALES Y DIAGRAMAS DE FLUJO*********")

print("----------------------------------------------------------------------------------------------------------------")

print("Ejercicios con condicionaeles y operaciones matematicas\n")

print("----------------------------------------------------------------------------------------------------------------")

print("EJERCICIO 1")
numero = float(input("ingresa un numero para verificar si es positivo,negativo o cero: "))
if numero >= 1:
    print("el numero es positvo")
elif numero <=-1 : 
    print("el numero es negativo")
elif numero == 0 : 
    print("el numero es cero")

print("----------------------------------------------------------------------------------------------------------------")
  

print("EJERCICIO 2")
n1 = float(input("Ingrese un priemr numero: "))
n2 = float(input("Ingrese un segundo numero: "))
if n1 > n2 : 
    print("el primer numero es mayor")
elif n1 < n2 : 
    print("el segundo numero es mayor")
else : 
    print("esta obsion no esta disponible")

print("----------------------------------------------------------------------------------------------------------------")


print("EJERCICIO 3")

print("Ejercicio 4")
numero = int(input("ingrese un numero: "))
if numero > 10 and numero < 20 : 
    print("su numero esta entre el 10 y el 20")
else :
    print("su numero no forma parte de los numeros selecionados")
    
print("----------------------------------------------------------------------------------------------------------------")

print("Ejercicio 5")
n1 = int(input("ingrese un primero numero: "))
n2 = int(input("Ingrese un segundo numero: "))
n3 = int(input("Ingrese un tercer numero: "))
if n1 > n2 and n1 > n3 :
    print("el primer numero es mayor que el resto")
elif n2 > n1 and n2 >n3 :
    print("el segundo numero es mayor que el resto")
elif n3 > n1 and n3 > n2 :
    print("el tercer numero es mayor que el resto")

print("----------------------------------------------------------------------------------------------------------------")
 
print("Ejercicio 6")
precio_producto = int(input("Ingrese el precio total del producto para saver si tiene un descuento: "))
if precio_producto > 100 :
    descuento = precio_producto * 0.10
    precio_final = descuento - precio_producto
    print("su descuento fue de",descuento)
    print("total apagar:", precio_final)
else :
    print("su producto no tiene descuento por lo tanto tiene que pagar: ",precio_producto)

print("----------------------------------------------------------------------------------------------------------------")

print("Ejercicio 7")
edad = int(input("ingrese la edad para saber si tiene la edad suficiente para votar: "))
if edad >= 18 :
    print("es acto para votar")
else :
    print("no es acto para votar")

print("----------------------------------------------------------------------------------------------------------------")

print("Ejercicio 8")
tipo_cliente = input("hola, ¿eres cliente vip o cliente normal?: ")
producto = int(input("indica el precio del producto: "))

if tipo_cliente == "vip" :
    descuento = producto * 0.20 
    precio_final = descuento - producto
    print("por ser cliente vip tuvo un descuento por lo tanto debes pagar ", precio_final)
else: 
    print("por no ser cliente vip no tienes descuento por lo tanto debes pagar", producto)

print("----------------------------------------------------------------------------------------------------------------")

print("Ejercicio 9") 
numero = int(input("ingresa un numero porfavor: "))
if numero % 5 == 0 and numero % 3 == 0 :
    print("su numero es multiplo de 5 y 3")
else : 
    print("su numero no es multiplo de 5 y 3")

print("----------------------------------------------------------------------------------------------------------------")

print("Ejercicio 10") 
dividendo = int(input("ingresa un numero para dividir: "))
divisor1 = int(input("ingrese el primer divisor: "))
divisor2 = int(input("ingrese el segundo divisor: "))
if dividendo % divisor1 ==0 and dividendo % divisor2 == 0 :
    print("su numero es divisible por los dos numeros")
else : 
    print("su numero no es divisible por los dos numeros")

print("----------------------------------------------------------------------------------------------------------------")
print("*******EJERCICIOS CON LISTAS (CON CONDICIONALES)\n")
print("----------------------------------------------------------------------------------------------------------------")

print("Ejercicio 11")
n1 = int(input("ingresa un primer numero: "))
n2 = int(input("ingresa un segundo numero: "))
n3 = int(input("ingresa un tercer numero: "))
n4 = int(input("ingresa un cuarto numero: "))
n5 = int(input("ingresa un quinto numero: "))
lista = [n1,n2,n3,n4,n5]
print("esta es el orden", lista)
if lista [2] > 10 :
    print("el tercer numero es mayor que 10")
else :
    print("el tercer numero no es mayor a 10")

print("----------------------------------------------------------------------------------------------------------------")

print("Ejercicio 12")
lista = [3, 5, 7, 9]
numero = int(input("ingresa un numero para saber si lo adivinas: "))
if numero == 7 :
    print("su numero es correcto",lista)
else :
    print("su numero no es correcto")

print("----------------------------------------------------------------------------------------------------------------")

print("Ejercicio 13")
n1 = int(input("ingresa un primer numero: "))
n2 = int(input("ingresa un segundo numero: "))
n3 = int(input("ingresa un tercer numero: "))
n4 = int(input("ingresa un cuarto numero: "))
lista = [n1,n2,n3,n4]
ope = n1 + n2 
if ope > 10 :
    print("la suma de los numero es mayor a 10")
else :
    print("su numero es menor a 10")

print("----------------------------------------------------------------------------------------------------------------")

print("Ejercicio 14")
lista=["Ana", "Luis", "Pedro", "Marta"]
name=lista[3]
if name:
    print("Nombre correcto")
else:
    print("Nombre diferente")

print("----------------------------------------------------------------------------------------------------------------")

print("Ejercicio 15")
lista = ["amarillo","azul","verde"]
print(lista)
lista[1]= "azul"
print("lista actualizada",lista)

print("----------------------------------------------------------------------------------------------------------------")

print("Ejercicio 16")
tupla=(5, 8, 12, 20)
if tupla[0] < tupla[3]:
     print("Es de Orden ascendente")
else:
     print("Es de Orden descendente")

print("----------------------------------------------------------------------------------------------------------------")

print("Ejercicio 17")
tupla=(25, 32, 28)
if tupla[1] >30:
     print("Edad mayor a 30")
else: 
     print("Edad menor o igual a 30")
  
print("----------------------------------------------------------------------------------------------------------------")
  
print("Ejercicio 18")
tupla=(1, 2, 3)
print("Tupla: " ,tupla)
lista = list(tupla)
if lista[1] == 2:
    lista[1] = 10
    print("Es posible cambiarla")
else:
     print("No es posible")
tupla = tuple(lista)
print("tupla actualizada la tupla quedo:", tupla)

print("----------------------------------------------------------------------------------------------------------------")

print("Ejercicio 19")
tupla= (4, 9)
if tupla[1]>5:
    print("Coordenada alta")
else: 
    print("Coordenada baja")

print("----------------------------------------------------------------------------------------------------------------")

print("Ejercicio 20")
tup1=(3, 4)
tup2=(3, 5)
if tup1==tup2:
    print("Tuplas iguales")
else: 
    print("Tuplas diferentes")
    
print("----------------------------------------------------------------------------------------------------------------")

print("Ejercicio 21")
diccionario1={
    "Nombre":"Juan",
    "Edad":17 }
if diccionario1["Edad"]>=18:
     print("Adulto")
else:
    print("Menor de edad")
    
print("----------------------------------------------------------------------------------------------------------------")

print("Ejercicio 22")
diccionario = {
    "nombre": "carlos"
}
diccionario["ciudad"] = "bogota"
print(f"el diccionario se le agrego otra cosas y quedo de la siguiente manera{diccionario}")

print("----------------------------------------------------------------------------------------------------------------")

print("Ejercicio 24")
diccionario = {
    "producto": "pan",
    "precio" : 1200}
if "precio" in diccionario :
    print("el valor si existe y es : ",diccionario["precio"])
else:
    print("el valor no existe")

print("----------------------------------------------------------------------------------------------------------------")

print("Ejercicio 25")
diccionario = {
    "pan": 1200 ,
    "leche" : 2000
}
if "pan" in diccionario :
    print("el pan si esta y su valor es de",diccionario["pan"])
else :
    print("el valor no existe")