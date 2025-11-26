import re

class Validador:
    def __init__(self):
        pass
    
    def validar_fecha(self,dato):
        if re.match(r"[0-9]{2}/[0-9]{2}/[0-9]{4}",dato) or re.match(r"[0-9]/[0-9]{2}/[0-9]{4}",dato) or re.match(r"[0-9]{2}/[0-9]/[0-9]{4}",dato) or re.match(r"[0-9]/[0-9]/[0-9]{4}",dato):
            return True
    
    def validar_hora(self,dato):
        if re.match(r"[0-9]{2}:[0-9]{2}",dato):
            return True

    def validar_nombre(self,dato):
        if dato.replace(" ", "").isalpha():
            return True
        else:
            print("El nombre ingresado es inválido")
            return False
