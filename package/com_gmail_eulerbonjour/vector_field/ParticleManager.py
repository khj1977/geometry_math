import sys
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

from com_gmail_eulerbonjour.ode_solver import ode_time as time

class ParticleManager:
    
    def __init__(self):
        self.innerList = []
        self.envT = time.ODETime(0.0, 1000.0, 0.01)

    def addParticle(self, aParticle):
        self.innerList.append(aParticle)

        return self

    def getParticles(self):
        return self.innerList

    def getParticle(self, id):
        return self.innerList[id]

    def renderAll(self):
        # debug
        # put OpenGL related func call should be here?
        glClear(GL_COLOR_BUFFER_BIT)

        for p in self.innerList:
            p.render()
        # end of debug

        glFlush()


        return self

    # it is supposed that this similator is small/mid size only
    # and thus, it would be OK to interact to all particles each other
    # considering order of calculation.
    def interactAll(self):
        # skip if pki but pik is executed. It is symmetry.
        # The above assumption may be incorrect considering definition of interact().
        for p1 in self.innerList:
            for p2 in self.innerList:
                # debug
                # another way of comparison of object?
                # end of debug
                if p1 == p2:
                    continue

                p1.interact(p2)
        
        return self
    
    def incAll(self):
        for t in self.envT.startClock():
            for p in self.innerList:
                p.inc()

        return self