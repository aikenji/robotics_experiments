# preambles
import spatialmath.base.symbolic as sym
from spatialmath import SE3

# symbols setup
alph = sym.symbol("alph")
a = sym.symbol("a")
d = sym.symbol("d")
e = sym.symbol("e")

S1 = SE3.Tx(a) * SE3.Rx(alph)
S2 = SE3.Tz(d) * SE3.Rz(e)
T = S1 * S2

T.print()
