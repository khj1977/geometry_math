class SimpleMesh:

    def __init__(self, rows, cols, minX, maxX, minY, maxY):
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
        # self.internalMatrix = np.zeros((rows, cols))

        self.internalMatrix = []

        for i in range(rows + 1):
            self.internalMatrix.append([])
            for j in range(cols + 1):
                self.internalMatrix[i].append(0.0)

        return self

    def fillInternalMatrixByFalse(self):
        i = 0
        j = 0
        while True:
            if (i > self.rows):
                break
            while True:
                if (j > self.cols):
                    break

                self.internalMatrix[i][j] = False

                j = j + 1
            i = i + 1

        return self

    def addParticle(self, row, col, particle):
        self.internalMatrix[row][col] = particle

        return self
    
    def addParticleByGlutPosition(self, x, y, particle):
        row = int(self.xScale * x)
        col = int(self.yScale * y)

        # self.internalMatrix[row][col] = particle
        self.addParticle(row, col, particle)

        return self
    
    def getParticle(self, row, col):
        return self.internalMatrix[row][col]
    
    def getParticleByGlutPosition(self, x, y):
        row = int(self.xScale * x)
        col = int(self.yScale * y)

        return self.getParticle(row, col)

    def calcScale(self):
        self.xScale = self.rows / (self.maxX - self.minX)
        self.yScale = self.cols / (self.maxY - self.minY)

        return self

    def getParticlesAroundIt(self, x, y, th):
        row = int(self.xScale * x)
        col = int(self.yScale * y)

        i = -1.0 * th
        j = -1.0 * th

        particles = []
        while True:
            if (i > th):
                break
            while True: 
                if (j > th):
                    break

                if (i == 0 and j == 0):
                    j = j + 1
                    continue

                crow = int(row + i)
                ccol = int(col + j)

                p = self.getParticle(crow, ccol)
                particles.append(p)

                j = j + 1
            i = i + 1
            

        return particles
