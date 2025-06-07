a = int(input("ingrese un numero: "))
b = int(input("ingrese un numero: "))

ope = a*b

if ope > 1:
    print("C es mayo a 1 pero menor que 100")
elif ope > 100:
    print("C es mayor a 100 pero menor que 200")
elif ope > 200:
    print("C es mayor que 200 pero menor que 300")
else:
    print("C no cumple con las condiciones")
