import pygame
from pygame import display, event, key, draw
from pygame.constants import K_KP0, K_KP1, K_KP2, K_KP3, K_KP4, K_KP5, K_KP6, K_KP7, K_KP8, K_KP9
import math


pygame.init()
display.set_caption("Place")
running = True
screen = display.set_mode((900,900))
c_souris = False
color = 1
cells = []
size_grille = (30,30)
size_cell = (30,30)

COLORS = [
 (255, 255, 255), # White
 (0, 0, 0), # Black
 (255, 0, 0), # Red
 (51, 204, 51), # Green
 (0, 153, 255), # Blue
 (255, 51, 204), # Pink
 (255, 153, 0), # Orange
 (255, 255, 0), # Yellow
 (153, 0, 204), # Purple
 (128, 128, 128), # Gray
]

def init_grille(size_grille):
    for x in range(size_grille[0]):
        rows = []
        for y in range(size_grille[1]):                
            rows.append(0)
        cells.append(rows)

screen.fill((255,255,255))
display.update()
init_grille(size_grille)
while running :
    for e in event.get():
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.MOUSEBUTTONDOWN:
            
            if not c_souris:
                c_souris = True
                pos = pygame.mouse.get_pos()

                x_temp = pos[0] / 30
                y_temp = pos[1] / 30

                x_pos  = math.trunc(x_temp)
                y_pos  = math.trunc(y_temp)

                cells[x_pos][y_pos] = color

                for x in range(size_grille[0]):
                    for y in range(size_grille[1]):
                        draw.rect(screen, COLORS[cells[x][y]],((x*size_cell[0],y*size_cell[1]),(size_cell[0],size_cell[1])))



            display.update()









                #fonction remplir couleur sur la case
        else :
            c_souris = False

    if key.get_pressed()[K_KP0]:
        color = 0

    if key.get_pressed()[K_KP1]:
        color = 1
  
    if key.get_pressed()[K_KP2]:
        color = 2

    if key.get_pressed()[K_KP3]:
        color = 3
    
    if key.get_pressed()[K_KP4]:
        color = 4
    
    if key.get_pressed()[K_KP5]:
        color = 5
    
    if key.get_pressed()[K_KP6]:
        color = 6
    
    if key.get_pressed()[K_KP7]:
        color = 7
    
    if key.get_pressed()[K_KP8]:
        color = 8
    
    if key.get_pressed()[K_KP9]:
        color = 9







