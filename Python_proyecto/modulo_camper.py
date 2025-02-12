import funciones_a
import json

def abrirJSON():
    dicFinal={}
    with open(f"./campers.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open(f"./campers.json",'w') as outFile:
        json.dump(dic,outFile)
def inc():
    print("Bienvenido camper")
    print("1. Iniciar sesión")
    
    opc = input(": ")
    if opc == "1":
        datos = abrirJSON()

        # Solicitar el Número de Identificación para iniciar sesión
        numId = input("Ingresa tu Número de Identificación: ")

        # Verificar si el numero_documento existe en la lista de campers
        camper_encontrado = None
        for camper in datos["campers"]:
            if camper["Numero_documento"] == numId:
                camper_encontrado = camper
                break
        
        if camper_encontrado:
            # Si el NumId se encuentra, iniciar sesión
            print(f" Bienvenido de nuevo, {camper_encontrado['Nombre']}!")
            print(funciones_a.menucamper())
            