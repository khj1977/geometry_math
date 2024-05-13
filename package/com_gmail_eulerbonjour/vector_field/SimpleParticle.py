import sys
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

import math as m

from com_gmail_eulerbonjour.ode_solver import ode_euler as euler
from com_gmail_eulerbonjour.ode_solver import ode_env as oenv
from com_gmail_eulerbonjour.ode_solver import ode_programmable_input as pi

class SimpleParticle:

    def __init__(self, r, cx0, cy1, odeEngine):
        self.r = r

        self.cx = cx0
        self.cy = cy1
        
        self.theta = 0
        self.deltaTheta = 0.1

        # self.thNorm = 0.01
        self.theNorm = self.r

        # or even obtain env via engine?
        self.oenv = self.odeEngine.getEnv()

        self.odeEngine = odeEngine

        self.forceInput = pi.ProgrammableInput()
        self.odeEngine.setControlInput(self.forceInput)

    def render(self):
        glBegin(GL_POLYGON)
        glColor3d(0.0, 0.0, 1.0)
        while True:
            if self.theta > 3.14 * 2.0:
                break
       
            glVertex3d(self.r * m.cos(self.theta) + self.cx, self.r * m.sin(self.theta) + self.cy, 0.0)

            self.theta = self.theta + self.deltaTheta
        glEnd()

        return self

    def setCentre(self, cx, cy):
        self.cx = cx
        self.cy = cy

        return self
    
    def getCentreX(self):
        return self.cx
    
    def getCentreY(self):
        return self.cy
    
    def interact(self, anotherParticle):
        # debug
        # impl interaction between paricles such as apply force or resistance.
        # Using odeEnv, set x and xdot to reverse direction.
        env = self.oenv
        norm = self.get2Norm(anotherParticle)

        # thNorm could be r of paricle.
        if (norm < self.thNorm):
            # not required since making direction of x could be OK but not negative position.
            # direction would be changed only by speed or xdot.
            # env.setX(-1.0 * env.getX())
            env.setXDot(-1.0 * env.getXDot())

        # add how to apply force. It might be via disturbance of ODE engine.
        gravity = self.calcGravity(anotherParticle)
        # ignore mass
        self.forceInput.setNumericInput(gravity)
        # end of debug

    def calcGravity(self, anotherParticle):
        norm = self.get2Norm(anotherParticle)
        k = 1.0
        # debug
        # force as scalar or vector?
        force = k / norm*norm
        # end of debug

        return force
    
    def get2Norm(self, anotherParticle):
        x1 = self.getCentreX()
        x2 = anotherParticle.getCentreX()

        y1 = self.getCentreY()
        y2 = anotherParticle.getCentreY()

        xx = x2 - x1
        yy = y2 - y1

        norm = m.sqrt(xx * xx + yy * yy)

        return norm
    
    # debug
    # use to calc next (cx, cy) by euler solver with gravity of each particle.
    # end of debug
    def inc(self):
        self.odeEngine.inc()

        cx = self.oenv.getX()
        cy = self.oenv.getXDot()

        self.setCentre(cx, cy)

        return self