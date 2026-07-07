from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

rect = [
    [100,100,1],
    [300,100,1],
    [300,200,1],
    [100,200,1]
]

R = [
    [0,-1,0],
    [1,0,0],
    [0,0,1]
]

def transform(p):
    x,y,_ = p
    return (
        R[0][0]*x + R[0][1]*y,
        R[1][0]*x + R[1][1]*y
    )

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1,0,0)
    glBegin(GL_LINE_LOOP)
    for p in rect:
        glVertex2f(p[0],p[1])
    glEnd()

    glColor3f(0,1,0)
    glBegin(GL_LINE_LOOP)
    for p in rect:
        x,y = transform(p)
        glVertex2f(x+250,y+250)
    glEnd()

    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutInitWindowSize(800,800)
glutCreateWindow(b"Rotation")
gluOrtho2D(0,800,0,800)
glutDisplayFunc(display)
glutMainLoop()