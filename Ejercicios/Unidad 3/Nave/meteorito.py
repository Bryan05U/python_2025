import pygame as pg
import random
from configuración import ANCHO_PANTALLA, ALTO_PANTALLA, VELOCIDAD_METEORITO

class Meteorito(pg.sprite.Sprite):
    def __init__(self):
        self.image = pg.Surface((30, 30))
        pg.draw.circle(self.image, (255, 0, 0), (15, 15), 15)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, ANCHO_PANTALLA - self.rect.width) # Aparece al azar en la parte superior de la pantalla
        self.rect.y = -self.rect.height # Simular que el meteorito aparece fuera de la pantalla
    
    def update(self):
        self.rect.y += VELOCIDAD_METEORITO

        # Si el meteorito sale de la pantalla, se elimina
        if self.rect.top > ALTO_PANTALLA:
            self.kill()