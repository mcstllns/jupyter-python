#!/usr/bin/env python

# ------------------------------------------------------
#   Miguel A. Castellanos, Diciembre 2019
# ------------------------------------------------------

#
# Este codigo se creo para gestionar jupyterHub, lo que hace es manetener actualizados los
# directorios de los usuarios

# > update.py path/to/src

# Cuando se ejecuta va a borrar lo que hay en el home de los usuarios
# de jupyter y poner lo que hay en la carpeta path/to/src

# A los que pertenecen al grupo jupyterhub-admins no se les actualiza


# OJO: Si la carpeta ya existe no va a funcionar

import sys, os, shutil

Dst = "/home"
cadID = 'jupyter-'
adminID = 'miguel'

if len(sys.argv)-1 != 1:
    print('Sintaxis: {} pathToSrc'.format(sys.argv[0])) 
    sys.exit()


Src = sys.argv[1]
print("-----------------------------------")
print("Source: " + Src)

# -----------------------------------------------------------------
def getSrc(path):
    folders = []
    files = []
    for r, d, f in os.walk(path):
        for fol in d:
            folders.append(os.path.join(r, fol))
        for fil in f:
            files.append(os.path.join(r, fil))
    return { 'folders': folders, 'files': files}


def getUsers(path):
    USERS = []
    for r, d, f in os.walk(path):
        for fol in d:
            if cadID in fol:
                uri = os.path.join(r, fol)
                user = {'home': uri,
                        'owner': os.stat(uri).st_uid,
                        'group': os.stat(uri).st_gid}
                USERS.append(user)
        break
    return USERS


def changeOwner(Dest, owner, group):
    # os.chown(Dest, info['owner'], info['group'])
    for root, dirs, files in os.walk(Dest):
        for d in dirs:
            os.chown(os.path.join(root,d), owner, group)
        for f in files:
            os.chown(os.path.join(root,f), owner, group)


def deleteHome(path):
  for root, dirs, files in os.walk(path):
   for f in files:
    os.unlink(os.path.join(root, f))
   for d in dirs:
    shutil.rmtree(os.path.join(root, d))

# -----------------------------------------------------------------

SrcStruct = getSrc(Src)
Users = getUsers(Dst)
print(Users)

dirs = SrcStruct['folders']
files = SrcStruct['files']


for user in Users:
    if adminID not in user['home']:
        print('Updating:  ' + user['home'])
        
        # deleteHome(user['home'])

        for d in dirs: 
            try:
                os.mkdir(user['home'] + '/' + d.replace(Src,''))
            except OSError:
                pass
        for f in files:
            shutil.copyfile(f, user['home'] + '/' + f.replace(Src,''))
        changeOwner(user['home'], user['owner'], user['group'])

