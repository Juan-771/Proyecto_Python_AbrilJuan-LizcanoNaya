import funciones_a
import json

def abrirJSON():
    dicFinal={}
    with open(f"./trainers.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open(f"./trainers.json",'w') as outFile:
        json.dump(dic,outFile)
data=abrirJSON

def inc():
    print ("Bienvenido Trainer ")
    
        
        

def verificar_id():
    while True:
        id_usuario = input("\nDame tu ID: ")  # Pedir el ID
        data = abrirJSON()
        # Buscar el ID dentro de los entrenadores
        if any(trainer["id"] == id_usuario for trainer in data["trainers"]):
            print("ID válido. Bienvenido.")
            print(funciones_a.menutrainer())
            break
            
        else:
            print("ID no válido. Inténtalo de nuevo.")

