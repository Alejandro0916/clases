# SISTEMA DE BIENVENIDA, PAGINA 1

print("PROYECTO SISTEMA DE VENTAS VIRTUAL")
print("╔══════════════════════════════════════════════╗")
print("              🚀 BIENVENIDO A 🚀              ")
print("          🔌💻  Tech⚡Store 💻🔌            ")
print("╚══════════════════════════════════════════════╝\n")

print("En esta tienda online de tecnología te ofrecemos los mejores productos\nde calidad y a los mejores precios, para que obtengas las tres B:\n")

print("⭐  BUENO\n⭐  BONITO\n⭐  BARATO\n")

visualizacion = input("¿Deseas visualizar los productos que tenemos disponibles? (si/no): ").lower()

# Productos disponibles de TECH⚡STORE
productos = [
    ("🔊 Audífonos", "$45.000"),
    ("💿 Memoria USB", "$30.000"),
    ("💿 Memoria RAM", "$50.000"),
    ("🔸 CPU", "$70.000"),
    ("🔌 Cargador", "$20.000"),
    ("⌨ Teclado Gamer", "$135.000")
]

# USUARIOS REGISTRADOS EN EL SISTEMA
usuarios = [
    ("sebastian", "C001", "sebastian@gmail.com"),
    ("alejandro", "C002", "alejandro@gmail.com"),
    ("laura", "C003", "laura@gmail.com")
]

# CONDICION PARA INICIAR SESION O REGISTRARSE
if visualizacion == "si":
    print("Tech⚡Store")
    print("\nLOG IN / REGISTER")
    print("1 - Iniciar sesión")
    print("2 - Registrarse")
    opcion = input("Selecciona una opción (1/2): ")

# BLOQUE DE INICIO DE SESION
    if opcion == "1":
        intentos = 0
        while intentos < 3:
            correo = input("Ingresa tu correo: ").lower()
            codigo = input("Ingresa tu código de acceso: ").upper()
            acceso = False
            for usuario in usuarios: #para usuario esta en usuario
                if correo == usuario[2] and codigo == usuario[1]: # si el correo es igual a lo que ingreso el usuario
                    print(f"\n¡BIENVENIDO DE NUEVO, {usuario[0].capitalize()}!") #aparece el bienvenido y la primera letra en mayus (capitalize)
                    acceso = True
                    break
            if acceso:
                break
            else:
                intentos += 1
                print(f"Datos incorrectos. Intento {intentos}/3.") # CONDICION PARA HACER QUE SOLAMENTE EL USUARIO TENGA 3 INTENTOS
        if intentos == 3:
            print("❌ Demasiados intentos fallidos. el programa cerró") # EL PROGRAMA CIERRA SI LOS 3 INTENTOS SON INCORRECTOS
            exit() # EL PROGRAMA SE FINALIZA FORZOSAMENTE
    # BLOQUE PARA REGISTRO DE SESIÓN
    elif opcion == "2":
        nuevo_nombre = input("Ingresa tu nombre: ").lower()
        nuevo_codigo = f"C{len(usuarios)+1:03}"  #se le suma mas 1 al codigo existente
        nuevo_correo = f"{nuevo_nombre}@gmail.com"
        usuarios.append((nuevo_nombre, nuevo_codigo, nuevo_correo)) # AGREGAMOS EL NUEVO USUARIO A LA LISTA DE USUARIOS
        print(f"\n✔ Registro exitoso. Tu correo es: {nuevo_correo} y tu codigo es: {nuevo_codigo}")

#este else rompe el bucle de si quiere iniciar sesion o registrarse ya que si pone un numero el cual nosea 1/2 le imprime lo siguiente y lo rompe
    else:
        print("Hubo un error / Opción no valida")
        exit()

    print("Tech⚡Store")
    print("\nProductos disponibles:")
    print(f"1. {productos[0]}\n2. {productos[1]}\n3. {productos[2]}\n4. {productos[3]}\n5. {productos[4]}\n6. {productos[5]}")


    carrito = []
    while True:  #carrito
        seleccion = input("🛒 Ingresa el número del producto que deseas agregar (fin para terminar): ").lower()
        if seleccion.lower() == "fin":
            break
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(productos): #ISDIGIT es un metodo cadena verifica si todos los caracteres
            carrito.append(productos[int(seleccion)-1])                    # son de una cadena son digitos
            #int(seleccion):
            # Convierte el número elegido (que es texto) a un número entero.
            # Ejemplo: "2" se convierte en 2.

            # int(seleccion) - 1:
            # Resta 1 para acceder al índice correcto en la lista (porque los índices en Python empiezan desde 0).
            # Entonces si eligió el "producto 2", realmente es el índice 1.

            # productos[int(seleccion) - 1]:
            # Accede al producto en la lista.
            # En el ejemplo, sería productos[1], que es "Banano".

            # carrito.append(...):
            # Añade ese producto al final de la lista carrito.
            print("\n✅  Carrito actualizado:")
            for idx, (prod, prec) in enumerate(carrito, start=1):  #para recorrer un iterable (como list, tupl o cadena) y obtener tanto el indice como el valor de cada elemento
                print(f"{idx}. {prod} - {prec}")  
                #idx = Para mostrar al usuario un número ordenado de cada producto en el carrito.
        else:
            print("Selección inválida. Intenta de nuevo.")
                #FACTURA
    if carrito:
        print("Tech⚡Store")
        print("\n🧾 RESUMEN DE COMPRA")
        print("--------------------------------------------------")
        total = 0
        for idx, (prod, prec) in enumerate(carrito, start=1): #star=1 empieza a contar de uno
            # Quitar el símbolo $ y los puntos para convertir a entero
            precio_num = int(prec.replace("$", "").replace(".", ""))
            print(f"{idx}. {prod} - {prec}")
            total += precio_num
        iva = total * 0.19
        total_con_iva = total + iva
        print("--------------------------------------------------")
        print("Tech⚡Store")
        print(f"🧾 Subtotal: ${total:,.0f}")
        print(f"🧾 IVA 19%: ${iva:,.0f}")
        print(f"💰 TOTAL A PAGAR: ${total_con_iva:,.0f}")
    else:
        print("🛑 No agregaste productos al carrito.")
        exit()

    print("Tech⚡Store")
    print("-------------💳 MÉTODO DE PAGO------------")
    sinopago = input("¿Deseas continuar a la página de Metodos de Pago? (SI/NO): ").upper() # PREGUNTA DE INTERACCIÓN PARA PREGUNTAR SI DESEA CONTINUAR PARA PAGAR O NO

    if sinopago == "SI":
        print("Tech⚡Store")
        print("-------------💳 MÉTODO DE PAGO------------")
        print("DISPONIBLES:\n1. Nequi\n2. Tarjeta de Crédito/Débito\n3. PayPal")
        pago = input("💳 Ingresa el número del metodo de pago: ")

    # CONDICIONAL PARA LOS METODOS DE PAGO

#metodo de pago mediante nequi
        if pago == "1":
            nequi = input("📱 Ingresa tu numero de Nequi: ")
            print("Validando.....")
            si1 = input("¿Deseas Continuar con la compra? (SI/NO): ").upper() # INTERACCIONM
            if si1 == "SI":
                print(f"✅ Compra Realizada. Gracias por tu compra!\n TOTAL: ${total_con_iva:,.0f}")
            else:
                print("Compra Rechazada.")
                exit()

#metodo de pago mediante tarjeta de credito/debito
        elif pago == "2":
            tarjeta = input("💳 Ingresa los últimos 4 Digitos de tu Tarjeta: ")
            venci = input("🗓 Ingresa la fecha de vencimiento de tu Tarjeta: ")
            cvv = int(input("📅 Ingresa los 3 digitos de tu CVV: "))
            print("Validando...")
            si2 = input("¿Deseas Continuar con la compra? (SI/NO): ").upper()
            if si2 == "SI":
                print(f"✅ Compra Realizada. Gracias por tu compra!\n TOTAL: ${total_con_iva:,.0f}")
            else:
                print("Compra Rechazada.")
                exit()

#metodo de pago mediante paypal 
        elif pago == "3":
            paypal = input("📩 Ingresa tu correo electronico vinculado a Paypal: ")
            print("Validando...")
            si3 = input("¿Deseas Continuar con la compra? (SI/NO): ").upper()
            if si3 == "SI":
                print("Tech⚡Store")
                print(f"✅ Compra Realizada. Gracias por tu compra!\n TOTAL: ${total_con_iva:,.0f}")
            else:
                print("Compra Rechazada.")
                exit()

        else:
            print("❌ Opción de pago no válida. Intenta de nuevo.")
    else:
        print("Tech⚡Store")
        print("Gracias por visitar Tech⚡Store.")
else:
    print("Tech⚡Store")
print("Gracias por visitar Tech⚡Store.")
        # FINALIZA EL SISTEMA.