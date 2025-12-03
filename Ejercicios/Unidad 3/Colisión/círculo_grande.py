import pygame as pg

class CírculoGrande:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radio = 50
        self.color = (0, 0, 255)
        self.velocidad = 1
    
    def dibujar(self, ventana):
        pg.draw.circle(ventana, self.color)
    
    def mover(self, teclas):
        mov_x = 0
        mov_y = 0

        if teclas[pg.K_a]:
            mov_x = -1
        if teclas[pg.K_d]:
            mov_x = 1
        if teclas[pg.K_w]:
            mov_y = -1
        if teclas[pg.K_s]:
            mov_y = 1
        
        self.rect.x += mov_x * self.velocidad
        self.rect.y += mov_y * self.velocidad