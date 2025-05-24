print("EJERCICIO 1")

frase = "El conocimiento es poder "
print(frase.find("poder"))
print(frase.find("conocimiento"))

print("----------------------------------------------------------------------\n")

print("EJERCICIO 2")

frase2 = "la practica hace al maestro"
print(frase2.find("practica"))
print(frase2.find("maestro"))

print("----------------------------------------------------------------------\n")

print("EJERCICIO 3")

frase3 = (input("ingrese una frase: "))
buscapalabra = (input("ingresa palabra que quieras buscar: "))
print(frase.find(buscapalabra))

print("----------------------------------------------------------------------\n")

print("EJERCICIO 4")

texto = "Doña Uzeada de Ribera Maldonado de Bracamonte y Anaya era baja, rechoncha, abigotada. Ya no existia razon para llamar talle al suyo. Sus colores vivos, sanos, podian mas que el albayalde y el soliman del afeite, con que se blanqueaba por simular melancolias. Gastaba dos parches oscuros, adheridos a las sienes y que fingian medicamentos. Tenia los ojitos ratoniles, maliciosos. Sabia dilatarlos duramente o desmayarlos con recato o levantarlos con disimulo. Caminaba contoneando las imposibles caderas y era dificil, al verla, no asociar su estampa achaparrada con la de ciertos palmipedos domesticos. Sortijas celestes y azules le ahorcaban las falanges"
print(texto.find("Sabia"))
print(texto.find("Caminaba"))
print(texto.find("falanges"))
print(texto[459:655])

print("----------------------------------------------------------------------\n")

print("EJERCICIO 5")

texto = "El oeste de Texas divide la frontera entre Mexico y Nuevo México. Es muy bella pero aspera, llena de cactus, en esta region se encuentran las Davis Mountains. Todo el terreno esta lleno de piedra caliza, torcidos arboles de mezquite y espinosos nopales. Para admirar la verdadera belleza desertica, visite el Parque Nacional de Big Bend, cerca de Brownsville. Es el lugar favorito para los excurcionistas, acampadores y entusiastas de las rocas. Pequeños pueblos y ranchos se encuentran a lo largo de las planicies y cañones de esta region. El area solo tiene dos estaciones, tibia y realmente caliente. La mejor epoca para visitarla es de Diciembre a Marzo cuando los dias son tibios, las noches son frescas y florecen las plantas del desierto con la humedad en el aire."
print(texto.find("oeste"))
print(texto.find("excurcionistas"))
print(texto.find("aire"))