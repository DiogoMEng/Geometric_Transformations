import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from figure.cube import wireCube

# Inicialização do Pygame e OpenGL
pygame.init()

screen_width = 1000
screen_height = 800

background_color = (0, 0, 0, 1)
drawing_color = (1, 1, 1, 1)

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Transformações Geométricas - OpenGL')

# Variáveis de transformação
angle = 0
tx, ty, tz = 0.0, 0.0, -5.0
scale = 1.0
mirrorX = 1
mirrorY = 1
mirrorZ = 1

def initialise():
    glClearColor(*background_color)
    glColor4f(*drawing_color)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glEnable(GL_DEPTH_TEST)
    glViewport(0, 0, screen.get_width(), screen.get_height())

def display():
    global angle, scale, mirrorX, mirrorY, mirrorZ

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()

    # 1. Translação (posiciona o objeto no espaço)
    glTranslatef(tx, ty, tz)

    # 2. Escala (inclui espelhamento se valores forem negativos)
    glScalef(scale * mirrorX, scale * mirrorY, scale * mirrorZ)

    # 3. Rotação (aplicada por último)
    glRotatef(angle, 1, 1, 0)

    # Desenhar o cubo
    glPushMatrix()
    wireCube()
    glPopMatrix()

    angle += 1
    pygame.display.flip()

def main():
    global tx, ty, tz, scale, mirrorX

    initialise()
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_LEFT:
                    tx -= 0.1
                elif event.key == K_RIGHT:
                    tx += 0.1
                elif event.key == K_UP:
                    ty += 0.1
                elif event.key == K_DOWN:
                    ty -= 0.1
                elif event.key == K_PAGEUP:
                    tz += 0.1
                elif event.key == K_PAGEDOWN:
                    tz -= 0.1
                elif event.key == K_PLUS or event.key == K_EQUALS:
                    scale += 0.1
                elif event.key == K_MINUS:
                    scale -= 0.1
                elif event.key == K_m:
                    mirrorX *= -1

        display()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()