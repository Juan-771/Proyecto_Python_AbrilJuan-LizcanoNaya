import modulo_camper 
import modulo_coordinador
import modulo_trainer


print("Bienvenido a CampusLands")
print("¿Cómo deseas ingresar?")
print("1. Camper")
print("2. Trainer")
print("3. Coordinador")
opt = input(": ")

if opt == "1":
    modulo_camper.inc()
            
elif opt == "2":
    modulo_trainer.inc()
    modulo_trainer.verificar_id()

elif opt == "3":
    modulo_coordinador.inc()
    modulo_coordinador.verificar_iden()