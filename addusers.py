#!/usr/bin/env python

# ------------------------------------------------------
#   Miguel A. Castellanos, Diciembre 2019
# ------------------------------------------------------

#
# Este codigo se creo para gestionar jupyterHub, lo que hace es manetener actualizados los
# directorios de los usuarios

# > addusers.py fileWithUserNames

# Cuando se ejecuta va a borrar lo que hay en el home de los usuarios
# de jupyter y poner lo que hay en la carpeta path/to/src

import os


#f = open("/home/miguel/Desktop/Desarrollo/pruebasPy/usersList.txt", "r")

filename = "/home/miguel/Desktop/Desarrollo/pruebasPy/usersList.txt"


with open(filename) as f:
    content = f.readlines()
f.close()

content = [x.strip() for x in content] 

print("Creamos nuevos usuarios de jupyterHub")
for user in content:
    print("Creando: " + user)
    os.system("useradd  --create-home --user-group --groups jupyterhub-users jupyter-"+user)

print("Terminado")
