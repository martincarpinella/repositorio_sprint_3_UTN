def pedir_int(mensaje : str) -> str:

    dato = input(mensaje)

    return dato

def validar_int (dato : str) -> int:

    '''
    # Qué hace? 
        Pide el ingreso de un entero y lo valida.

    # Qué recibe?
        Un número entero.

    # Qué retorna?
        El número entero ingresado.
    '''


    while True:

        es_int = True

        for i in dato:
            if i < "0" or i > "9":
                es_int = False
            
            if es_int == True:
                return int(dato)

            else:
                dato = pedir_int("Error. Debe ingresar un número entero: ")

                break

def pedir_str(mensaje : str) -> str: 

    dato = input(mensaje)
    
    return dato

def validar_str (dato : str) -> str:

    '''
    # ¿Qué hace?
        Valida que los caracteres ingresados sean exclusivamente alfabéticos Mayús. y Minus. (A-Z).
        
    # ¿Qué recibe?
        Un string.

    # ¿Qué retorna?
        El string ingresado validado según la condición esperada.
    '''

    while True:


        es_texto = True

        for i in dato:
            i = ord(i)

            if not (i >= 65 and i <= 90) and not (i >= 97 and i <= 122):
                es_texto = False

        if es_texto == True:
            return dato

        else:
            dato = pedir_str("Ingrese solo letras (A-Z): ")

def validar_motivo_viaje (dato : str, par_1 : str, par_2 : str, par_3 : None, error : str) -> str:

    
    '''
    # ¿Qué hace?
        Valida entre 1 y 3 datos ingresados por el usuario.
        
    # ¿Qué recibe?
        Entre 1 y 3 string.

    # ¿Qué retorna?
        Los string validados.
    '''

    valor_usuario = dato
    
    if par_3 == None:
        while valor_usuario != par_1 and valor_usuario != par_2: 

            valor_usuario = input(error)

            if valor_usuario == "":

                valor_usuario = input(error)

    else:
        while valor_usuario != par_1 and valor_usuario != par_2 and valor_usuario != par_3:
                valor_usuario = input(error)

                if valor_usuario == "":
                    valor_usuario = input(error)

    return valor_usuario

def validar_estrellas(numero_ingresado : int , numero_actual = 5) -> int:  
    
    '''
    # ¿Qué hace?
        Función recursiva que valida el número de estrellas ingresado, en un rango de 1 a 5.
        
    # ¿Qué recibe?
        Un int.

    # ¿Qué retorna?
        El número de estrellas validado.
    '''

    if numero_ingresado < 1 or numero_ingresado > 5:
        print("ERROR, ingrese un numero del 1 al 5: ")

        nuevo_int = validar_int(pedir_int("ingrese un numero de estrellas (1-5): "))

        return validar_estrellas(nuevo_int)
    
    elif numero_actual == numero_ingresado:
        return numero_actual

    else:
        return validar_estrellas(numero_ingresado , numero_actual - 1)

def validar_presupuesto (dato : str, presupuesto_minimo : int = 20) -> int:

    '''
    # Qué hace?
        Valida que el ingreso del presupuesto esté dentro del mínimo permitido.

    # Qué recibe?
        Un string.

    # Qué retorna?
        El número de presupuesto como int(?)
    '''

    presupuesto = validar_int(dato)

    while presupuesto < presupuesto_minimo:
        dato = pedir_int("Error❌. Ingrese un presupuesto válido: ")
        presupuesto = validar_int(dato)
    
    return presupuesto

def validar_huespedes_dias(dato: str, ingreso_minimo: int = 1) -> int:

    '''
    # Qué hace?
        Valida el ingreso mínimo de un int.

    # Qué recibe?
        Un string.

    # Qué retorna?
        Un int.
    '''

    numero_ingresado = validar_int(dato)

    while numero_ingresado < ingreso_minimo:
        dato = pedir_int("Error❌. Ingrese un número de días/huéspedes válido: ")
        numero_ingresado = validar_int(dato)
    
    return numero_ingresado

def seleccionar_check_in(mensaje : str, error : str) -> str:

    '''
    # Qué hace?
        Matchea el horario de check-in.

    # Qué recibe?
        Un string.

    # Qué retorna?
        Un string.
    '''

    while True:

        check_in_elegido = pedir_int(mensaje)

        match check_in_elegido:

            case "14":
                check_in_elegido = "Express - 14hs"
                return check_in_elegido

            case "20":
                check_in_elegido = "Express - 20hs"
                return check_in_elegido

            case _:
                print(error)


menu = ('''
Check in disponibles:

-Express: 14hs
-Regular: 20hs

''')

print(menu)

check_in_elegido = seleccionar_check_in("Ingrese el horario que desee: ", "Error. Debe ingresar alguna de las dos opciones.")
print(f"Su check-in es {check_in_elegido}.")


estrellas = validar_estrellas(validar_int(pedir_int("ingrese un numero de estrellas (1-5)")))
print(f"las estrellas elegidas son", estrellas)
presupuesto = validar_presupuesto(pedir_int("Ingrese un presupuesto: "))
print(f"El presupuesto ingresado es: {presupuesto}")

numero_ingresado = validar_huespedes_dias(pedir_int("Ingrese un número de días/huéspedes: "))
print(f"El número de días/huéspedes ingresado es: {numero_ingresado}")
