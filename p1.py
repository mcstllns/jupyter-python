#!/usr/bin/env python3


import os
import config


with open(config.usersFile) as f:
    content = f.readlines()
f.close()

content = [x.strip() for x in content] 
print("")
print("------------------------------")
print("Se van a crear los siguientes usuarios :", content)
print(" ")
print("Desea crearlos? [y/n]: ")
ans = input()

if (ans == "y"):
    print("ha dicho yes")


"""
os.system("cp -r ../kk/kk1 ../kk/kk2")
os.system("cp -r ../kk/kk1 ../kk/kk2")
os.system("chown -R miguel:miguel ../kk/kk2")
"""
#os.system("ls")
