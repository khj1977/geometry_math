class ParticleManager:
    
    def __init__(self):
        self.innerList = []

    def addParticle(self, aParticle):
        self.innerList.append(aParticle)

        return self

    def getParticles(self):
        pass

    def getParticle(self, id):
        pass

    def renderAll(self):
        # debug
        # put OpenGL related func call should be here?
        for p in self.innerList:
            p.render()
        # end of debug

        return self