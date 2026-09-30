from enum import Enum


class EstadoVehiculo(Enum):
    DISPONIBLE = "Disponible"
    RESERVADO = "Reservado"
    EN_ALQUILER = "En alquiler"
    FUERA_DE_SERVICIO = "Fuera de servicio"


class EstadoReserva(Enum):
    SOLICITADA = "Solicitada"
    CONFIRMADA = "Confirmada"
    EN_CURSO = "En curso"
    FINALIZADA = "Finalizada"
    CANCELADA = "Cancelada"