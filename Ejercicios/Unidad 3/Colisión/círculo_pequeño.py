import pygame as pg

class CírculoPequeño:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radio = 25
        self.color = (0, 255, 255)
        self.velocidad = 1

    def dibujar(self, ventana):
        pg.draw.circle(ventana, self.color)
    
    def mover(self, teclas):
        mov_x = 0
        mov_y = 0
        
        if teclas[pg.K_LEFT]:
            mov_x = -1
        if teclas[pg.K_RIGHT]:
            mov_x = 1
        if teclas[pg.K_UP]:
            mov_y = 1
        if teclas[pg.K_DOWN]:
            mov_y = -1

        self.rect.x += mov_x * self.velocidad
        self.rect.y += mov_y * self.velocidad