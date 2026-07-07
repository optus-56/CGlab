from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

rectangle=[
[-50,-30,1],
[50,-30,1],
[50,30,1],
[-50,30,1]
]

def multiply(p,m):
    return [
        p[0]*m[0][0]+p[1]*m[1][0]+p[2]*m[2][0],
        p[0]*m[0][1]+p[1]*m[1][1]+p[2]*m[2][1],
        p[0]*m[0][2]+p[1]*m[1][2]+p[2]*m[2][2]
    ]

angle=radians(45)

scale=[
[2,0,0],
[0,2,0],
[0,0,1]
]

rotation=[
[cos(angle),sin(angle),0],
[-sin(angle),cos(angle),0],
[0,0,1]
]

reflection=[
[1,0,0],
[0,-1,0],
[0,0,1]
]

translation=[
[1,0,0],
[0,1,0],
[100,80,1]
]

def draw(rect):
    glBegin(GL_LINE_LOOP)
    for p in rect:
        glVertex2f(p[0],p[1])
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1,0,0)
    draw(rectangle)

    transformed=[]

    for p in rectangle:
        q=multiply(p,scale)
        q=multiply(q,rotation)
        q=multiply(q,reflection)
        q=multiply(q,translation)
        transformed.append(q)

    glColor3f(0,1,0)
    draw(transformed)

    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutInitWindowSize(500,500)
glutCreateWindow(b"Composite Transformation")
gluOrtho2D(-300,300,-300,300)
glutDisplayFunc(display)
glutMainLoop()