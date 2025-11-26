class Peluquero:
    def __init__(self, peluquero_id, nombre):
        self.peluquero_id = peluquero_id
        self.nombre = nombre

    def __str__(self):
        return f"ID Peluquero: {self.peluquero_id}, Nombre: {self.nombre}"
    
    def encabezados_para_csv(self):
        return "peluquero_id,nombre"
    
    def valores_para_csv(self):
        return f"{self.peluquero_id},{self.nombre}"