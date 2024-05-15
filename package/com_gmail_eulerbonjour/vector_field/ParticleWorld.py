from com_gmail_eulerbonjour.ode_solver import ode_euler as euler
from com_gmail_eulerbonjour.ode_solver import ode_env as e
from com_gmail_eulerbonjour.ode_solver import ode_programmable_input as pi
from com_gmail_eulerbonjour.ode_solver import ode_control_input as ci
from com_gmail_eulerbonjour.ode_solver import ode_coefs as ce
from com_gmail_eulerbonjour.ode_solver import ode_time as time
from com_gmail_eulerbonjour.vector_field import SimpleParticleManager as manager
from com_gmail_eulerbonjour.vector_field import SimpleParticle as particle
from com_gmail_eulerbonjour.ode_solver import ode_disturbance as d

from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

def my_glut_idle():
    glutPostRedisplay()

def my_glut_mouse(button, state, x, y):
  if button == GLUT_LEFT_BUTTON:
    if (state == GLUT_DOWN):
      glutIdleFunc(my_glut_idle)
    else:
      glutIdleFunc(0)
  elif button == GLUT_RIGHT_BUTTON:
    if state == GLUT_DOWN:
        glutPostRedisplay()

def my_glut_init():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    
    glLoadIdentity()
    # glOrtho(0.0, 1.0, 0.0, 1.0, -1.0, 1.0)
    glOrtho(-10.0, 10.0, -10.0, 10.0, -10.0, 10.0)

    # gluPerspective(30.0, 1.0, 1.0, 100.0)
    # glTranslated(0.0, 0.0, -5.0);
    # gluLookAt(0.0, 0.0, -10.0, 0.0, 0.0, 10.0, 0.0, 1.0, 0.0)

def my_glut_display():
    # dirty hack
    global world

    world.inc()
    world.render()

class ParticleWorld:

    def __init__(self):
        self.startT = 0.0
        self.endT = 10000.0
        self.deltaT = 0.01
        self.envT = time.ODETime(self.startT, self.endT, self.deltaT)

        self.manager = manager.SimpleParticleManager(self.envT)
        self.initialize()

    def initialize(self):   
        for i in range(11):
            # f = lambda t, x, xDot: -0.2 * x - 0.1 * xDot
            f = lambda t, x, xDot: -0.2 * x
            disturbanceF = lambda t, x, xDot: 0.0

            startX = i
            startXDot = 0.1
            env = e.ODEEnv().setX(startX).setXDot(startXDot)

            forceControlInput = pi.ProgrammableInput()

            nullControlInput = ci.ControlInput()
            nullControlInput.setEnvT(self.envT)
            coefs = ce.ODECoefs()
            coefs.setCoefs([0.0, 0.0])
            nullControlInput.setCoef(coefs)

            disturbance = d.Disturbance(disturbanceF, env, self.envT)

            # def __init__(self, deltaT, startT, endT, startX, startXDot, f, env, envT, controlInput, controlInputNominal, disturbance):
            odeEngine = euler.ODEOneDimEulerMethod(self.deltaT, self.startT, self.endT,
                                                   startX, startXDot, f, 
                                                   env, self.envT, forceControlInput, nullControlInput, disturbance)
            
            # def __init__(self, r, cx0, cy1, odeEngine, controlInput):
            p = particle.SimpleParticle(0.2, 0.1 * i, 0.5, odeEngine, forceControlInput)
            self.manager.addParticle(p)
            
        return self
    
    def inc(self):
        self.manager.interactAll()
        self.manager.incAll()

        return self
    
    def render(self):

       self.manager.renderAll()

       return self

    def runGlut(self):
       glutInit(sys.argv)
       glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
       glutInitWindowSize(600, 600)
       glutInitWindowPosition(200, 200)
       glutCreateWindow(b"Particle World")
       glutMouseFunc(my_glut_mouse)
       my_glut_init()
       glutDisplayFunc(my_glut_display)
       glutMainLoop()

# Although it is not static, it is treated as singleton. Thus, it is
# OK to init world at this scope. This could be refered by another module.
world = ParticleWorld()