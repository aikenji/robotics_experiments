from spatialmath import SE3
from matplotlib import pyplot as plt

lims = [-1, 5, -1, 5, -1, 5]
T0 = SE3()
T0.plot(frame="A", color="blue", width=2, dims=lims)

T = SE3.Ty(4) * SE3.Rx(90, "deg")
T.animate(frame="B", color="pink", width=2, repeat=True)
T.plot(frame="B", color="red", width=2, dims=lims)

plt.show()
