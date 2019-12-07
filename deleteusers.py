#!/usr/bin/env python

# ------------------------------------------------------
#   Miguel A. Castellanos, Diciembre 2019
# ------------------------------------------------------

#
# Este codigo se creo para gestionar jupyterHub, lo que hace es eliminar los usuarios de jupyterhub que esten en un fichero

# > deleteusers.py fileWithUserNames

import os, sys

adminID = 'miguel'

# filename = "/home/miguel/Desktop/Desarrollo/pruebasPy/usersList.txt"

if len(sys.argv)-1 != 1:
    print('ERROR: Sintaxis: {} fileWithUserNames'.format(sys.argv[0])) 
    sys.exit()


filename = sys.argv[1]


with open(filename) as f:
    content = f.readlines()
f.close()

content = [x.strip() for x in content] 

print("-----------------------------------")
print("Borramos usuarios de jupyterHub")
for user in content:
    if adminID not in user:
        print("Borrando: " + user)
        os.system("deluser --remove-home jupyter-"+user)

print("Terminado")

