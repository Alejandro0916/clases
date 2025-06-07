año_naci = int(input("ingresa su año de nacimiento: "))
if año_naci <= 1945:
    print("eres de la generacion silenciosa")
elif año_naci <= 1964:
    print("eres de la generacion baby boomer")
elif año_naci <= 1979:
    print("eres de la generacion X")
elif año_naci <= 2000:
    print("ese de la generacion Y")
elif año_naci <= 2010:
    print("eres de la generacion Z")
else :
    print("tu generacion no esta registrada")