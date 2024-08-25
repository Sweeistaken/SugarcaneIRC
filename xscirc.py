splash="""

  ____                                                                   ___   ____     ____ 
 / ___|   _   _    __ _    __ _   _ __    ___    __ _   _ __     ___    |_ _| |  _ \\   / ___|
 \\___ \\  | | | |  / _` |  / _` | | '__|  / __|  / _` | | '_ \\   / _ \\    | |  | |_) | | |    
  ___) | | |_| | | (_| | | (_| | | |    | (__  | (_| | | | | | |  __/    | |  |  _ <  | |___ 
 |____/   \\__,_|  \\__, |  \\__,_| |_|     \\___|  \\__,_| |_| |_|  \\___|   |___| |_| \\_\\  \\____|
                  |___/                                                                      

"""
print(splash)
from time import sleep
import sys
import os
import pygame
from tkinter import messagebox as mb
import threading
pygame.init()
if not pygame.get_init():
  mb.showerror("Error", "Couldn't load all pygame modules!")
  raise SystemError("Aborted...")
pygame.display.set_mode((640,480), pygame.RESIZABLE)
pygame.display.set_caption('SugarCaneIRC GUI')
icon = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/assets/icon.png')
pygame.display.set_icon(icon)
run=True
while run:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
           run=False

pygame.display.quit()
print("Exited successfully")