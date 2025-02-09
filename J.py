import json

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
    print("2. Registrarse")
    opc = input(": ")

    if opc == "2":
        
        datos = abrirJSON()

        
        nuevo_camper = {
            "NumId": input("Ingresa tu Número de Identificación: "),
            "Nombres": input("Ingresa tus nombres: "),
            "Apellidos": input("Ingresa tus apellidos: "),
            "Direccion": input("Ingresa la dirección de tu vivienda: "),
            "Acudiente": input("Ingresa el nombre de tu acudiente: "),
            "Telefonos": input("Ingresa tu número de teléfono: ")
        }

        
        datos["campers"].append(nuevo_camper)

        
        guardarJSON(datos)

        print(" Nuevo camper registrado correctamente.")
        
        





    









