class ServicioNotificacion:
    def notificar(self, cliente, mensaje):
        print("Notificacion para", cliente.nombre)
        print(mensaje)