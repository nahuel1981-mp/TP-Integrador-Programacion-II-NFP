class Cliente:
    def __init__(self, nombre, apellido, dni, telefono, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.telefono = telefono
        self.correo = correo
        self.reservas = []

    def agregar_reserva(self, reserva):
        self.reservas.append(reserva)