class Sucursal:
    def __init__(self, codigo, ciudad, direccion):
        self.codigo = codigo
        self.ciudad = ciudad
        self.direccion = direccion
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)