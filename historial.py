from datetime import datetime


class RegistroHistorial:
    def __init__(self, estado, descripcion):
        ahora = datetime.now()

        self.fecha = ahora.date()
        self.hora = ahora.time()
        self.estado = estado
        self.descripcion = descripcion