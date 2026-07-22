from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

xmin, ymin = 100,100
xmax, ymax = 400,300

x1,y1 = 50,50
x2,y2 = 450,350


def liangBarsky():

    dx = x2-x1
    dy = y2-y1

    p = [-dx, dx, -dy, dy]
    q = [x1-xmin, xmax-x1, y1-ymin, ymax-y1]

    u1 = 0
    u2 = 1

    for i in range(4):

        if p[i] == 0:

            if q[i] < 0:
                return None

        else:

            t = q[i]/p[i]

            if p[i] < 0:
                u1 = max(u1,t)
            else:
                u2 = min(u2,t)

    if u1 > u2:
        return None

    nx1 = x1 + u1*dx
    ny1 = y1 + u1*dy

    nx2 = x1 + u2*dx
    ny2 = y1 + u2*dy

    return nx1,ny1,nx2,ny2


def display():

    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1,0,0)

    glBegin(GL_LINE_LOOP)
    glVertex2f(xmin,ymin)
    glVertex2f(xmax,ymin)
    glVertex2f(xmax,ymax)
    glVertex2f(xmin,ymax)
    glEnd()

    glColor3f(1,1,1)

    glBegin(GL_LINES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glEnd()

    line = liangBarsky()

    if line:

        glColor3f(0,1,0)

        glBegin(GL_LINES)
        glVertex2f(line[0],line[1])
        glVertex2f(line[2],line[3])
        glEnd()

    glFlush()


def init():
    glClearColor(0,0,0,1)
    gluOrtho2D(0,500,0,400)


glutInit()
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutInitWindowSize(600,500)
glutCreateWindow(b"Liang Barsky")
init()
glutDisplayFunc(display)
glutMainLoop()