from com_gmail_eulerbonjour.ode_solver import ode_euler as euler
from com_gmail_eulerbonjour.ode_solver import ode_env as env
from com_gmail_eulerbonjour.ode_solver import ode_programmable_input as pi
from com_gmail_eulerbonjour.ode_solver import ode_control_input as ci
from com_gmail_eulerbonjour.ode_solver import ode_coefs as ce
from com_gmail_eulerbonjour.ode_solver import ode_time as time
from com_gmail_eulerbonjour.vector_field import SimpleParticleManager as manager
from com_gmail_eulerbonjour.vector_field import SimpleParticle as particle

class ParticleWorld:

    def __init__(self):
        self.startT = 0.0
        self.endT = 10000.0
        self.deltaT = 0.01
        self.envT = time.ODETime(self.startT, self.endT, self.deltaT)

        self.manager = manager.SimpleParticleManager(self.envT)

    def initialize(self):     
        for i in range(2):
            f = lambda t, x, xDot: -0.2 * x
            disturbance = lambda t, x, xDot: 0.0

            startX = 0.0
            startXDot = 0.1
            env = env.ODEEnv().setX(startX).setXDot(startXDot)

            forceControlInput = pi.ProgrammableInput()

            nullControlInput = ci.ControlInput()
            nullControlInput.setEnvT(self.envT)
            coefs = ce.ODECoefs()
            coefs.setCoefs([0.0, 0.0])
            nullControlInput.setCoef(coefs)

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