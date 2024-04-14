from sys import set_int_max_str_digits
import spatialmath.base.symbolic as sym
from spatialmath import SE3
from matplotlib import pyplot as plt
from sympy.solvers.diophantine.diophantine import diop_general_sum_of_squares

alpha = sym.symbol("alpha")
T = SE3.Rx(alpha)
print(T)
R = SE3.Rz(90, "deg") * SE3.Rx(90, "deg") * SE3.Rz(90, "deg")
R.print()
R0 = SE3()
R0.plot(frame="A", color="blue", width=2)
R.plot(frame="B", color="red", width=2)
R.animate(frame="B", color="green", repeat=True)
plt.show()
