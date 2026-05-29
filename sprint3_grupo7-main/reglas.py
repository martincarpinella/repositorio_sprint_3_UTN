from hoteles import *

def recomendar_cinco_estrellas(
                            presupuesto : int, 
                            motivo_viaje : str,
                            ubicacion : str, 
                            numero_huespedes : int,
                            check_in : int, 
                            ) -> str:
    
    '''
    # ¿Qué hace?
        Filtra los datos ingresados por el usuario para una recomendación de hotel.
        
    # ¿Qué recibe?
        Una serie de int y str.

    # ¿Qué retorna?
        Un str. 
    '''

    hotel_recomendado = ""

    if presupuesto >= 300 and motivo_viaje == "vacaciones" and (ubicacion == "sur" or ubicacion == "norte"):
        hotel_recomendado = HOTEL_1

    elif presupuesto >= 250 and numero_huespedes <= 5 and ubicacion == "norte":
        if motivo_viaje == "vacaciones" or (motivo_viaje == "trabajo" and check_in == 14):
            hotel_recomendado = HOTEL_2

    elif presupuesto >= 200 and motivo_viaje == "trabajo" and check_in == 20 and not (ubicacion == "norte" or ubicacion == "sur"):
        hotel_recomendado = HOTEL_3

    return hotel_recomendado

def recomendar_cuatro_estrellas(
                            presupuesto : int, 
                            motivo_viaje : str,
                            ubicacion : str,
                            categoria : str,
                            numero_huespedes : int,
                            numero_dias : int,
                            check_in : int, 
                            ) -> str:

    '''
    # ¿Qué hace?
        Filtra los datos ingresados por el usuario para una recomendación de hotel.
        
    # ¿Qué recibe?
        Una serie de int y str.

    # ¿Qué retorna?
        Un str. 
    '''

    hotel_recomendado = ""

    if presupuesto >= 180 and ubicacion == "centro" and categoria == "all inclusive" and numero_huespedes >= 3 and numero_huespedes <= 15 and numero_dias <= 10:
        if motivo_viaje == "vacaciones" or (motivo_viaje == "trabajo" and check_in == 20):
            hotel_recomendado = HOTEL_4

    elif presupuesto >= 160 and motivo_viaje == "vacaciones" and (ubicacion == "sur" or ubicacion == "centro") and categoria == "solo alojamiento" and numero_dias >= 7 and numero_dias <= 15:
        hotel_recomendado = HOTEL_5

    return hotel_recomendado

def recomendar_tres_estrellas(
                            presupuesto : int, 
                            motivo_viaje : str,
                            ubicacion : str,
                            categoria : str,
                            numero_huespedes : int,
                            numero_dias : int,
                            check_in : int, 
                            ) -> str:
    

    '''
    # ¿Qué hace?
        Filtra los datos ingresados por el usuario para una recomendación de hotel.
        
    # ¿Qué recibe?
        Una serie de int y str.

    # ¿Qué retorna?
        Un str. 
    '''

    hotel_recomendado = ""

    if presupuesto >= 150 and motivo_viaje == "vacaciones" and (ubicacion == "sur" or ubicacion == "norte") and categoria == "media pension" and numero_huespedes <= 10 and numero_dias >= 7 and numero_dias <= 10:
        hotel_recomendado = HOTEL_6

    elif presupuesto >= 100 and ubicacion == "norte" and categoria == "media pension" and numero_dias <= 15:
        if motivo_viaje == "vacaciones" or (motivo_viaje == "trabajo" and check_in == 14):
            hotel_recomendado = HOTEL_7
        
    elif presupuesto >= 50 and motivo_viaje == "trabajo" and check_in == 14 and ubicacion == "centro" and categoria == "solo alojamiento" and numero_huespedes <= 8:
        hotel_recomendado = HOTEL_8

    return hotel_recomendado

def recomendar_dos_estrellas(
                            presupuesto : int, 
                            motivo_viaje : str,
                            ubicacion : str,
                            categoria : str,
                            numero_huespedes : int,
                            numero_dias : int,
                            check_in : int, 
                            ) -> str:
    
    '''
    # ¿Qué hace?
        Filtra los datos ingresados por el usuario para una recomendación de hotel.
        
    # ¿Qué recibe?
        Una serie de int y str.

    # ¿Qué retorna?
        Un str. 
    '''

    hotel_recomendado = ""

    if presupuesto >= 45 and motivo_viaje == "vacaciones" and (ubicacion == "norte" or ubicacion == "sur") and categoria == "media pension" and numero_huespedes >= 2 and numero_dias >= 3 and numero_dias <= 12:
        hotel_recomendado = HOTEL_9

    elif presupuesto >= 40 and motivo_viaje == "trabajo" and check_in == 20 and (ubicacion == "norte" or ubicacion == "centro") and categoria == "solo alojamiento" and numero_huespedes >= 15 and numero_dias >= 5:
        hotel_recomendado = HOTEL_10

    return hotel_recomendado

def recomendar_una_estrella(
                            presupuesto : int, 
                            motivo_viaje : str,
                            ubicacion : str,
                            numero_huespedes : int,
                            numero_dias : int,
                            check_in : int, 
                            ) -> str:
    
    '''
    # ¿Qué hace?
        Filtra los datos ingresados por el usuario para una recomendación de hotel.
        
    # ¿Qué recibe?
        Una serie de int y str.

    # ¿Qué retorna?
        Un str. 
    '''

    hotel_recomendado = ""

    if presupuesto >= 30 and motivo_viaje == "vacaciones" and (ubicacion == "sur" or ubicacion == "norte") and numero_huespedes <=10:
        hotel_recomendado = HOTEL_11

    elif presupuesto >= 25 and ubicacion == "norte" and numero_huespedes >= 5 and numero_dias >= 10:
        if motivo_viaje == "vacaciones" or (motivo_viaje == "trabajo" and check_in == 20):
            hotel_recomendado = HOTEL_12

    elif presupuesto >= 20 and motivo_viaje == "trabajo" and check_in == 14 and (ubicacion == "norte" or ubicacion == "centro") and numero_huespedes <= 3 and numero_dias >= 7: 
        hotel_recomendado = HOTEL_13

    return hotel_recomendado