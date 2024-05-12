import spatialmath.base.symbolic as sym
import numpy as np
from spatialmath import SE3, SO3, Line3
from matplotlib import pyplot as plt

# alpha = sym.symbol("alpha")
# T = SE3.Rx(alpha)
# T.print()

# original frame
R0 = SE3()
R0.plot(frame="A", color="blue", width=2)

# R = SE3.Rz(90, "deg") * SE3.Rx(90, "deg") * SE3.Rz(90, "deg")
# R.print()
# R.plot(frame="B", color="red", width=2)
# R.animate(frame="B", color="green", repeat=True)

R1 = SO3(np.array([[0, 0, 1], [0, -1, 0], [1, 0, 0]]))
R1.print()
R1.animate(frame="B", color="purple", width=2, repeat=True)

# plot the axis of rotation
a = Line3.Join(R1.angvec("deg")[1], [0, 0, 0])
a.plot(color="red", ls="-")
plt.show()
