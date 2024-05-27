import numpy as np

class SimpleMesh:

    def __init__(self, rows, cols, minX, minY, maxX, maxY):
        self.internalMatrix = np.zeros((rows, cols))

        self.rows = rows
        self.cols = cols

        self.minX = minX
        self.maxX = maxX
        self.minY = minY
        self.maxY = maxY

        self.calcScale()

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


