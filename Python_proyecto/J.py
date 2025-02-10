import json
from funciones import *
# Función para abrir el archivo JSON
def abrirJSON():
    dicFinal={}
    with open(f"./campers.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open(f"./campers.json",'w') as outFile:
        json.dump(dic,outFile)

'''def abrirJSON():
    dicFinal={}
    with open(f"./trainers.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open(f"./trainers.json",'w') as outFile:
        json.dump(dic,outFile)'''



print("Bienvenido a CampusLands")
print("¿Cómo deseas ingresar?")
print("1. Camper")
print("2. Trainer")
print("3. Coordinador")
opt = input(": ")

if opt == "1":
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
            if camper["numero_documento"] == numId:
                camper_encontrado = camper
                break
        
        if camper_encontrado:
            # Si el NumId se encuentra, iniciar sesión
            print(f" Bienvenido de nuevo, {camper_encontrado['Nombres']}!")
