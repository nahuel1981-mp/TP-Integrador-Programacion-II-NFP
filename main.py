from datetime import date

from cliente import Cliente
from sucursal import Sucursal
from vehiculos import Auto, Camioneta, Moto
from reserva import Reserva
from enums import EstadoReserva, EstadoVehiculo


print("SISTEMA DE ALQUILER DE VEHICULOS")


cliente1 = Cliente(
    "Nahuel",
    "Fernandez",
    "476584754",
    "2991234567",
    "nahuel@gmail.com"
)

print("Cliente:")
print(cliente1.nombre, cliente1.apellido)


auto1 = Auto(
    "AA111AA",
    "Toyota",
    "Corolla",
    50000
)

camioneta1 = Camioneta(
    "AB222AB",
    "Ford",
    "Ranger",
    50000
)

moto1 = Moto(
    "A123ABC",
    "Honda",
    "Wave",
    50000
)


sucursal1 = Sucursal(
    "S01",
    "Cutral Co",
    "Av. Principal 123"
)

sucursal1.agregar_vehiculo(auto1)
sucursal1.agregar_vehiculo(camioneta1)
sucursal1.agregar_vehiculo(moto1)


print("\nVehiculos de la sucursal:")

for vehiculo in sucursal1.vehiculos:
    print(
        vehiculo.marca,
        vehiculo.modelo
    )


print("Costo por 3 dias:")

print(
    "Auto:",
    auto1.calcular_costo(3)
)

print(
    "Camioneta:",
    camioneta1.calcular_costo(3)
)

print(
    "Moto:",
    moto1.calcular_costo(3)
)


reserva1 = Reserva(
    1,
    cliente1,
    auto1,
    date(2026, 10, 1),
    date(2026, 10, 4)
)

print("Reserva:")

print(
    "Numero:",
    reserva1.numero
)

print(
    "Costo:",
    reserva1.calcular_costo()
)


auto1.estado = EstadoVehiculo.RESERVADO

reserva1.confirmar()

print(
    "Estado:",
    reserva1.estado.value
)


reserva1.cambiar_estado(
    EstadoReserva.EN_CURSO
)

print(
    "Nuevo estado:",
    reserva1.estado.value
)


print("Historial:")

for registro in reserva1.historial:
    print(
        registro.fecha,
        registro.estado.value,
        registro.descripcion
    )

print("Prueba de error 1:")

tarifa = -100

if tarifa > 0:
    auto2 = Auto(
        "AA999AA",
        "Fiat",
        "Cronos",
        tarifa
    )
else:
    print("La tarifa tiene que ser mayor a 0")

print("Prueba de error 2:")

fecha_inicio = date(2026, 10, 10)
fecha_fin = date(2026, 10, 5)

if fecha_fin > fecha_inicio:
    reserva2 = Reserva(
        2,
        cliente1,
        moto1,
        fecha_inicio,
        fecha_fin
    )
else:
    print("La fecha final tiene que ser posterior a la inicial")