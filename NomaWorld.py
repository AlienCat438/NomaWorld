#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *		

pygame.init()
start = False
continuer = True
fenetre = pygame.display.set_mode((650, 495),RESIZABLE)
Curseur = pygame.image.load("Texture/Curseur/Curseur.png").convert_alpha()
Fond = pygame.image.load("Texture/Fond/EcranTitre.png").convert()
pygame.key.set_repeat(400, 50)

class Button(pygame.sprite.Sprite):
	
	def __init__(self,image,x,y):
		""" Classe utilisée pour les boutons
		"""
		
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image)
		self.w = self.image.get_rect()[2]
		self.h = self.image.get_rect()[3]
		self.rect = Rect(x,y,self.w,self.h)
		self.mask = pygame.mask.from_surface(self.image)

class Block(pygame.sprite.Sprite):
	
	def __init__(self,image,x,y):
		""" Classe utilisée pour les boutons
		"""
		
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image)
		self.w = self.image.get_rect()[2]
		self.h = self.image.get_rect()[3]
		self.rect = Rect(x,y,self.w,self.h)
		self.mask = pygame.mask.from_surface(self.image)
def creer_blocks(image,positions):
	herbes = []
	for pos in positions:
		herbes.append(Block(image, pos[0], pos[1]))
	return herbes
herbes = creer_blocks("Texture/Block/Herbe.png",[(0,195),(50,195),(100,195),(150,195),(200,195),(250,195),(300,195),(350,195),(400,195),(450,195),(500,195),(550,195),(600,195)])
terres = creer_blocks("Texture/Block/Terre.png",[(0,245),(50,245),(100,245),(150,245),(200,245),(250,245),(300,245),(350,245),(400,245),(450,245),(500,245),(550,245),(600,245)])
pierres = creer_blocks("Texture/Block/Pierre.png",[(0,295),(100,295),(150,295),(200,295),(250,295),(300,295),(400,295),(450,295),(500,295),(550,295),(600,295),(150,345),(200,345),(250,345),(300,345),(450,345),(500,345),(550,345),(600,345),(0,395),(50,395),(100,395),(150,395),(200,395),(250,395),(300,395),(350,395),(400,395),(450,395),(500,395),(550,395),(600,395),(0,445),(50,445),(100,445),(150,445),(200,445),(250,445),(300,445),(350,445),(400,445),(450,445),(500,445),(550,445),(600,445)])
coals = creer_blocks("Texture/Block/Coal.png",[(50,295),(0,345),(50,345),(100,345)])
arbres = creer_blocks("Texture/Block/Arbre.png",[(100,-5)])
irons = creer_blocks("Texture/Block/Iron.png",[(350,295),(350,345),(400,345)])
blocks = herbes + terres + pierres + coals + arbres + irons
# bouton du menu de démarage (play)
buttonPlay = Button("Texture/Fond/boutonplay.png", 250, 200)
class Perso(pygame.sprite.Sprite):

	def __init__(self,image,x,y):
		""" Classe utilisée pour les boutons
		"""
		pygame.sprite.Sprite.__init__(self)
		self.counter = 0
		
		self.gauche = ["Texture/Perso/Avancer/VersGauche/PiedGauche/Sprite1.png", "Texture/Perso/Avancer/VersGauche/PiedGauche/Sprite2.png", "Texture/Perso/Avancer/VersGauche/PiedGauche/Sprite3.png"]
		self.droite = ["Texture/Perso/Perso_Droite-G.png", "Texture/Perso/Perso_Droite-D.png"]
				
		self.set_image("droite")
		self.w = self.image.get_rect()[2]
		self.h = self.image.get_rect()[3]
		self.rect = Rect(x,y,self.w,self.h)
		self.mask = pygame.mask.from_surface(self.image)
		
		
	def move(self,x,y, direction="droite"):
		self.rect = self.rect.move(x,y)
		self.set_image(direction)
		
	def set_image(self, direction):
		if direction == "gauche":
			images = self.gauche
		else:
			images = self.droite
			
		self.image = pygame.image.load(images[self.counter])
		self.counter = not self.counter
			
perso = Perso("Texture/Perso/Perso_Droite-S.png", 100, 115)
		
while continuer:
	
	
	###############################
	### 		EVENEMENTS 		###
	###############################
	
	
	for event in pygame.event.get():
		
		if event.type == pygame.MOUSEBUTTONUP:
			
			# gestion du menu de démarage
			if not start :
				pos = pygame.mouse.get_pos()
				# collision souris / boutton play
				if buttonPlay.rect.collidepoint(pos):
					start = True
					Fond = pygame.image.load("Texture/Fond/FondCiel.png").convert()
					
		elif event.type == KEYDOWN and event.key == K_d:
			perso.move(5,0,"droite")

		elif event.type == KEYDOWN and event.key == K_q:
			perso.move(-5,0,"gauche")
		
		elif event.type == KEYDOWN and event.key == K_ESCAPE:
			exit()

			
	###############################
	### 		AFFICHAGE 		###
	###############################
	
	# fondqd
	fenetre.blit(Fond, (0,0))
		
		
	# afficher bouton tant que jeu pas démarré
	if not start: 
		fenetre.blit(buttonPlay.image, buttonPlay.rect)
	else:
		fenetre.blit(perso.image, (perso.rect[0], perso.rect[1]))
		for b in blocks:
			fenetre.blit(b.image,b.rect)
	pygame.display.flip()
