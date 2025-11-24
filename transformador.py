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
            valor_limpio = values[i].strip()
            datos[self.keys[i].strip()] = valor_limpio
            i = i + 1
        
        obj = self.clase_elemento(**datos)
        print(obj)
        return obj