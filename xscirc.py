splash="""
░█░█░█▀▀░█▀▀░▀█▀░█▀▄░█▀▀
░▄▀▄░▀▀█░█░░░░█░░█▀▄░█░░
░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀
"""
print(splash)
from time import sleep
import sys
print("Importing sys...")
import os
print("Importing pygame...")
import pygame
print("Importing tkinter...")
from tkinter import messagebox as mb
print("Importing threading...")
import threading
print("Importing SugarCaneParse IRC...")
import scparseirc
print("Initializing PyGame...")
pygame.init()
if not pygame.get_init():
  mb.showerror("Error", "Couldn't load all pygame modules!")
  raise SystemError("Aborted...")
print("Now starting display...")
display = pygame.display.set_mode((800,600), pygame.RESIZABLE)
pygame.display.set_caption('XScIRC')
white = (255, 255, 255)
font_debug = pygame.font.SysFont('monospace', 14)
splash2 = []
splashRect = []
def get_splashtext():
  y = 0
  for i in splash.split("\n"):
    j = font_debug.render(i, True, white)
    splash2.append(j)
    h = j.get_rect()
    splashRect.append(h.move(0, y))
    y += 14
icon = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/assets/icon.png')
pygame.display.set_icon(icon)
run=True
loading=True
def ircloop():
   print("IRC loop placeholder")
print("Starting IRC thread...")
ircthread = threading.Thread(target=ircloop)
ircthread.start()
print("Reached mainloop!")
while run:  
    if loading:
      display.fill((0, 0, 0))
      get_splashtext()
      for i, j in zip(splash2, splashRect):
        display.blit(i, j)
      #text = font_debug.render(i, True, white)

    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
           print("Recieved quit trigger from OS.")
           run=False
        pygame.display.update()

pygame.display.quit()
print("Exited successfully")