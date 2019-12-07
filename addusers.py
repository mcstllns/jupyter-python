#!/usr/bin/env python3

# ------------------------------------------------------
#   Miguel A. Castellanos, Diciembre 2019
# ------------------------------------------------------

#
# Este codigo se creo para gestionar jupyterHub, lo que hace es crear usuarios

# > addusers.py 
# Lee la configuracion de config.py
# ejecutar con privilegios

import os
import config


with open(config.usersFile) as f:
    content = f.readlines()
f.close()

content = [x.strip() for x in content]

print("")
print("------------------------------")
print("Se van a CREAR los siguientes usuarios :", content)
print(" ")
print("Desea crearlos? [y/n]: ")
ans = input()

if (ans == 'y'):
    for user in content:
        print("Creando: " + user)
        os.system("useradd  --create-home --user-group --groups jupyterhub-users jupyter-"+user)
else:
    print("No se ha creado ningun usuario")

print("Terminado") 

