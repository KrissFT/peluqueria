
class Peluquero:
    def __init__(self, peluquero_id, nombre):
        self.peluquero_id = peluquero_id
        self.nombre = nombre

    def __str__(self):
        return f"ID Peluquero: {self.peluquero_id}, Nombre: {self.nombre}"


class Cliente:
    def __init__(self, cliente_id, nombre):
        self.cliente_id = cliente_id
        self.nombre = nombre

    def __str__(self):
        return f"ID Ciente: {self.cliente_id}, Nombre: {self.nombre}"


class Turno:
    def __init__(self, turno_id, peluquero, cliente, fecha, hora):
        self.turno_id = turno_id
        self.peluquero = peluquero
        self.cliente = cliente
        self.fecha = fecha
        self.hora = hora

    def __str__(self):
        return f"ID Turno: {self.turno_id}, Peluquero: {self.peluquero.nombre}, Cliente: {self.cliente.nombre}, Fecha: {self.fecha}, Hora: {self.hora}"


class SistemaTurnos:
    def __init__(self):
        self.peluqueros = []
        self.clientes = []
        self.turnos = []

    def agregar_peluquero(self, peluquero_id, nombre):
        peluquero = Peluquero(peluquero_id, nombre)
        self.peluqueros.append(peluquero)

    def agregar_cliente(self, cliente_id, nombre):
        cliente = Cliente(cliente_id, nombre)
        self.clientes.append(cliente)

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
    
    def agendar_turno(self, turno_id, peluquero_id, cliente_id, fecha, hora):
        peluquero = self.buscar_peluquero(peluquero_id)
        cliente = self.buscar_cliente(cliente_id)

        if peluquero and cliente:
            turno = Turno(turno_id, peluquero, cliente, fecha, hora)
            self.turnos.append(turno)
            print(f"Turno agendado: {turno}")
        else:
            print("Peluquero o cliente no encontrado")

    def modificar_turno_peluquero(self, turno_id, peluquero_reemplazo):
        turno_modificable = self.buscar_turno(turno_id)
        self.turnos.remove(turno_modificable)
        turno_modificable.peluquero_id = peluquero_reemplazo
        self.turnos.append(turno_modificable)
        print(f"Turno actualizado: {turno_modificable}")

    def modificar_turno_fecha_hora(self, turno_id, fecha, hora):
        pass
    def ver_peluqueros(self):
        for peluquero in self.peluqueros:
            print(peluquero)

    def ver_clientes(self):
        for cliente in self.clientes:
            print(cliente)

    def ver_turnos(self):
        for turno in self.turnos:
            print(turno)



def main():
    sistema = SistemaTurnos()

    #Hice esto a la rápida pero no me gusta tener así nomás un while True
    while True:
        print("\nTurnos de peluquería")
        print("1. Añadir peluquero")
        print("2. Añadir cliente")
        print("3. Agendar turno")
        print("4. Modificar turno")
        print("5. Cancelar turno")
        print("6. Ver peluqueros")
        print("7. Ver clientes")
        print("8. Ver turnos")
        print("9. Salir")

        opcion = input("\nIngresa una opción: ")

        if opcion == '1':
            peluquero_id = len(sistema.peluqueros)
            nombre = input("Ingrese nombre del peluquero: ")
            sistema.agregar_peluquero(peluquero_id, nombre)

        elif opcion == '2':
            cliente_id = len(sistema.clientes)
            nombre = input("Ingrese nombre de cliente: ")
            sistema.agregar_cliente(cliente_id, nombre)

        elif opcion == '3':
            turno_id = len(sistema.turnos)
            #agregar excepción para no ints
            peluquero_id = int(input("Ingrese la ID del peluquero: "))
            cliente_id = int(input("Ingrese la ID de cliente: "))
            #implementar datetime, validar ingresos
            fecha = input("Ingrese fecha (Día/Mes/Año): ")
            hora = input("Ingrese horario (Horas:Minutos): ")
            sistema.agendar_turno(turno_id, peluquero_id, cliente_id, fecha, hora)

        elif opcion == '4':
            #agregar excepción para no ints
            #agregar buscar_turno para validar input
            turno_id_input = int(input("Ingrese la ID del turno a modificar: "))
            turno = sistema.buscar_turno(turno_id_input)

            if turno != None:
                print("\nOpciones de modificación")
                print("1. Modificar peluquero")
                print("2. Modificar fecha y hora")

                opcion_mod = input("\nIngresa una opción: ")
                
                if opcion_mod == '1':
                    peluquero_reemplazo = int(input("Ingrese la ID del nuevo peluquero: "))
                    if sistema.buscar_peluquero(peluquero_reemplazo) != None:
                        sistema.modificar_turno_peluquero(turno.turno_id, peluquero_reemplazo)
                    else:
                        print("\nID inválida.")
                elif opcion_mod == '2':
                    sistema.modificar_turno_fecha_hora(turno_id,fecha,hora)
                else:
                    print("\nValor inválido.")
            else:
                print("\nID inválida.")

        elif opcion == '6':
            sistema.ver_peluqueros()

        elif opcion == '7':
            sistema.ver_clientes()

        elif opcion == '8':
            sistema.ver_turnos()

        elif opcion == '9':
            print("\nThunder Break")
            break
            

        else:
            print("\nValor inválido. Intente nuevamente")


if __name__ == "__main__":
    main()



