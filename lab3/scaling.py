from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


rect = [
    [100,100,1],
    [200,100,1],
    [200,200,1],
    [100,200,1]
]

S = [
    [2,0,0],
    [0,2,0],
    [0,0,1]
]

def transform(p):
    x,y,_ = p
    return (
        S[0][0]*x,
        S[1][1]*y
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
        glVertex2f(x,y)
    glEnd()

    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"Scaling")
gluOrtho2D(0,600,0,600)
glutDisplayFunc(display)
glutMainLoop()