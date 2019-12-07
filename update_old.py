#!/usr/bin/env python

import sys, os, shutil

# cadID = 'jupyter-'
"""
pathOrigin = "/home/miguel/Desktop/Desarrollo/kk/origen/"
# pathDest = "/home/miguel/Desktop/Desarrollo/kk/home"
pathDest = "/home"
#dirDest = os.path.split(pathOrigin)[1])
dirDest = 'copiaOrigen'
"""

"""
if len(sys.argv)-1 != 3:
    print('Sintaxis: {} DirectorioOrigen PathconCuentasJupyter(normalmente /home) DirectorioDestino'.format(sys.argv[0])) 
    sys.exit()

pathOrigin = sys.argv[1]
pathDest = sys.argv[2]
dirDest = sys.argv[3]
"""
Src = "/home/miguel/Desktop/Desarrollo/kk/origen/"
Dst = "/home"
cadID = 'jupyter-'

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
    
def list_files(startpath):

    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))


def getUsers(path):
    users = []
    owners = []
    groups = []
    for r, d, f in os.walk(path):
        for fol in d:
            if cadID in fol:
                uri = os.path.join(r, fol)
                users.append(uri)
                owners.append(os.stat(uri).st_uid)
                groups.append(os.stat(uri).st_gid)
        break

    return {'home': users, 'owners': owners, 'groups': groups}


def changeOwner(Dest, info):
    # os.chown(Dest, info['owner'], info['group'])
    for root, dirs, files in os.walk(Dest):
        for d in dirs:
            os.chown(os.path.join(root,d), info['owner'], info['group'])
        for f in files:
            os.chown(os.path.join(root,f), info['owner'], info['group'])

# -----------------------------------------------------------------

# list_files(Src)


SrcStruct = getSrc(Src)
#print(SrcStruct)
Users = getUsers(Dst)


dirs = SrcStruct['folders']
files = SrcStruct['files']

homes = Users['users']

"""
for h in homes:
    for d in dirs:
        d2 = d.replace(Src,'')
        d3 = h + '/' + d2
        #print(d)
        print(d3)  
        try:
            os.mkdir(d3)
        except OSError:
            pass

for h in homes:
    for f in files:
        d2 = f.replace(Src,'')
        d3 = h + '/' + d2
        #print(d)
        print(d3) 
        shutil.copyfile(f, d3)
 """
for key in Users:

    print(key, "::", Users[key])



"""
Users = getUsers(Dst)
print(Users)
"""


"""
fDest = getFolderDest(pathDest, cadID)
print(fDest)

for f in fDest:
    info = getInfo(f)
    Dest = os.path.join(f, dirDest)
    if os.path.exists(Dest):
        shutil.rmtree(Dest, ignore_errors=True)
    
    shutil.copytree(pathOrigin, Dest)
    changeOwner(Dest, info)

"""