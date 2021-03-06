#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os, commands

class InterfaceWTP:

"""
    @author: Kaio Cesar <tecnico.kaio@gmail.com>
    @todo Qual o intuito desse script.
"""

	headerStart = ["##################################",
		       "#_________WebToolsPy_____________#",
		       "#___ Creation tool environment___#",		      
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


	def createVHOST(self):
		os.system('clear')
		print("#_#-# Create VHOST #-#_#")
		
		RespSN = "n"
		while RespSN.lower() == "n":			
			ServerName = raw_input("Enter SERVER NAME: ")
			RespSN = raw_input("You're sure, Server Name is '"+ ServerName +"'? [y/n]: ")

		RespDR = "n"
		while RespDR.lower() == "n":			
			DocumentRoot = raw_input("Enter DOCUMENT ROOT: ")
			RespDR = raw_input("You're sure, Document Root is '"+ DocumentRoot.upper() +"' ? [y/n]")
	
		RespLang = "n"	
		Langs = ["PHP","PYTHON"]
		while RespLang <> "y":
			Language = raw_input("What's project programme language [0] PHP, [1]PYTHON: ")
			RespLang = raw_input("You're sure, Language is '"+ Langs[int(Language)] +"'' ? [y/n]")
		

	def defChoice(self):
		if (self.response=='1'):
			self.createVHOST()
		elif(self.response =='2'):
			print("Create a new project....")
		else:
			self.init()
			




WTP = WebToolsPy()
