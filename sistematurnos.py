from peluquero import Peluquero
from cliente import Cliente
from turno import Turno

class SistemaTurnos:
    def __init__(self):
        self.peluqueros = []
        self.clientes = []
        self.turnos = []

    def agregar_peluquero(self, peluquero_id, nombre):
        peluquero = Peluquero(peluquero_id, nombre)
        self.peluqueros.append(peluquero)
        return peluquero

    def agregar_cliente(self, cliente_id, nombre):
        cliente = Cliente(cliente_id, nombre)
        self.clientes.append(cliente)
        return cliente

    def buscar_peluquero(self, peluquero_id):
        for p in self.peluqueros:
            if p.peluquero_id == peluquero_id:
                return p
        return None

    def buscar_cliente(self, cliente_id):
        for c in self.clientes:
            if c.cliente_id == cliente_id:
                return c
        return None

    def buscar_turno(self, turno_id):
        for t in self.turnos:
            if t.turno_id == turno_id:
                return t
        return None

    def buscar_turno_id_mayor(self):
        mayor_encontrado = 0
        for t in self.turnos:
            if int(t.turno_id) > mayor_encontrado:
                mayor_encontrado = int(t.turno_id)
        return mayor_encontrado
    
    def agendar_turno(self, turno_id, peluquero_id, cliente_id, fecha, hora):
        peluquero = self.buscar_peluquero(peluquero_id)
        cliente = self.buscar_cliente(cliente_id)

        if peluquero and cliente:
            turno = Turno(turno_id, peluquero.peluquero_id, cliente.cliente_id, fecha, hora)
            self.turnos.append(turno)
            print(f"Turno agendado: {turno}")
            return turno
        else:
            print("Peluquero o cliente no encontrado")

    def modificar_turno_peluquero(self, turno_id, peluquero_reemplazo):
        turno_modificable = self.buscar_turno(turno_id)
        self.turnos.remove(turno_modificable)
        turno_modificable.peluquero = peluquero_reemplazo
        self.turnos.append(turno_modificable)
        print(f"Turno actualizado: {turno_modificable}")
        return turno_modificable

    def modificar_turno_fecha_hora(self, turno_id, nueva_fecha, nueva_hora):
        turno_modificable = self.buscar_turno(turno_id)
        self.turnos.remove(turno_modificable)
        turno_modificable.hora = nueva_hora
        turno_modificable.fecha = nueva_fecha
        self.turnos.append(turno_modificable)
        print(f"Turno actualizado: {turno_modificable}")
        return turno_modificable

    def cancelar_turno(self, id_a_cancelar):
        turno_a_cancelar = self.buscar_turno(id_a_cancelar)
        self.turnos.remove(turno_a_cancelar)

    def ver_peluqueros(self):
        for peluquero in self.peluqueros:
            print(peluquero)

    def ver_clientes(self):
        for cliente in self.clientes:
            print(cliente)

    def ver_turnos(self):
        for turno in self.turnos:
            print(turno)