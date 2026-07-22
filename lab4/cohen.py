from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Clipping Window
xmin, ymin = 100, 100
xmax, ymax = 400, 300

# Line
x1, y1 = 50, 50
x2, y2 = 450, 350

INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8


def computeCode(x, y):
    code = INSIDE

    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT

    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP

    return code


def cohenSutherland():
    global x1, y1, x2, y2

    code1 = computeCode(x1, y1)
    code2 = computeCode(x2, y2)

    accept = False

    while True:

        if code1 == 0 and code2 == 0:
            accept = True
            break

        elif (code1 & code2) != 0:
            break

        else:

            if code1 != 0:
                codeOut = code1
            else:
                codeOut = code2

            if codeOut & TOP:
                x = x1 + (x2-x1)*(ymax-y1)/(y2-y1)
                y = ymax

            elif codeOut & BOTTOM:
                x = x1 + (x2-x1)*(ymin-y1)/(y2-y1)
                y = ymin

            elif codeOut & RIGHT:
                y = y1 + (y2-y1)*(xmax-x1)/(x2-x1)
                x = xmax

            elif codeOut & LEFT:
                y = y1 + (y2-y1)*(xmin-x1)/(x2-x1)
                x = xmin

            if codeOut == code1:
                x1, y1 = x, y
                code1 = computeCode(x1, y1)
            else:
                x2, y2 = x, y
                code2 = computeCode(x2, y2)

    return accept


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Window
    glColor3f(1,0,0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(xmin,ymin)
    glVertex2f(xmax,ymin)
    glVertex2f(xmax,ymax)
    glVertex2f(xmin,ymax)
    glEnd()

    # Original Line
    glColor3f(1,1,1)
    glBegin(GL_LINES)
    glVertex2f(50,50)
    glVertex2f(450,350)
    glEnd()

    if cohenSutherland():
        glColor3f(0,1,0)
        glBegin(GL_LINES)
        glVertex2f(x1,y1)
        glVertex2f(x2,y2)
        glEnd()

    glFlush()


def init():
    glClearColor(0,0,0,1)
    gluOrtho2D(0,500,0,400)


glutInit()
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutInitWindowSize(600,500)
glutCreateWindow(b"Cohen Sutherland")
init()
glutDisplayFunc(display)
glutMainLoop()