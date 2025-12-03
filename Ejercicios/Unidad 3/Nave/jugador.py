import pygame as pg
from configuración import ANCHO_PANTALLA, ALTO_PANTALLA, VELOCIDAD_JUGADOR

class Jugador(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Atributos de la nave
        self.image = pg.Surface((50, 50), pg.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.centerx = ANCHO_PANTALLA // 2 # Aparecerá al medio de la pantalla
        self.rect.bottom = ALTO_PANTALLA - 10

        # Dibujar el triángulo
        pg.draw.polygon(self.image, (0, 0, 255), [(25, 0),(0, 50),(50, 50)])
    
    def update(self):
        keys = pg.key.get_pressed()
        
        # Teclas ocupadas
        if keys[pg.K_a]:
            self.rect.x -= VELOCIDAD_JUGADOR
        if keys[pg.K_d]:
            self.rect.x += VELOCIDAD_JUGADOR
        
        # Mantener la nave dentro de los límites de la pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > ANCHO_PANTALLA:
            self.rect.right = ANCHO_PANTALLA