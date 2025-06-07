print("*******TALLER DE CONDICIONALES Y DIAGRAMAS DE FLUJO*********")

print("Ejercicios con condicionaeles y operaciones matematicas\n")
print("EJERCICIO 1")
numero = float(input("ingresa un numero para verificar si es positivo,negativo o cero: "))
if numero > 0 :
    print("el numero es positvo")
elif numero < 0 : 
    print("el numero es negativo")
else : 
    print("el numero es cero")

print("EJERCICIO 2")
n1 = float(input("Ingrese un priemr numero: "))
n2 = float(input("Ingrese un segundo numero: "))
if n1 > n2 : 
    print("el primer numero es mayor")
elif n1 < n2 : 
    print("el segundo numero es mayor")
else : 
    print("esta obsion no esta disponible")

print("EJERCICIO 3")

print("Ejercicio 4")
numero = int(input("ingrese un numero: "))
if numero > 10 and numero < 20 : 
    print("su numero esta entre el 10 y el 20")
else :
    print("su numero no forma parte de los numeros selecionados")
    

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
    
print("Ejercicio 6")
precio_producto = int(input("Ingrese el precio total del producto para saver si tiene un descuento: "))
if precio_producto > 100 :
    descuento = precio_producto * 0.10
    precio_final = descuento - precio_producto
    print("su descuento fue de",descuento)
    print("total apagar:", precio_final)
else :
    print("su producto no tiene descuento por lo tanto tiene que pagar: ",precio_producto)
    
print("Ejercicio 7")
edad = int(input("ingrese la edad para saber si tiene la edad suficiente para votar: "))
if edad >= 18 :
    print("es acto para votar")
else :
    print("no es acto para votar")
    
print("Ejercicio 8")
tipo_cliente = input("hola, ¿eres cliente vip o cliente normal?: ")
producto = int(input("indica el precio del producto: "))

if tipo_cliente == "vip" :
    descuento = producto * 0.20 
    precio_final = descuento - producto
    print("por ser cliente vip tuvo un descuento por lo tanto debes pagar ", precio_final)
else: 
    print("por no ser cliente vip no tienes descuento por lo tanto debes pagar", producto)

print("Ejercicio 9") 