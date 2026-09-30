# Trabajo Integrador - Programacion II

# Sistema de alquiler de vehiculos

Este proyecto corresponde al Trabajo Integrador de las Unidades 1 y 2 de Programacion II.

El programa representa de forma simple un sistema de alquiler de vehiculos, donde se pueden registrar clientes, vehiculos, sucursales y reservas.

# Funcionalidades

El sistema permite:

Crear clientes.
Crear distintos tipos de vehiculos.
Agregar vehiculos a una sucursal.
Crear reservas.
Calcular el costo de un alquiler.
Cambiar el estado de una reserva.
Guardar un historial de los cambios de estado.
Validar algunos datos incorrectos.

# Tipos de vehiculos

El sistema cuenta con tres tipos de vehiculos:

Auto
Camioneta
Moto

Todos heredan de la clase Vehiculo.

Cada uno calcula el costo de alquiler de una manera diferente:

Auto: utiliza la tarifa normal.
Camioneta: tiene un recargo del 20%.
Moto: tiene un descuento del 15%.

# Estados

Para manejar los estados se utilizaron Enum.

Los estados de los vehiculos son:
DISPONIBLE
RESERVADO
EN_ALQUILER
FUERA_DE_SERVICIO

Los estados de las reservas son:
SOLICITADA
CONFIRMADA
EN_CURSO
FINALIZADA
CANCELADA

# Clases utilizadas

Las principales clases del programa son:
Cliente
Vehiculo
Auto
Camioneta
Moto
Sucursal
Reserva
RegistroHistorial

# Conceptos utilizados

Durante el desarrollo del trabajo se utilizaron distintos conceptos de Programacion Orientada a Objetos:
Clases y objetos.
Herencia.
Polimorfismo.
Encapsulamiento.
Enum.
Listas de objetos.

El polimorfismo se utiliza principalmente en el metodo calcular_costo(), ya que cada tipo de vehiculo realiza el calculo de una manera diferente.

# Archivos del proyecto

El proyecto esta dividido en los siguientes archivos:
main.py
cliente.py
vehiculos.py
sucursal.py
reserva.py
historial.py
enums.py

# Ejecucion

Para ejecutar el programa hay que abrir una terminal dentro de la carpeta del proyecto y ejecutar:

python3 main.py

El archivo main.py crea los objetos necesarios y realiza distintas pruebas para comprobar el funcionamiento del sistema.