from com_gmail_eulerbonjour.ode_solver import ode_env as oenv

class SimpleParticleStrategy:

    def __init__(self, that):
         self.that = that

    def interact(self, anotherParticle):
        # debug
        # impl interaction between paricles such as apply force or resistance.
        # Using odeEnv, set x and xdot to reverse direction.
        env = self.that.getEnv()
        norm = self.that.get2Norm(anotherParticle)

        thNorm = self.that.getThNorm()

        # thNorm could be r of paricle.
        if (norm < thNorm):
            # not required since making direction of x could be OK but not negative position.
            # direction would be changed only by speed or xdot.
            # env.setX(-1.0 * env.getX())
            env.setXDot(-1.0 * env.getXDot())

        # add how to apply force. It might be via disturbance of ODE engine.
        gravity = self.that.calcGravity(anotherParticle)
        # ignore mass
        self.that.forceControlInput.setNumericInput(gravity)
        # end of debug