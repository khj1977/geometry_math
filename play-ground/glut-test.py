# The basics of glut for python is mainly from: https://zenn.dev/zgw426/articles/2619722626bf23

import sys
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

import math as m

def idle():
    glutPostRedisplay()

def mouse(button, state, x, y):
  if button == GLUT_LEFT_BUTTON:
    if (state == GLUT_DOWN):
      glutIdleFunc(idle)
    else:
      glutIdleFunc(0)
  elif button == GLUT_RIGHT_BUTTON:
    if state == GLUT_DOWN:
        glutPostRedisplay()

def displayOld():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex3f(0.25, 0.25, 0.0)
    glVertex3f(0.75, 0.25, 0.0)
    glVertex3f(0.75, 0.75, 0.0)
    glEnd()
    glFlush()

def display():
    # static theta = 0.0
    # static deltaTheta = 0.01
    # static xx = 0.0
    # static yy = 0.0
    global theta
    global deltaTheta
    global xx
    global yy

    theta = theta + deltaTheta
    if (theta > 2.0 * 3.14):
        theta = 0.0

    xx = m.cos(theta)
    yy = m.sin(theta)

    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POINTS)

    glVertex2d(xx, yy)

    glEnd()
    glFlush()

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1.0, 0.0, 1.0, -1.0, 1.0)


theta = 0.0
deltaTheta = 0.01
xx = 0.0
yy = 0.0
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(300, 300)
glutInitWindowPosition(200, 200)
glutCreateWindow(b"hello")
glutMouseFunc(mouse)
init()
glutDisplayFunc(display)
glutMainLoop()