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

    # it is supposed that this similator is small/mid size only
    # and thus, it would be OK to interact to all particles each other
    # considering order of calculation.
    def interactAll(self):
        for p1 in self.innerList:
            for p2 in self.innerList:
                # debug
                # another way of comparison of object?
                # end of debug
                if p1 == p2:
                    continue

                p1.interact(p2)
        
        return self