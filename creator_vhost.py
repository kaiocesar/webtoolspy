#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import os
import commands

def lerVhost(file_=""):

	file_open = open(file_,'r')
	texts = file_open.read()

	vhosts = texts.split('##')

	"""
	  Leitura do arquivo, e obteção dos Vhosts
	"""

	new_vhost = []
	for vhost in vhosts :
		new_vhost.append(vhost.strip())
		new_vhost.append("##")

	file_open.close()

	"""
	  Obter os dados para o novo Vhost
	"""

	ServernameVhost = raw_input("Enter SERVER NAME VHost: ")

	DocrootVhost = raw_input("Enter DOCUMENT ROOT VHost: ")


	TypeProject = raw_input("Type project PHP[1] or Python[2]: ")

	if TypeProject == '2':
		WSGI = raw_input("Enter your Mod_WSGI location")
	else:
		WSGI = ""


	nodeVhost = "\n## \n\n"
	nodeVhost += "<VirtualHost *:80> \n"
	nodeVhost += "    ServerName " + ServernameVhost + '\n'
	if WSGI != "":
		nodeVhost+= "    WSGIScriptAlias / " + WSGI + "\n"
	nodeVhost += "    DocumentRoot " + DocrootVhost + '\n'
	nodeVhost += "</VirtualHost>\n"


	new_vhost.append(nodeVhost)

	arquivo = open(file_,'r')
	texto = arquivo.readlines()
	texto.append(nodeVhost)

	arquivo = open(file_,'w')
	arquivo.writelines(texto)

	arquivo.close()


	print('done..')





lerVhost('texto.txt')

# lerVhost("/opt/lampp/etc/extra/httpd-vhosts.conf")
