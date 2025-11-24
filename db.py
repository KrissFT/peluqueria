from transformador import Transformador

# Autor original de la clase DB: Emiliano Billi
class DB:
    def __init__(self, archivo, clase_elemento):
        self.archivo = archivo
        self.clase_elemento = clase_elemento
    
    def leer(self):
        db = []
        csv = open(self.archivo, "rt")
        linea = csv.readline()

        if linea == "":
            return db
        keys = linea.split(",")
        trans = Transformador(keys, self.clase_elemento)
        linea = csv.readline() 
        while linea != "":
            values = linea.split(",")
            obj = trans.a_objeto(values)
            if obj: 
                db.append(obj)
            linea = csv.readline()
        csv.close()
        return db
    
    def escribir_auto(self,elemento):
        csv = open(self.archivo, "at")
        csv.write(elemento.valores_para_csv()+"\n")
        csv.close()

    def escribir_completo(self, elementos):
        csv = open(self.archivo, "wt")
        encabezados = elementos[0].encabezados_para_csv()
        csv.write(encabezados+"\n")
        i = 0
        while i < len(elementos):
            csv.write(elementos[i].valores_para_csv()+"\n")
            i += 1
        csv.close()

    def eliminar_entrada(self, elemento_borrable):
        csv = open(self.archivo, "rt")
        lineas = csv.readlines()
        csv.close()
        
        valores = str(elemento_borrable)

        csv = open(self.archivo, "wt")
        for linea in lineas:
            if linea.strip("\n") != valores:
                csv.write(linea)
        csv.close()