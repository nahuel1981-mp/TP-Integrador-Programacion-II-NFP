from enums import EstadoVehiculo


class Vehiculo:
    def __init__(self, patente, marca, modelo, tarifa):
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.tarifa = tarifa
        self.estado = EstadoVehiculo.DISPONIBLE

    @property
    def tarifa(self):
        return self._tarifa

    @tarifa.setter
    def tarifa(self, tarifa):
        if tarifa <= 0:
            raise ValueError("La tarifa tiene que ser mayor a 0")

        self._tarifa = tarifa

    def calcular_costo(self, dias):
        return self.tarifa * dias


class Auto(Vehiculo):
    def calcular_costo(self, dias):
        return self.tarifa * dias


class Camioneta(Vehiculo):
    def calcular_costo(self, dias):
        costo = self.tarifa * dias
        return costo * 1.20


class Moto(Vehiculo):
    def calcular_costo(self, dias):
        costo = self.tarifa * dias
        return costo * 0.85