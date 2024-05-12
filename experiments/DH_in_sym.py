from spatialmath import SE3
import spatialmath.base.symbolic as sym

a = sym.symbol("a")
d = sym.symbol("d")
alph = sym.symbol("alph")
e = sym.symbol("e")

T = SE3.Rx(alph) * SE3.Tx(a) * SE3.Tz(d) * SE3.Rz(e)
T.print()
