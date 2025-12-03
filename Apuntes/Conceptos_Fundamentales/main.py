import pygame as pg

# Se inicializa Pygame
pg.init()

# Creación de ventana de 800x600 píxeles
window = pg.display.set_mode((800,600))
# Título de pantalla de juego
pg.display.set_caption("Pygame")

# Color de fondo (variable)
background = (0,0,0) # Negro

# Limitador de FPS
clock = pg.time.Clock()
FPS = 30

running = True
while running:
    dt = clock.tick(FPS) / 1000.0 # Segundos desde el frame anterior

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    # Actualizar estados (usar dt para movimiento)
    # pos += velocidad * dt

    # Dibujar
    window.fill(background)

    # Dibujar figuras
    pg.draw.circle(window, (104, 235, 237), (400, 300), 70) # Círculo
    pg.draw.rect(window, (74, 65, 42), (350, 275, 100, 50)) # Rectángulo
    pg.draw.ellipse(window, (0, 140, 140), (350, 275, 100, 50)) # Elipse
    pg.draw.line(window, (0, 255, 35), (100, 100), (700, 100), 10) # Línea

    # Vértices
    v = [(400, 110), (350, 200), (450, 200)]
    
    pg.draw.polygon(window, (191, 255, 1), v)

    pg.display.update()

pg.quit