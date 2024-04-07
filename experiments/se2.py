from spatialmath import SE2
from matplotlib import pyplot as plt

T = SE2(1, 1, 60, unit="deg")
T_1 = SE2(0, 0, 30, unit="deg")
T_0 = SE2(0, 0, 0, unit="deg")
p = [1, 0]
lim = [-3, 3, -3, 3]

# T_i = T.inv()
# T_i.print()
pp = T_1 * p
print(pp)

T.animate(frame="B", color="red", width=1, dims=lim, repeat=True)
T.plot(frame="B", color="red", width=1, dims=lim)
T_0.plot(frame="A", color="blue", width=1, dims=lim)

plt.show()
