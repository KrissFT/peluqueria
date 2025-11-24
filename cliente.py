class Cliente:
    def __init__(self, cliente_id, nombre):
        self.cliente_id = cliente_id
        self.nombre = nombre

    def __str__(self):
        return f"ID Ciente: {self.cliente_id}, Nombre: {self.nombre}"
    
    def encabezados_para_csv(self):
        return "cliente_id,nombre"

    def valores_para_csv(self):
        return f"{self.cliente_id},{self.nombre}"