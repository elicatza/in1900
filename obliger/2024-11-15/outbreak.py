#!/usr/bin/env python3

from SEIR import solve_SEIR, plot_SEIR
from datetime import date, timedelta
import numpy as np

# Problem 3

def beta(t):
    t = np.asarray(t)
    return np.where(t < 30, 0.4, 0.083)

def R(t):
    return 1.25 * beta(t)/0.5 + 0.1 * beta(t)/0.2 + beta(t)/0.2


if __name__ == '__main__':
    print(f"På starten er R = {R(0):.2f}")
    print(f"Etter hvert blir R = {R(60):.2f}")

    t, u = solve_SEIR(T=300, S_0=5.5e6, E2_0=100, beta=beta)
    plot_SEIR(t, u)


# /usr/bin/env python3 outbreak.py stdout:
"""
På starten er R = 3.20
Etter hvert blir R = 0.66
written plot to `outbreak.py.output.png`
"""

# Kommentar problem 3
"""
Fordi β verdien synker til 0.083, blir R = 0.66. Dette betyr at en infisert
person smitter i snitt 0.66 personer. På grunn av den korte (µ = 0.2)
levetiden, kommer antallet infiserte halvere ganske raskt og viruset dør ut.
Dette ser vi tydelig i `./outbreak.py.output.png`
"""
