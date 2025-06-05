# # print("EJERCICIO 1")
# # nom_producto= input("ingresa el nombre de tu producto: ")
# # precio_unitario= float(input("ingresa el precio unitario de ese producto:"))
# # cantidad = int(input("ingresa la cantidad del producto: "))
# # tupla = (nom_producto,precio_unitario,)
# # lista = [tupla,cantidad]
# # dicionario = { "producto":lista
# #               }
# # cf= precio_unitario * cantidad
# # print("si precio total del producto es: ",cf)

# print("------------------------------------------------------------------------------------\n")
# print("EJERCICIO 2")
# print("COMPRA DE 3 PRODUCTOS")
# print("primer producto\n")
# nombre_1 = input("ingresa el nombre del producto: ")
# precio_uni_1= float(input("ingrese precio unitario del primer producto: "))
# cantidad_1 = int(input("ingresa la cantidad comprada: "))

# print("SEGUNDO PRODUCTO\n")
# nombre_2 = input("ingresa el nombre del producto: ")
# precio_uni_2 = float(input("ingrese precio unitario del segundo producto: "))
# cantidad_2 = int(input("ingresa la cantidad comprada: "))

# print("TERCER PRODUCTO\n")
# nombre_3 = input("ingresa el nombre del producto: ")
# precio_uni_3 = float(input("ingrese precio unitario del tercer producto: "))
# cantidad_3 = int(input("ingresa la cantidad comprada: "))

# tupla_producto1 =(nombre_1,precio_uni_1)
# tupla_producto2 =(nombre_2,precio_uni_2)
# tupla_producto3 =(nombre_3,precio_uni_3)
# list1 =(tupla_producto1,cantidad_1)
# list2 =(tupla_producto2,cantidad_2)
# list3 =(tupla_producto3,cantidad_3)
# dicionario = {
#     "producto1" : nombre_1 ,
#     "producto2" : nombre_2,
#     "producto3" : nombre_3}
# #operacion para precio final de cada producto 
# total_producto1 = precio_uni_1 * cantidad_1
# total_producto2 = precio_uni_2 * cantidad_2
# total_producto3 = precio_uni_3 * cantidad_3
# total_producto = total_producto1 + total_producto2 + total_producto3
# #en estas codificaciones interactuo con el usuario para hacerle una factura muy detallada y para imprimirle una factura bien ordenada 
# print("INFORMACION PARA LA FACTURA\n")
# print("porfavor responder las siguientes preguntas para imprimir su factura ordenadamente\n")
# nombre_cliente = input("ingrese su nombre para la factura: ")
# dia_compra = input("ingrese la feccha que compro los productos: ")
# #y por ultimo esta es la factura
# print("--------------------------------------------------------\n")
# print("nombre de comprador: ",          nombre_cliente)
# print("dia de compra: ",                dia_compra )
# print("--------------------------------------------------------\n")
# print("PRODUCTOS COMPRADOS:")
# print("--------------------------------------------------------\n")
# print(nombre_1                 ,       total_producto1)
# print("--------------------------------------------------------\n")
# print(nombre_2                 ,       total_producto2)
# print("--------------------------------------------------------\n")
# print(nombre_3                 ,         total_producto3)
# print("--------------------------------------------------------\n")
# print("TOTAL",                          total_producto)
# print("--------------------------------------------------------\n")
# print("Gracias por tu compra que tenga buen dia")