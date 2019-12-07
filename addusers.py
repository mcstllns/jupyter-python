#!/usr/bin/env python

# ------------------------------------------------------
#   Miguel A. Castellanos, Diciembre 2019
# ------------------------------------------------------

#
# Este codigo se creo para gestionar jupyterHub, lo que hace es crear usuarios

# > addusers.py fileWithUserNames


import os, sys

# filename = "/home/miguel/Desktop/Desarrollo/pruebasPy/usersList.txt"


if len(sys.argv)-1 != 1:
    print('ERROR: Sintaxis: {} fileWithUserNames'.format(sys.argv[0])) 
    sys.exit()


filename = sys.argv[1]

print("-----------------------------------")

with open(filename) as f:
    content = f.readlines()
f.close()

content = [x.strip() for x in content] 

print("Creamos nuevos usuarios de jupyterHub")
for user in content:
    print("Creando: " + user)
    os.system("useradd  --create-home --user-group --groups jupyterhub-users jupyter-"+user)

print("Terminado")
