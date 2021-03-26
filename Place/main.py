import pygame
from pygame import display, event, key
from pygame.constants import K_KP1, K_KP2
from colors import Colors

pygame.init()
display.set_caption("Place")
running = True
screen = display.set_mode((900,900))
c_souris = False
color = 1
cells = []
size_grille = (30,30)
size_cell = (30,30)


def init_grille(size_grille):
    for x in range(size_grille[0]):
        rows = []
        for y in range(size_grille[1]):                
            rows.append(0)
        cells.append(rows)




while running :
    for e in event.get():
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.MOUSEBUTTONDOWN:
            
            if not c_souris:
                c_souris = True
                pos = pygame.mouse.get_pos()

                for x in range(size_grille[0]):
                    for y in range(size_grille[1]):
                           draw.rect(self.screen, Color(cells(x,y)),((x*size_cell[0],y*size_cell[1]),(size_cell[0],size_cell[1])))
                



                #fonction remplir couleur sur la case
        else :
            c_souris = False

    if key.get_pressed()[K_KP1]:
        color = 0
  
    if key.get_pressed()[K_KP2]:
        color = 1


    screen.fill((255,255,255))






