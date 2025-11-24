from peluquero import Peluquero 
from cliente import Cliente
from turno import Turno
from transformador import Transformador
from db import DB
from sistematurnos import SistemaTurnos

def main():
    sistema = SistemaTurnos()
    #TODO experimentar para tener todo en una misma instancia de BD
    bd_peluqueros = DB("./csv/datos_peluqueros.csv",Peluquero)
    bd_clientes = DB("./csv/datos_clientes.csv",Cliente)
    bd_turnos = DB("./csv/datos_turnos.csv",Turno)

    #carga automática
    sistema.peluqueros = bd_peluqueros.leer()
    sistema.clientes = bd_clientes.leer()
    sistema.turnos = bd_turnos.leer()

    #TODO acotar la botonera
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
        print("9. Exportar y sobreescribir CSV")
        print("10 Importar de CSV")
        print("11. Salir")

        opcion = input("\nIngresa una opción: ")

        if opcion == '1':
            peluquero_id = len(sistema.peluqueros)
            nombre = input("Ingrese nombre del peluquero: ")
            peluquero = sistema.agregar_peluquero(peluquero_id, nombre)
            bd_peluqueros.escribir_auto(peluquero)

        elif opcion == '2':
            cliente_id = len(sistema.clientes)
            nombre = input("Ingrese nombre de cliente: ")
            cliente = sistema.agregar_cliente(cliente_id, nombre)
            bd_clientes.escribir_auto(cliente)

        elif opcion == '3':
            if len(sistema.turnos) == 0:
                turno_id = 0
            else:
                turno_max = sistema.buscar_turno_id_mayor()
                turno_id = turno_max + 1
                turno_id = str(turno_id) 
            #agregar excepción para no ints
            peluquero_id = input("Ingrese la ID del peluquero: ")
            cliente_id = input("Ingrese la ID de cliente: ")
            #implementar datetime, validar ingresos
            fecha = input("Ingrese fecha (Día/Mes/Año): ")
            hora = input("Ingrese horario (Horas:Minutos): ")
            turno = sistema.agendar_turno(turno_id, peluquero_id, cliente_id, fecha, hora)
            bd_turnos.escribir_auto(turno)

        elif opcion == '4':
            #agregar excepción para no ints
            turno_id_input = input("Ingrese la ID del turno a modificar: ")
            turno = sistema.buscar_turno(turno_id_input)

            if turno == None:
                print("\nID inválida.")
            else:    
                print("\nOpciones de modificación")
                print("1. Modificar peluquero")
                print("2. Modificar fecha y hora")

                opcion_mod = input("\nIngresa una opción: ")
                
                if opcion_mod == '1':
                    peluquero_reemplazo = input("Ingrese la ID del nuevo peluquero: ")
                    if sistema.buscar_peluquero(peluquero_reemplazo) != None:
                        turno_viejo = turno.valores_para_csv()
                        turno_nuevo = sistema.modificar_turno_peluquero(turno.turno_id, peluquero_reemplazo)
                        bd_turnos.eliminar_entrada(turno_viejo)
                        bd_turnos.escribir_auto(turno_nuevo)
                    else:
                        print("\nID inválida.")
                elif opcion_mod == '2':
                    fecha = input("Ingrese fecha nueva (Día/Mes/Año): ")
                    hora = input("Ingrese horario nuevo (Horas:Minutos): ")
                    #TODO validaciones y excepciones
                    turno_viejo = turno.valores_para_csv()
                    turno_nuevo = sistema.modificar_turno_fecha_hora(turno.turno_id,fecha,hora)
                    bd_turnos.eliminar_entrada(turno_viejo)
                    bd_turnos.escribir_auto(turno_nuevo)
                else:
                    print("\nValor inválido.")

        elif opcion == '5':
            a_cancelar = input("Ingrese la ID del turno a cancelar: ")
            turno_cancelable = sistema.buscar_turno(a_cancelar)
            bd_turnos.eliminar_entrada(turno_cancelable.valores_para_csv())
            sistema.cancelar_turno(a_cancelar)
        
        elif opcion == '6':
            sistema.ver_peluqueros()

        elif opcion == '7':
            sistema.ver_clientes()

        elif opcion == '8':
            sistema.ver_turnos()
        
        elif opcion == '9':
            bd_peluqueros.escribir_completo(sistema.peluqueros)
            bd_clientes.escribir_completo(sistema.clientes)
            bd_turnos.escribir_completo(sistema.turnos)

        elif opcion == '10':
            sistema.peluqueros = bd_peluqueros.leer()
            sistema.clientes = bd_clientes.leer()
            sistema.turnos = bd_turnos.leer()

        elif opcion == '11':
            print("\nThunder Break")
            break
            
        else:
            print("\nValor inválido. Intente nuevamente")

if __name__ == "__main__":
    main()



