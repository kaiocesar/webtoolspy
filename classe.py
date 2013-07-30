#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os, commands

class InterfaceWTP:

	headerStart = ["##################################",
		       "#_________WebToolsPy_____________#",
		       "#___Creation tool environment___#",		      
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
		return response
		
			
	


class WebToolsPy(InterfaceWTP):

	response='0'

	def __init__(self):
		self.init()

	def init(self):		
		self.response = self.startInterface()
		self.defChoice()		


	def CreateVHOST(self):
		print("Create a VHOST......")


	def defChoice(self):
		if (self.response=='1'):
			print("Create VHOST.....")
		elif(self.response =='2'):
			print("Create a new project....")
		else:
			self.init()
			




WTP = WebToolsPy()
# WTP.startInterface()	

#WTP.readVHost("tete")		

#IWTP = InterfaceWTP()

#IWTP.startInterface()

"""
1 - menu escolher
2 - 

"""
