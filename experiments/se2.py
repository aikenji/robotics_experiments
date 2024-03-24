from spatialmath import SE2
from matplotlib import pyplot as plt

T = SE2(1, 0, 90, unit="deg")

T_i = T.inv()
T_i.print()
T_i.animate(frame="A", color="red")

plt.show()
