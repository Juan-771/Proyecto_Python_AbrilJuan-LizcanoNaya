import json
import funciones_a
def abrirJSON():
    dicFinal={}
    with open(f"./coordinador.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open(f"./coordinador.json",'w') as outFile:
        json.dump(dic,outFile)
data=abrirJSON


def inc():
    print("Bienvenido coordinador/a")

def verificar_iden():
    while True:
        id_usuario = input("\nDame tu ID: ")
        data = abrirJSON()

        if any(coordinador["id"] == id_usuario for coordinador in data["coordinador"]):

            print("ID válido. Bienvenido.")

            print(funciones_a.menucoordinador())

            break
        else:
            print("ID no válido. Inténtalo de nuevo.")
            break

    