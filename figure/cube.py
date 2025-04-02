from OpenGL.GL import *

# Vértices do cubo
vertices = [
    (0.5, -0.5, 0.5),   # 0
    (-0.5, -0.5, 0.5),  # 1
    (0.5, 0.5, 0.5),    # 2
    (-0.5, 0.5, 0.5),   # 3
    (0.5, 0.5, -0.5),   # 4
    (-0.5, 0.5, -0.5),  # 5
    (0.5, -0.5, -0.5),  # 6
    (-0.5, -0.5, -0.5)  # 7
]

# Faces do cubo (formadas por 4 vértices)
faces = [
    (0, 1, 3, 2),  # Frente
    (4, 5, 7, 6),  # Trás
    (2, 3, 5, 4),  # Topo
    (0, 1, 7, 6),  # Base
    (1, 3, 5, 7),  # Esquerda
    (0, 2, 4, 6)   # Direita
]

# Cores diferentes para cada face
colors = [
    (1, 0, 0),  # Vermelho (Frente)
    (0, 1, 0),  # Verde (Trás)
    (0, 0, 1),  # Azul (Topo)
    (1, 1, 0),  # Amarelo (Base)
    (0, 1, 1),  # Ciano (Esquerda)
    (1, 0, 1)   # Magenta (Direita)
]

# Função que desenha o cubo colorido
def wireCube():
    for i, face in enumerate(faces):
        glColor3fv(colors[i])
        glBegin(GL_QUADS)
        for vertex in face:
            glVertex3fv(vertices[vertex])
        glEnd()