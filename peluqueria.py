import sys

sys.path.insert(1, './classes/')

from peluquero import Peluquero 
from cliente import Cliente
from turno import Turno
from transformador import Transformador
from db import DB
from validador import Validador
from sistematurnos import SistemaTurnos

def main():
    sistema = SistemaTurnos()

    #Si bien la clase es DB, son a efectos prácticos las tablas del SQL
    bd_peluqueros = DB("./csv/datos_peluqueros.csv",Peluquero)
    bd_clientes = DB("./csv/datos_clientes.csv",Cliente)
    bd_turnos = DB("./csv/datos_turnos.csv",Turno)

    #carga automática
    sistema.peluqueros = bd_peluqueros.leer()
    sistema.clientes = bd_clientes.leer()
    sistema.turnos = bd_turnos.leer()

    trans_dt = Transformador(None,Turno)
    validador = Validador()

    while True:
        ok = False

        print("\nTurnos de peluquería")
        print("1. Añadir peluquero")
        print("2. Añadir cliente")
        print("3. Agendar turno")
        print("4. Modificar turno")
        print("5. Cancelar turno")
        print("6. Ver datos")
        print("7. Exportar y sobreescribir CSV")
        print("8. Importar de CSV")
        print("9. Salir")

        opcion = input("\nIngresa una opción: ")

        if opcion == '1':
            peluquero_id = len(sistema.peluqueros)


            while ok != True:
                nombre = input("Ingrese nombre del peluquero: ")
                ok = validador.validar_nombre(nombre)
            
            peluquero = sistema.agregar_peluquero(peluquero_id, nombre)
            bd_peluqueros.escribir_auto(peluquero)

        elif opcion == '2':
            cliente_id = len(sistema.clientes)
            
            while ok != True:
                nombre = input("Ingrese nombre de cliente: ")
                ok = validador.validar_nombre(nombre)

            cliente = sistema.agregar_cliente(cliente_id, nombre)
            bd_clientes.escribir_auto(cliente)

        elif opcion == '3':
            if len(sistema.turnos) == 0:
                turno_id = 0
            else:
                turno_max = sistema.buscar_turno_id_mayor()
                turno_id = turno_max + 1
                turno_id = str(turno_id) 

            while ok != True:
                print("\nPeluqueros existentes:")
                sistema.ver_peluqueros()
                peluquero_id = input("\nIngrese la ID del peluquero: ")
                
                print("\nClientes existentes:")
                sistema.ver_clientes()
                cliente_id = input("\nIngrese la ID de cliente: ")

                try:
                    int(peluquero_id)
                    int(cliente_id)
                except ValueError:
                    print("No ingresó una ID válida")
                ok = True

                prueba_p = sistema.buscar_peluquero(peluquero_id)
                prueba_c = sistema.buscar_cliente(cliente_id)

                if prueba_c == None or prueba_p == None:
                    print("La ID ingresada no forma parte de nuestras bases de datos.")
                    ok = False
            
            ok = False
            while ok != True:
                fecha = input("Ingrese fecha (Día/Mes/Año): ")
                hora = input("Ingrese horario (Horas:Minutos): ")
                
                fecha_valida = validador.validar_fecha(fecha)
                hora_valida = validador.validar_hora(hora)

                horario_disponible = validador.turno_disponible(trans_dt.adaptar_a_dt_ddmmyy(fecha, hora),sistema.turnos,peluquero_id)

                if fecha_valida and hora_valida and horario_disponible:
                    turno = sistema.agendar_turno(turno_id, peluquero_id, cliente_id, fecha, hora)
                    bd_turnos.escribir_auto(turno)
                    ok = True
                
                elif horario_disponible == False:
                    print("El turno solicitado se encuentra ocupado")

                else:
                    print("Uno o varios datos no siguen el formato correcto (DD/MM/YYYY HH:MM)")
            

        elif opcion == '4':
            print("\nTurnos a realizar:")
            sistema.ver_turnos_activos()

            turno_id_input = input("\nIngrese la ID del turno a modificar: ")
            turno = sistema.buscar_turno(turno_id_input)

            if turno == None:
               print("\nID inválida.")

            else:    
                print("\nOpciones de modificación")
                print("1. Modificar peluquero")
                print("2. Modificar fecha y hora")

                opcion_mod = input("\nIngresa una opción: ")
                    
                if opcion_mod == '1':

                   while ok != True:
                        print("\nPeluqueros existentes:")
                        sistema.ver_peluqueros()
                        peluquero_reemplazo = input("\nIngrese la ID del nuevo peluquero: ")
                        
                        if sistema.buscar_peluquero(peluquero_reemplazo) != None:
                            turno_viejo = turno.valores_para_csv()
                            turno_nuevo = sistema.modificar_turno_peluquero(turno.turno_id, peluquero_reemplazo)
                                
                            bd_turnos.eliminar_entrada(turno_viejo)
                            bd_turnos.escribir_auto(turno_nuevo)

                            ok = True
                            
                        else:
                            print("\nNo ingresó una ID válida.")

                elif opcion_mod == '2':
                    while ok != True:
                        fecha = input("Ingrese fecha nueva (Día/Mes/Año): ")
                        hora = input("Ingrese horario nuevo (Horas:Minutos): ")

                        fecha_valida = validador.validar_fecha(fecha)
                        hora_valida = validador.validar_hora(hora)

                        #validación de si están ocupadas
                        horario_disponible = validador.turno_disponible(trans_dt.adaptar_a_dt_ddmmyy(fecha, hora),sistema.turnos,peluquero_id)

                        if fecha_valida and hora_valida and horario_disponible:
                            turno_viejo = turno.valores_para_csv()
                            turno_nuevo = sistema.modificar_turno_fecha_hora(turno.turno_id,fecha,hora)
                            
                            bd_turnos.eliminar_entrada(turno_viejo)
                            bd_turnos.escribir_auto(turno_nuevo)

                            ok = True

                        elif horario_disponible == False:
                            print("El turno solicitado se encuentra ocupado")

                        else:
                            print("Uno o varios datos no siguen el formato correcto (DD/MM/YYYY HH:MM)")
                        
                else:
                    print("\nValor inválido.")

        elif opcion == '5':
            print("\nTurnos a realizar:")
            sistema.ver_turnos_activos()

            a_cancelar = input("\nIngrese la ID del turno a cancelar: ")
            turno_cancelable = sistema.buscar_turno(a_cancelar)
            
            if turno_cancelable != None:
                bd_turnos.eliminar_entrada(turno_cancelable.valores_para_csv())
                sistema.cancelar_turno(a_cancelar)
            else:
                print("El turno solicitado no se encuentra en la base de datos")
        
        elif opcion == '6':
            print("\nElija la lista a visualizar:")
            print("1. Peluqueros")
            print("2. Clientes")
            print("3. Turnos")

            opcion = input("\nIngresa una lista: ")

            if opcion == '1':
                sistema.ver_peluqueros()
            elif opcion == '2':
                sistema.ver_clientes()
            elif opcion == '3':
                print("\n1. Turnos de hoy")
                print("2. Turnos activos")
                print("3. Turno por peluquero")
                print("4. Turno por cliente")
                print("5. Todos los turnos")

                opcion_turno = input("\nIngrese una opción: ")

                if opcion_turno == '1':
                    sistema.ver_turnos_hoy()

                elif opcion_turno == '2':
                    sistema.ver_turnos_activos()

                elif opcion_turno == '3':
                    id_buscar = input("Ingrese la ID del peluquero:")
                    sistema.ver_turnos_peluquero(id_buscar)

                elif opcion_turno == '4':
                    id_buscar = input("Ingrese la ID del cliente: ")
                    sistema.ver_turnos_cliente(id_buscar)
                
                elif opcion_turno == '5':
                    sistema.ver_turnos()
            else:
                print("Opción inválida")
        
        elif opcion == '7':
            bd_peluqueros.escribir_completo(sistema.peluqueros)
            bd_clientes.escribir_completo(sistema.clientes)
            bd_turnos.escribir_completo(sistema.turnos)

        elif opcion == '8':
            sistema.peluqueros = bd_peluqueros.leer()
            sistema.clientes = bd_clientes.leer()
            sistema.turnos = bd_turnos.leer()

        elif opcion == '9':
            print("\nThunder Break")
            break
            
        else:
            print("\nValor inválido. Intente nuevamente")

if __name__ == "__main__":
    main()



