class Turno:
    def __init__(self, turno_id, peluquero, cliente, fecha, hora):
        self.turno_id = turno_id
        self.peluquero = peluquero
        self.cliente = cliente
        self.fecha = fecha
        self.hora = hora

    def __str__(self):
        return f"ID Turno: {self.turno_id}, Peluquero: {self.peluquero}, Cliente: {self.cliente}, Fecha: {self.fecha}, Hora: {self.hora}"
        #TODO modificar los datos que llegan al __str__ para que figuren los nombres en vez de ID

    def encabezados_para_csv(self):
        return "turno_id,peluquero,cliente,fecha,hora"

    def valores_para_csv(self):
        return f"{self.turno_id},{self.peluquero},{self.cliente},{self.fecha},{self.hora}"