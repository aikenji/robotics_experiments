# preamble
import numpy as np
from matplotlib import pyplot as plt
from roboticstoolbox import DHRobot, RevoluteMDH


deg = np.pi / 180


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

# find coordinate of P
T_30 = bot1.fkine([10 * deg, 20 * deg, 30 * deg])
print(T_30)
p_3 = [1, 0, 0]
p_0 = T_30 * p_3
print(p_0)
