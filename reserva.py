from enums import EstadoReserva, EstadoVehiculo
from historial import RegistroHistorial


class Reserva:
    def __init__(self, numero, cliente, vehiculo, fecha_inicio, fecha_fin):

        if fecha_fin <= fecha_inicio:
            raise ValueError("La fecha final tiene que ser posterior a la inicial")

        self.numero = numero
        self.cliente = cliente
        self.vehiculo = vehiculo
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = EstadoReserva.SOLICITADA
        self.historial = []

        self.agregar_historial("Se creo la reserva")
        cliente.agregar_reserva(self)

    def agregar_historial(self, descripcion):
        registro = RegistroHistorial(self.estado, descripcion)
        self.historial.append(registro)

    def calcular_costo(self):
        dias = (self.fecha_fin - self.fecha_inicio).days
        costo = self.vehiculo.calcular_costo(dias)

        if costo < 0:
            raise ValueError("El costo no puede ser negativo")

        return costo

    def confirmar(self):

        if self.vehiculo.estado != EstadoVehiculo.DISPONIBLE:
            raise ValueError("El vehiculo no esta disponible")

        # primero guarde el historial y despues cambie el estado
        self.agregar_historial("Se confirmo la reserva")

        self.estado = EstadoReserva.CONFIRMADA
        self.vehiculo.estado = EstadoVehiculo.RESERVADO

    def cambiar_estado(self, nuevo_estado):

        if (
            self.estado == EstadoReserva.SOLICITADA
            and nuevo_estado == EstadoReserva.FINALIZADA
        ):
            raise ValueError(
                "No se puede pasar de solicitada a finalizada"
            )

        self.estado = nuevo_estado
        self.agregar_historial("Se cambio el estado")