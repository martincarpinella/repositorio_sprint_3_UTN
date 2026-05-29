from main import *

# =========================
# CONTADORES
# =========================

cantidad_total_consultas = 0
contador_recomendacion = 0

contador_vacaciones = 0
viajes_trabajo = 0

cantidad_usuarios = 0

contador_categoria = 0
contador_usuarios_sur = 0

# =========================
# ACUMULADORES
# =========================

acumulador_dias = 0
presupuesto_sumado = 0

# =========================
# MÁXIMOS
# =========================

max_presupuesto_5_norte = 0
max_huespedes = 0

# =========================
# MÍNIMOS
# =========================

minimo_dias = 0

# =========================
# BANDERAS
# =========================

bandera_dias = True

# =========================
#PORCENTAJE NO CONDICIONADO
if motivo_viaje == "vacaciones":
    contador_vacaciones += 1

#PORCENTAJE CONDICIONADO
if categoria == "all inclusive" and ubicacion == "sur": 
    contador_categoria += 1
    contador_usuarios_sur += 1

#revisar categoria!!!

# =========================

#MÁXIMO GENERAL
def calcular_maximo_huespedes(numero_huespedes : int, 
                                max_huespedes : int) -> int:
    
    if numero_huespedes > max_huespedes:
        max_huespedes = numero_huespedes
    
    return max_huespedes

#PROMEDIO GENERAL  
def calcular_promedio_presupuesto(cantidad_usuarios : int,
                                presupuesto_sumado : int) -> float:
    
    if cantidad_usuarios > 0:
        promedio = presupuesto_sumado / cantidad_usuarios
    
    else:
        promedio = 0
    
    return promedio

#MÍNIMO
def calcular_minimo_dias(numero_dias : int,
                        minimo_dias : int,
                        bandera_dias : bool) -> int:
    
    if bandera_dias == True or numero_dias < minimo_dias:
        minimo_dias = numero_dias

        bandera_dias = False
    
    return minimo_dias

#MÁXIMO CONDICIONADO
def calcular_maximo_norte(estrellas : int,
                        ubicacion : str,
                        presupuesto : int,
                        presupuesto_maximo_norte : int) -> int:
    
    if estrellas == 5 and ubicacion == "norte":
        if presupuesto > presupuesto_maximo_norte:
            max_presupuesto = presupuesto

#ver nombre
    return max_presupuesto

#PORCENTAJE NO CONDICIONADO 
def calcular_porcentaje_vacaciones(contador_vacaciones : int,
                                cantidad_total_consultas : int) -> float:
    

    
    if cantidad_total_consultas > 0:
        promedio_vacaciones = (contador_vacaciones / cantidad_total_consultas) * 100
    else:
        promedio_vacaciones = 0
    
    return promedio_vacaciones

#PORCENTAJE CONDICIONADO
def calcular_porcentaje_categoria(contador_categoria : int, 
                                contador_usuarios_sur : int) -> float:
    
    if contador_usuarios_sur > 0:

        promedio_categoria = (contador_categoria / contador_usuarios_sur) * 100
    
    else:
        promedio_categoria = 0

    return promedio_categoria

#PROMEDIO CONDICIONADO
def calcular_promedio_trabajo(acumulador_dias : int,
                            viajes_trabajo : int) -> float:
    
    if viajes_trabajo > 0:
        promedio_trabajo = acumulador_dias / viajes_trabajo
    
    else:
        promedio_trabajo = 0
    
    return promedio_trabajo