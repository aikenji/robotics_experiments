# preamble
import spatialmath.base.symbolic as sym
from spatialmath import SE3

# symbols setup
L1 = sym.symbol("L1")
L2 = sym.symbol("L2")
e1 = sym.symbol("e1")
e2 = sym.symbol("e2")
e3 = sym.symbol("e3")

T_10 = SE3.Rz(e1)
T_21 = SE3.Tx(L1) * SE3.Rz(e2)
T_32 = SE3.Tx(L2) * SE3.Rz(e3)

T_30 = T_21 * T_32
print(T_30)
