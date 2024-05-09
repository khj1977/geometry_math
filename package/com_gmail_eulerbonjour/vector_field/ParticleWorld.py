from com_gmail_eulerbonjour.ode_solver import ode_euler as euler
from com_gmail_eulerbonjour.ode_solver import ode_env as env
from com_gmail_eulerbonjour.vector_field import ParticleManager as manager

class ParticleWorld:

    def __init__(self):
        self.manager = manager.ParticleManager()