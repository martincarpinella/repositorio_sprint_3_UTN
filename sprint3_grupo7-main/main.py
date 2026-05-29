from reglas import *
from hoteles import *
from input import *

# presupuesto = 150
# motivo_viaje = "trabajo"
# ubicacion = "centro"
# numero_huespedes = 2
# check_in = 20

presupuesto = 260
motivo_viaje = "trabajo"
ubicacion = "norte"
numero_huespedes = 3
check_in = 14

hotel_recomendado = recomendar_cinco_estrellas(
    presupuesto,
    motivo_viaje,
    ubicacion,
    numero_huespedes,
    check_in
)


if hotel_recomendado != "":
    print(f"Hotel recomendado: {hotel_recomendado}")

else:
    print("No se encontró ningún hotel que cumpla con los requisitos.")


nombre = validar_str(pedir_str("Ingrese el nombre del huésped: "))

apellido = validar_str(pedir_str("Ingrese el apellido del huésped: "))

print(nombre, apellido)