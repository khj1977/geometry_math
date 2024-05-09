import sys
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

import math as m

class SimpleParticle:

    def __init__(self, r, cx0, cy1):
        self.r = r

        self.cx = cx0
        self.cy = cy1
        
        self.theta = 0
        self.deltaTheta = 0.1

    def render(self):
        glBegin(GL_POLYGON)
        glColor3d(0.0, 0.0, 1.0)
        while True:
            if self.theta > 3.14 * 2.0:
                break
       
            glVertex3d(r * m.cos(theta2) + cx, r * m.sin(theta2) + cy, -2.0)

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
    
    def calcGravity(self, anotherParticle):
        norm = self.get2Norm(anotherParticle)
        k = 1.0
        force = k / norm*norm

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