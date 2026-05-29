from input import *

linea_hotel_uno = 0
linea_hotel_dos = 0
linea_hotel_tres = 0
linea_hotel_cuatro = 0
linea_hotel_cinco = 0
    
def validar_contador (estrellas_validadas : int , contador : int , numero_estrella : int) -> int:
    if estrellas_validadas == numero_estrella:
        return contador + 1
    else:
        return contador
    
def grafico_cinco_columnas(linea_hotel_uno: int, linea_hotel_dos: int, linea_hotel_tres: int, linea_hotel_cuatro: int, linea_hotel_cinco: int):


    '''
   
    '''


    valor_maximo = linea_hotel_uno
    if linea_hotel_dos > valor_maximo:
        valor_maximo = linea_hotel_dos
    if linea_hotel_tres > valor_maximo:
        valor_maximo = linea_hotel_tres
    if linea_hotel_cuatro > valor_maximo:
        valor_maximo = linea_hotel_cuatro
    if linea_hotel_cinco > valor_maximo:
        valor_maximo = linea_hotel_cinco
   
    if valor_maximo == 0:
        return "No hay datos suficientes para mostrar el gráfico."


    mensaje_final = ""


    for i in range(valor_maximo, 0, -1):
        linea = ""
       
        if linea_hotel_uno >= i:
            linea += "█   "
        else:
            linea += "  "
           
        if linea_hotel_dos >= i:
            linea += "█   "
        else:
            linea += "  "
           
        if linea_hotel_tres >= i:
            linea += "█   "
        else:
            linea += "  "
           
        if linea_hotel_cuatro >= i:
            linea += "█   "
        else:
            linea += "  "
           
        if linea_hotel_cinco >= i:
            linea += "█   "
        else:
            linea += "  "
       
        mensaje_final += linea + "\n"
   
    return mensaje_final + "1⭐ 2⭐ 3⭐ 4⭐ 5⭐"
    


estrellas_validadas = validar_estrellas(validar_int(pedir_int("ingrese un numero de estrellas (1-5)")))

# print(f"las estrellas elegidas son", estrellas_validadas)

linea_hotel_uno = validar_contador(estrellas_validadas, linea_hotel_uno, 1)
linea_hotel_dos = validar_contador(estrellas_validadas, linea_hotel_dos, 2)
linea_hotel_tres = validar_contador(estrellas_validadas, linea_hotel_tres, 3)
linea_hotel_cuatro = validar_contador(estrellas_validadas, linea_hotel_cuatro, 4)
linea_hotel_cinco = validar_contador(estrellas_validadas, linea_hotel_cinco, 5)

resultado_grafico = grafico_cinco_columnas(linea_hotel_uno , linea_hotel_dos , linea_hotel_tres , linea_hotel_cuatro , linea_hotel_cinco)
print(resultado_grafico)