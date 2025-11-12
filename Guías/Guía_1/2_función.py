import numpy as np
import mathplotlib.pyplot as plt
import math

class FunciónTrigonométrica():
    def __init__(self, tipo, amplitud=1, periodo=2*math.pi):
        self.tipo = tipo.lower()
        self.amplitud