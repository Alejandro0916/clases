print("EJERCICIOS DE TUPLAS")
print("-----------------------------------------------")

print("Ejercicio 1")
print("-----------------------------------------------")
tupla_1 = (1, 2, 3, 4, 5)
print("Primer numero", tupla_1[0])
print("Ultimo numero", tupla_1[-1])

print("Ejercicio 2")
print("-----------------------------------------------")
lista_1 = [3.14, 7.50, 6.55, 7.4, 3.5]
print("Segundo numero", lista_1[1])
print("Cuarto numero", lista_1[4])

print("Ejercicio 3")
print("-----------------------------------------------")
tupla_2 = ("Isabella", "Sebastian", "Alejandro")
variable_a = tupla_2[0]
variable_b = tupla_2[1]
variable_c = tupla_2[2]


print("Ejercicio 4")
lista_2 = [3, 6, 9, 12, 15]
suma = lista_2[0] + lista_2[1] + lista_2[2] + lista_2[3] + lista_2[4]
resultado = suma
print(resultado)

print("Ejercicio 5")
tupla_3 = (0.65, 75.8, 2.56)
promedio = tupla_3[0] + tupla_3[1] + tupla_3[2]
promedio_1 = promedio / 3
resultado_2 = promedio_1
print(resultado_2)

print("Ejercicio 6")
lista_3 = [2, 4, 6, 8]
variablea = lista_3[0]
print(variablea)

variableb = lista_3[1]
print(variableb)

variablec = lista_3[2]
print(variablec)

variabled = lista_3[3]
print(variabled)

print("Ejercicio 7")
tupla_4 = (3, 5)
multiplicacion = tupla_4[0] * tupla_4[1]
resultado_3 = multiplicacion
print(resultado_3)

print("Ejercicio 8")
lista_4 = [4, 8, 12]
lista_4.append(int(input("pon algun otro numero que deseas agregar :")))
print("La lista de numeros quedó de la siguiente manera: ", lista_4)
print("Primer numero: ", lista_4[0])
print("Ultimo numero: ", lista_4[-1])

print("Ejercicio 9")
tupla_5 = (3, 24, 89, 110)
suma_4 = tupla_5[0] + tupla_5[1]
resultado_4 = suma_4
print("El resultado de la suma es", resultado_4)

print("Ejercicio 10")
lista_5 = [5, 10, 15, 20, 25]
diferencia_1 = lista_5[1] / lista_5[3]
print(diferencia_1)

print("Ejercicio 11")
tupla_6 = (33, 69, 130, 45, 28)
multiplicacion_3 = tupla_6[0] * tupla_6[-1]
resultado_11 = multiplicacion_3
print(resultado_11)

print("Ejercicio 12")
lista_6 = [6, 94, 83]
division_2 = lista_6[0] / lista_6[2]
print(division_2)

print("Ejercicio 13")
tupla_7 = (4, 90, 28, 12)
print(tupla_7[2])

print("Ejercicio 14")
lista_7 = [3.79, 3.90, 5.87, 31.98, 9.93]
suma_a = lista_7[0] + lista_7[1] + lista_7[2] + lista_7[3] + lista_7[4]
print(suma_a)

print("Ejercicio 15")
lista_8 = [4, 8, 90, 31]
tupla_b = tuple(lista_8)
print(tupla_b)

print("Ejercicio 16")
tupla_8 = (1, 7, 10)
lista_b = list(tupla_8)
lista_b.append(int(input("pon algun otro numero que deseas agregar :")))
print("La lista de numeros quedó de la siguiente manera: ", lista_b)

print("Ejercicio 17")
lista_9 = [8, 3, 34, 12, 3]
tupla_c = tuple(lista_9)
print(tupla_c[2])

print("Ejercicio 18")
tupla_9 = (3, 1, 4)
lista_c = list(tupla_9)

nuevo_numero = int(input("Pon un número para reemplazar el segundo elemento: "))
lista_c[1] = nuevo_numero  

print("La lista de números quedó de la siguiente manera:", lista_c)

print("Ejercicio 19")
lista_10 = [4, 8, 83, 100]
tupla_d = tuple(lista_10)
print("Cantidad de elementos en la tupla:", len(tupla_d))

print("Ejercicio 20")
tupla_11 = (3, 12, 412, 431, 900)
lista_e = list(tupla_11)
lista_e.pop(-1)
print(lista_e)