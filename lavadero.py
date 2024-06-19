import os
import json
def limpiarPantalla():
    os.system("cls" if os.name == "nt" else  "clear")
def menu():
    print("1. para ingresar vehiculo")
    print("2. para retirar vehiculo")
    print("3. para listar vehiculos")
    print("4. para cambiar estado")
    print("5. para salir")
    opcion=input("seleccione una opcion: ")
    return opcion
def guardarDatos(vehiculos):
    with open("vehiculos.json","w") as file:
        json.dump(vehiculos, file,indent=4)
    return
def cargarDatos():
    try:
        with open("vehiculos.json", "r") as file:
            return json.load(file)
    except:
        return {}
def ingresarVehiculo():
    print("Ingreso de vehiculos".center(50," "))
    patente=input("ingrese la patente del vehiculo: ")
    interior=input("lavado interior s/n: ")
    exterior=input("lavado exterior s/n: ")
    motor=input("lavado motor s/n: ")
    encerado=input("encerado s/n: ")
    estado="pendiente"
    telefono=input("ingrese el num de telefono: ")
    vehiculos[patente]={
        "interior":interior,
        "exterior":exterior,
        "motor":motor,
        "encerado":encerado,
        "estado":estado,
        "telefono":telefono
    }
    guardarDatos(vehiculos)
    return
def cambiarEstado(vehiculos):
    print("cambio de estados".center(50," "))
    patente=input("ingrese la patente: ")
    if patente in vehiculos:
        print(f"patente: {patente}, estado: {vehiculos[patente]['estado']}")
        estado=input("ingrese el nuevo estado proceso/terminado/entregado: ")
        vehiculos[patente]["estado"]=estado
        guardarDatos(vehiculos)
        input("datos guardados correctamente, enter para continuar")
    else:
        input("vehiculo no registrado!  enter para continuar")

    



#programa principal

limpiarPantalla()
vehiculos=cargarDatos()
print(vehiculos)
while True:
    opcion=menu()
    if opcion=="1":
        ingresarVehiculo()
    elif opcion=="2":
        pass
        #retirarVehiculo()
    elif opcion=="3":
        pass
        #listarVehiculos()
    elif opcion=="4":
        cambiarEstado(vehiculos)
    elif opcion == "5":
        break
    else:
        print("opcion no valida!")

