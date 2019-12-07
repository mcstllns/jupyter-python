#!/usr/bin/env python3

# ------------------------------------------------------
#   Miguel A. Castellanos, Diciembre 2019
# ------------------------------------------------------

#
# Este codigo se creo para gestionar jupyterHub, lo que hace es eliminar los usuarios de jupyterhub que esten en un fichero

# > deleteusers.py fileWithUserNames


import os
import config


with open(config.usersFile) as f:
    content = f.readlines()
f.close()

content = [x.strip() for x in content] 

print("")
print("------------------------------")
print("Se van a ELIMINAR los siguientes usuarios :", content)
print(" ")
print("Desea eliminarlos? [y/n]: ")
ans = input()

if (ans == 'y'):
    for user in content:
        print("Eliminando: " + user)
        os.system("deluser --remove-home jupyter-"+user)
else:
    print("No se ha eliminado ningun usuario")

print("Terminado") 




