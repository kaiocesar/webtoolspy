#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os, commands

class InterfaceWTP:

	headerStart = ["##################################",
		       "#_________WebToolsPy_____________#",
		       "#_Ferramentas de ambientação web_#",
		       "##################################"]

	menuStart = ["1) Create VHost",
		     "2) Create project",
		     "3) List VHost"]

	def readList(self,list_=""):		
		for line in list_:
			print(line)		

	def makeStart(self):
		os.system('clear')
		self.readList(self.headerStart)
		self.readList(self.menuStart)

	def startInterface(self):
		self.makeStart()
		response = raw_input("Enter your choice ? ")
			
	


class WebToolsPy(InterfaceWTP):

	def readVHost(self,path=""):
		print(path)



WTP = WebToolsPy()
WTP.startInterface()	

#WTP.readVHost("tete")		

#IWTP = InterfaceWTP()

#IWTP.startInterface()

"""
1 - menu escolher
2 - 

"""
