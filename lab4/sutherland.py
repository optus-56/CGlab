from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

xmin,ymin=100,100
xmax,ymax=400,300

polygon=[
    (50,150),
    (200,350),
    (450,250),
    (350,50)
]


def inside(p,edge):

    x,y=p

    if edge=="LEFT":
        return x>=xmin

    if edge=="RIGHT":
        return x<=xmax

    if edge=="BOTTOM":
        return y>=ymin

    if edge=="TOP":
        return y<=ymax


def intersect(p1,p2,edge):

    x1,y1=p1
    x2,y2=p2

    if edge=="LEFT":
        x=xmin
        y=y1+(y2-y1)*(xmin-x1)/(x2-x1)

    elif edge=="RIGHT":
        x=xmax
        y=y1+(y2-y1)*(xmax-x1)/(x2-x1)

    elif edge=="BOTTOM":
        y=ymin
        x=x1+(x2-x1)*(ymin-y1)/(y2-y1)

    else:
        y=ymax
        x=x1+(x2-x1)*(ymax-y1)/(y2-y1)

    return (x,y)


def clip(poly,edge):

    output=[]

    prev=poly[-1]

    for curr in poly:

        if inside(curr,edge):

            if not inside(prev,edge):
                output.append(intersect(prev,curr,edge))

            output.append(curr)

        elif inside(prev,edge):
            output.append(intersect(prev,curr,edge))

        prev=curr

    return output


def sutherland():

    poly=polygon

    for edge in ["LEFT","RIGHT","BOTTOM","TOP"]:
        poly=clip(poly,edge)

    return poly


def drawPolygon(poly):

    glBegin(GL_LINE_LOOP)

    for p in poly:
        glVertex2f(p[0],p[1])

    glEnd()


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
    drawPolygon(polygon)

    clipped=sutherland()

    glColor3f(0,1,0)
    drawPolygon(clipped)

    glFlush()


def init():
    glClearColor(0,0,0,1)
    gluOrtho2D(0,500,0,400)


glutInit()
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutInitWindowSize(600,500)
glutCreateWindow(b"Sutherland Hodgman")
init()
glutDisplayFunc(display)
glutMainLoop()