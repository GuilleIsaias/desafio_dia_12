from usuario import Usuario
import json
import os

log_file = open(os.path.abspath("logs/error.log"))
instancias = []

with open("usuarios.txt") as usuarios:
    linea = usuarios.readline()

    while linea:
        users = json.loads(linea)
        instancias.append(Usuario(users.get("nombre"), users.get("apellido"),users.get("email"),users.get("genero")))
        linea = usuarios.readline()        


print(instancias)
