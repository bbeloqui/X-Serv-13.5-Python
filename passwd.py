#!/usr/bin/python
fich=open("/etc/passwd","r")
frases=fich.readlines()
dicc = {}
for linea in frases :
	conf = linea.split(":")
	username = conf[0]
	shell = conf[-1] [:-1]
	dicc[username] = shell

print dicc["root"]	
print len(dicc) #No haria falta ,nose pide

try:
	print dicc["imaginario"]
except KeyError:
	print"El usuario imaginario no existe"
fich.close()
