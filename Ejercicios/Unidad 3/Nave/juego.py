import pygame as pg
import random
from configuración import ANCHO_PANTALLA, ALTO_PANTALLA, NEGRO, FRECUENCIA_METEORITO
from jugador import Jugador
from meteorito import Meteorito

class Juego:
    def __init__(self):
        pg.init()
        self.pantalla = pg.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
        pg.display.set_caption("Nave Espacial vs Meteoritos")
        self.clock = pg.time.Clock()

        self.all_sprites = pg.sprite.Group()
        self.meteoritos = pg.sprite.Group()
    
        self.jugador = Jugador()
        self.all_sprites.add(self.jugador)

    def run(self):
        running = True
        while running:
            self.clock.tick(60)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                
                # Generar meteoritos al azar
                if random.randint(1, FRECUENCIA_METEORITO) == 1:
                    meteorito = Meteorito()
                    self.all_sprites.add(meteorito)
                    self.meteoritos.add(meteorito)
                
                # Actualizar todas las posiciones de los sprites
                self.all_sprites.update()

                # Lógica para corroborar las colisiones
                if pg.sprite.spritecollide(self.jugador, self.meteoritos, False):
                    print("GAME OVER")
                    running = False
                
                # Dibujar los sprites
                self.pantalla.fill(NEGRO)
                self.all_sprites.draw(self.pantalla)
                pg.display.flip()

        pg.quit()