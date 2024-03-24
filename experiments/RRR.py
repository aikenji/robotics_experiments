# preamble
from numpy import pi
import numpy as np
from matplotlib import pyplot as plt
from roboticstoolbox import DHRobot, RevoluteMDH, PrismaticMDH


# build the robot class
class RRR(DHRobot):
    def __init__(self):
        # write in your DH numbers of robot
        L1 = RevoluteMDH()
        L2 = RevoluteMDH(a=1)
        L3 = RevoluteMDH(a=2)
        super().__init__([L1, L2, L3], name="RRR")

        self.qz = np.array([0, 0, 0])
        self.addconfiguration("qz", self.qz)


# build my first bot
bot1 = RRR()
print(bot1)
bot1.teach(bot1.qz)
