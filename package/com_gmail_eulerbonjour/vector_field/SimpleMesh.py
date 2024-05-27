import numpy as np

class SimpleMesh:

    def __init__(self, rows, cols, minX, minY, maxX, maxY):
        # self.internalMatrix = np.zeros((rows, cols))
        self.clearInternalMatrix(rows, cols)

        self.rows = rows
        self.cols = cols

        self.minX = minX
        self.maxX = maxX
        self.minY = minY
        self.maxY = maxY

        self.calcScale()

    def clearInternalMatrix(self, rows, cols):
        self.internalMatrix = np.zeros((rows, cols))

        return self

    def addParticle(self, row, col, particle):
        self.internalMatrix[row][col] = particle

        return self
    
    def addParticleByGlutPosition(self, x, y, particle):
        row = self.xScale * x
        col = self.yScale * y

        # self.internalMatrix[row][col] = particle
        self.addParticle(row, col, particle)

        return self
    
    def getParticle(self, row, col):
        return self.internalMatrix[row][col]
    
    def getParticleByGlutPosition(self, x, y):
        row = self.xScale * x
        col = self.yScale * y

        return self.getParticle(row, col)

    def calcScale(self):
        self.xScale = self.rows / (self.maxX - self.minX)
        self.yScale = self.cols / (self.maxY - self.minY)

        return self

    def getParticlesAroundIt(self, x, y, th):
        row = self.xScale * x
        col = self.yScale * y

        i = -1.0 * th
        j = -1.0 * th

        particles = []
        while True:
            if (i > th):
                break

            if (j > th):
                break

            crow = row + i
            ccol = col + j

            p = self.getParticle(crow, ccol)
            particles.append(p)

            i = i + 1
            j = j + 1

        return particles
