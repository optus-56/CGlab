from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def plot(x, y):
    glVertex2i(x, y)
    glVertex2i(-x, y)
    glVertex2i(x, -y)
    glVertex2i(-x, -y)

def midpointEllipse(rx, ry):
    x = 0
    y = ry

    rx2 = rx * rx
    ry2 = ry * ry

    dx = 2 * ry2 * x
    dy = 2 * rx2 * y

    p1 = ry2 - rx2 * ry + 0.25 * rx2

    glBegin(GL_POINTS)

    while dx < dy:
        plot(x, y)

        if p1 < 0:
            x += 1
            dx = 2 * ry2 * x
            p1 += dx + ry2
        else:
            x += 1
            y -= 1
            dx = 2 * ry2 * x
            dy = 2 * rx2 * y
            p1 += dx - dy + ry2

    p2 = ry2 * (x + 0.5) ** 2 + rx2 * (y - 1) ** 2 - rx2 * ry2

    while y >= 0:
        plot(x, y)

        if p2 > 0:
            y -= 1
            dy = 2 * rx2 * y
            p2 += rx2 - dy
        else:
            x += 1
            y -= 1
            dx = 2 * ry2 * x
            dy = 2 * rx2 * y
            p2 += dx - dy + rx2

    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,1,1)
    midpointEllipse(100,50)
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500,500)
glutCreateWindow(b"Midpoint Ellipse")
gluOrtho2D(-250,250,-250,250)
glutDisplayFunc(display)
glutMainLoop()