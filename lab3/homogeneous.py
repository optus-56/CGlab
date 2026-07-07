from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

rectangle = [
    [-50, -30, 1],
    [50, -30, 1],
    [50, 30, 1],
    [-50, 30, 1]
]

# Matrix × Column Vector
def multiply(matrix, point):
    return [
        matrix[0][0] * point[0] + matrix[0][1] * point[1] + matrix[0][2] * point[2],
        matrix[1][0] * point[0] + matrix[1][1] * point[1] + matrix[1][2] * point[2],
        matrix[2][0] * point[0] + matrix[2][1] * point[1] + matrix[2][2] * point[2]
    ]

angle = radians(45)

# Scaling Matrix
scale = [
    [2, 0, 0],
    [0, 2, 0],
    [0, 0, 1]
]

# Rotation Matrix (45°)
rotation = [
    [cos(angle), -sin(angle), 0],
    [sin(angle),  cos(angle), 0],
    [0, 0, 1]
]

# Reflection about X-axis
reflection = [
    [1, 0, 0],
    [0, -1, 0],
    [0, 0, 1]
]

# Translation Matrix
translation = [
    [1, 0, 100],
    [0, 1, 80],
    [0, 0, 1]
]

def draw(rect):
    glBegin(GL_LINE_LOOP)
    for p in rect:
        glVertex2f(p[0], p[1])
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1, 0, 0)
    draw(rectangle)

    transformed = []

    for p in rectangle:
        q = multiply(scale, p)
        q = multiply(rotation, q)
        q = multiply(reflection, q)
        q = multiply(translation, q)
        transformed.append(q)

    glColor3f(0, 1, 0)
    draw(transformed)

    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Composite Transformation")

glClearColor(0,0,0,0)
glColor3f(0, 0, 0)

gluOrtho2D(-300, 300, -300, 300)

glutDisplayFunc(display)
glutMainLoop()