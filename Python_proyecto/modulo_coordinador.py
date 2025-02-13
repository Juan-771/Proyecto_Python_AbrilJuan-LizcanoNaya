import json

def abrirJSON():
    dicFinal={}
    with open(f"./coordinador.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open(f"./coordinador.json",'w') as outFile:
        json.dump(dic,outFile)
data=abrirJSON()




def inc():
    print("Bienvenido coordinador/a")

def verificar_iden():
    while True:
        id_usuario = input("\nDame tu ID: ")
        data = abrirJSON()

        if any(coordinador["id"] == id_usuario for coordinador in data["coordinador"]):

            print("ID válido. Bienvenido.")
            
            print("\n1. ver lista de estudiantes")
            print("2. ver horarios trainers")
            print("3. ver notas ")
            print("4. ver grupos")
            print("5. ver rutas")
            print("6. salir")
            mio=input("\nQue quieres hacer? ")
            if mio == "1":
                ListaDeEstudiantes(data)
            break
        else:
            print("ID no válido. Inténtalo de nuevo.")
            break

'''def abrirJSON():
    """Abre y carga el archivo campers.json."""
    try:
        with open("campers.json", "r", encoding="utf-8") as file:
            return json.load(file)  # Cargar JSON
    except FileNotFoundError:
        print("Error: El archivo 'campers.json' no se encontró.")
        return {}
    except json.JSONDecodeError:
        print("Error: El archivo 'campers.json' no tiene un formato JSON válido.")
        return {}
    except Exception as e:
        print(f"Error inesperado al abrir el JSON: {e}")
        return {}'''

def abrirJSON():
    dicFinal={}
    with open(f"./coordinador.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open(f"./coordinador.json",'w') as outFile:
        json.dump(dic,outFile)

def ListaDeEstudiantes(data):
    """Imprime el JSON completo en formato legible."""
    try:
        print(json.dumps(data, indent=4, ensure_ascii=False))  # Imprime el JSON formateado
    except Exception as e:
        print(f"Error al imprimir el JSON: {e}")

# Cargar JSON y llamar a la función ListaDeEstudiantes
data = abrirJSON()

