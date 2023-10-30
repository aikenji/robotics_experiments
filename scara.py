import roboticstoolbox as rtb
import numpy as np
from roboticstoolbox import DHRobot, RevoluteMDH, PrismaticMDH
from numpy import pi
from matplotlib import pyplot as plt


class Scara(DHRobot):
    def __init__(self):
        L = [
            RevoluteMDH(d=3.0),
            RevoluteMDH(a=1.0),
            PrismaticMDH(a=0.5, alpha=pi, qlim=[0.0, 2.0]),
            RevoluteMDH(),
        ]

        super().__init__(L, name="Scara")

        self.qz = np.array([0, 0, 0, 0])
        self.addconfiguration("qz", self.qz)


robot = Scara()
print(robot)
robot.plot(robot.qz)
plt.show()
robot.teach(robot.qz)

for i in np.arange(-2.0, 2.0, 0.1):
    T = robot.fkine([i, 0.2, 0.3, 0.4])
    # 	print(T)

    sol = robot.ikine_LM(T, q0=np.array([0, 0, 0, 0]), mask=[1, 1, 1, 0, 0, 1])

    print(sol.q)
    T_sol = robot.fkine(sol.q)
    print(T_sol)

T0 = robot.fkine([0.0, 0.0, 0.0, 0.0])
print(T0)
