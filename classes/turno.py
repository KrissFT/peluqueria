import datetime

class Turno:
    def __init__(self, turno_id, peluquero, cliente, fecha):
        self.turno_id = turno_id
        self.peluquero = peluquero
        self.cliente = cliente
        self.fecha_hora = fecha

    def __str__(self):
        return f"ID Turno: {self.turno_id}, Peluquero: {self.peluquero}, Cliente: {self.cliente}, Fecha y hora: {self.fecha_hora.strftime("%d/%m/%y %H:%M")}"
   

    def encabezados_para_csv(self):
        return "turno_id,peluquero,cliente,fecha,hora"

    def valores_para_csv(self):
        datos = str(self.fecha_hora)
        datos = datos.split(" ")

        fecha = datos[0]
        hora = datos[1]
        
        return f"{self.turno_id},{self.peluquero},{self.cliente},{fecha},{hora}"