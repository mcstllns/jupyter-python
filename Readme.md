Estos scripts en python se utilizan para gestionar cuentas en jupyterHub

___

Todos utilizan un fichero de configuracion definido en __config.py__ que tiene las siguientes variables:

>admins = ['miguel'
home = '/home'
usersFile = 'usersList.txt'
updateSrc = '/home/miguel/updates'
updateDst = 'update'

y el fichero con la lista de usuarios (usersList.txt) tiene este aspecto:
> user01
user02
etc...

---
- addusers.py: Crea las directorios definidos en el ficheros usersList.txt
- deleteusers.py: Borra las cuentas (y los directorios) de los usuarios en usersList.txt
- update.py: Copia o actualiza la carpeta config.updateSrc en la carpeta config.updateDst de todos los usuarios definidos en usersList.txt
- checkip.py: Comprueba periódicamente si una ip (publica, o dada) esta respondiendo y el log lo guarda en un fichero de texto.

---

