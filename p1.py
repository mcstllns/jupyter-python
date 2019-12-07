#!/usr/bin/env python

import sys, os, shutil

cadID = 'jupyter-'
"""
pathOrigin = "/home/miguel/Desktop/Desarrollo/kk/origen/"
# pathDest = "/home/miguel/Desktop/Desarrollo/kk/home"
pathDest = "/home"
#dirDest = os.path.split(pathOrigin)[1])
dirDest = 'copiaOrigen'
"""

if len(sys.argv)-1 != 3:
    print('Sintaxis: {} DirectorioOrigen PathconCuentasJupyter(normalmente /home) DirectorioDestino'.format(sys.argv[0])) 
    sys.exit()

pathOrigin = sys.argv[1]
pathDest = sys.argv[2]
dirDest = sys.argv[3]

# -----------------------------------------------------------------
def getFolderDest(path, cadID):
    folders = []
    for r, d, f in os.walk(path):
        for folder in d:
            if cadID in folder:
                folders.append(os.path.join(r, folder))
        break
    return folders
    
def getInfo(path):
    return {'owner': os.stat(path).st_uid, 'group': os.stat(path).st_gid}


def changeOwner(Dest, info):
    os.chown(Dest, info['owner'], info['group'])
    for root, dirs, files in os.walk(Dest):
        for d in dirs:
            os.chown(os.path.join(root,d), info['owner'], info['group'])
        for f in files:
            os.chown(os.path.join(root,f), info['owner'], info['group'])

# -----------------------------------------------------------------



fDest = getFolderDest(pathDest, cadID)
print(fDest)

for f in fDest:
    info = getInfo(f)
    Dest = os.path.join(f, dirDest)
    if os.path.exists(Dest):
        shutil.rmtree(Dest, ignore_errors=True)
    
    shutil.copytree(pathOrigin, Dest)
    changeOwner(Dest, info)

