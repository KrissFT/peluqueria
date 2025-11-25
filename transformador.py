import datetime

# Autor original de la clase Transformador: Emiliano Billi
class Transformador:
    def __init__(self, atributos, clase_elemento):
        self.keys = atributos
        self.clase_elemento = clase_elemento

    def a_dict(self, values):
        if len(values) != len(self.keys):
            return None
        dict = {}
        i = 0
        while i < len(values):
            dict[self.keys[i]] = values[i]
            i = i + 1
        return dict
    
    def a_objeto(self, values):
        if len(values) != len(self.keys):
            return None
        
        datos = {}
        i = 0
        while i < len(values):
            if type(values[i]) is str:
                valor_limpio = values[i].strip()
            else:
                valor_limpio = values[i]
            datos[self.keys[i].strip()] = valor_limpio
            i = i + 1
        print(datos)
        obj = self.clase_elemento(**datos)
        print(obj)
        return obj
    
    def adaptar_a_dt(self, values):
        lista_fecha = values[3].split("-")
        datos_hora = values[4].split(":")

        if datos_hora[1] == "00":
            fecha_hora = datetime.datetime(int(lista_fecha[0]),int(lista_fecha[1]),int(lista_fecha[2]),int(datos_hora[0]))
            return fecha_hora
        fecha_hora  = datetime.datetime(int(lista_fecha[0]),int(lista_fecha[1]),int(lista_fecha[2]),int(datos_hora[0]), int(datos_hora[1]))
        return fecha_hora

    def adaptar_a_dt_ddmmyy(self, fecha, hora):
        lista_fecha = fecha.split("/")
        datos_hora = hora.split(":")

        if datos_hora[1] == "00":
            fecha_hora = datetime.datetime(int(lista_fecha[2]),int(lista_fecha[1]),int(lista_fecha[0]),int(datos_hora[0]))
            return fecha_hora
        fecha_hora  = datetime.datetime(int(lista_fecha[2]),int(lista_fecha[1]),int(lista_fecha[0]),int(datos_hora[0]), int(datos_hora[1]))
        return fecha_hora