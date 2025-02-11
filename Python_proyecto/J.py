import json
import funciones_a
# Función para abrir el archivo JSON
def abrirJSON():
    dicFinal={}
    with open(f"./campers.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open(f"./campers.json",'w') as outFile:
        json.dump(dic,outFile)



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
            print(f" Bienvenido de nuevo, {camper_encontrado['nombre']}!")
            print(funciones_a.menucamper())
        

if opt == "3":
    print("Bienvenido coordinador/a")
    id=print(input("Digita tu Id "))
    
    print ("¿Que deseas hacer?")
    print ("1. Ver grupos")
    print ("2. Asignar")
    opc = input (":")
    print(funciones_a.menucoordinador())
    
if opt == "2":
        print ("Bienvenido Trainer ")
        print ("Digita tu Id")

        print (funciones_a.menutrainer())

        
        



    
