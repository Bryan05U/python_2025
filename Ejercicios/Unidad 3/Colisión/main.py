import pygame as pg
from círculo_grande import CírculoGrande
from círculo_pequeño import CírculoPequeño

pg.init

ventana = pg.display.set_mode((800, 600))
pg.display.set_caption("Colisión de Círculos")

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
    ventana.fill(background)
    círculo_pequeño.dibujar(ventana)
    círculo_grande.dibujar(ventana)
    
    pg.display.update()

pg.quit