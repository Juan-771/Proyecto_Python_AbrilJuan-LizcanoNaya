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
            "numero_documento": input("Ingresa tu Número de Identificación: "),
            "Nombres": input("Ingresa tus nombres: "),
            "Apellidos": input("Ingresa tus apellidos: "),
            "Direccion": input("Ingresa la dirección de tu vivienda: "),
            "Acudiente": input("Ingresa el nombre de tu acudiente: "),
            "Telefonos": input("Ingresa tu número de teléfono: ")
        }

        
        datos["campers"].append(nuevo_camper)

        
        guardarJSON(datos)

        print(" Nuevo camper registrado correctamente.")

    elif opc == "1":
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
        else:
            print("El Número de Identificación no está registrado.")
            opc_registrar = input("¿Deseas registrarte? (1. Sí, 2. No): ")
            if opc_registrar == "1":
                # Si no está registrado, permitir el registro
                nuevo_camper = {
                    "numero_documento": numId,
                    "Nombres": input("Ingresa tus nombres: "),
                    "Apellidos": input("Ingresa tus apellidos: "),
                    "Direccion": input("Ingresa la dirección de tu vivienda: "),
                    "Acudiente": input("Ingresa el nombre de tu acudiente: "),
                    "Telefonos": input("Ingresa tu número de teléfono: ")
                }

                # Añadir el nuevo camper a la lista de campers
                datos["campers"].append(nuevo_camper)

                # Guardar los datos actualizados en el archivo JSON
                guardarJSON(datos)

                print(" Nuevo camper registrado correctamente.")
elif opt == "2":
    










