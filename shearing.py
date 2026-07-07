from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

rect = [[-50,-50],[50,-50],[50,50],[-50,50]]

shx=1

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1,0,0)
    glBegin(GL_LINE_LOOP)
    for x,y in rect:
        glVertex2f(x,y)
    glEnd()

    glColor3f(0,1,0)
    glBegin(GL_LINE_LOOP)
    for x,y in rect:
        glVertex2f(x+shx*y,y)
    glEnd()

    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutInitWindowSize(500,500)
glutCreateWindow(b"Shearing")
gluOrtho2D(-250,250,-250,250)
glutDisplayFunc(display)
glutMainLoop()