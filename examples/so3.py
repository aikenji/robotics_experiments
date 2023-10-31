from sys import set_int_max_str_digits
import spatialmath.base.symbolic as sym
from spatialmath import SE3
from matplotlib import pyplot as plt
from sympy.solvers.diophantine.diophantine import diop_general_sum_of_squares

theta = sym.symbol("theta")
print(SE3.Ry(theta))

# R = SE3.Rz(90, "deg") * SE3.Rx(90, "deg") * SE3.Rz(90, "deg")
# R.print()
