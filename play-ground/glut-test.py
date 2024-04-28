# From: https://zenn.dev/zgw426/articles/2619722626bf23

import sys
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex3f(0.25, 0.25, 0.0)
    glVertex3f(0.75, 0.25, 0.0)
    glVertex3f(0.75, 0.75, 0.0)
    glEnd()
    glFlush()


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1.0, 0.0, 1.0, -1.0, 1.0)


glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(300, 300)
glutInitWindowPosition(200, 200)
glutCreateWindow(b"hello")
init()
glutDisplayFunc(display)
glutMainLoop()