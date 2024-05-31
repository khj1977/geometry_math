from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

from com_gmail_eulerbonjour.digital_signal import fft_and_audio as mic

def my_glut_idle():
    glutPostRedisplay()

def my_glut_mouse(button, state, x, y):
  if button == GLUT_LEFT_BUTTON:
    if (state == GLUT_DOWN):
      glutIdleFunc(my_glut_idle)
    # else:
      # glutIdleFunc(0)
  elif button == GLUT_RIGHT_BUTTON:
    if state == GLUT_DOWN:
        glutPostRedisplay()

def my_glut_init(minX, maxX, minY, maxY, minZ, maxZ):
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    
    glLoadIdentity()
    # glOrtho(0.0, 1.0, 0.0, 1.0, -1.0, 1.0)
    # glOrtho(-20.0, 20.0, -20.0, 20.0, -10.0, 10.0)
    glOrtho(minX, maxX, minY, maxY, minZ, maxZ)

    # gluPerspective(30.0, 1.0, 1.0, 100.0)
    # glTranslated(0.0, 0.0, -5.0);
    # gluLookAt(0.0, 0.0, -10.0, 0.0, 0.0, 10.0, 0.0, 1.0, 0.0)

def my_glut_display():
    global audioMod

    audioMod.readDataAndDoFFT()

audioMod = mic.MicAndFFT()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutInitWindowPosition(200, 200)
glutCreateWindow(b"FFT")
glutMouseFunc(my_glut_mouse)
my_glut_init(-5.0, 5.0, -5.0, 5.0, -5.0, 5.0)
glutDisplayFunc(my_glut_display)
glutMainLoop()

