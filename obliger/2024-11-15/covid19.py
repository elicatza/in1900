#!/usr/bin/env python3

from SEIR import SEIR, solve_SEIR, plot_SEIR
from lockdown import Beta
from scipy.integrate import solve_ivp

# Problem 5

class SEIRimport(SEIR):
    def __init__(self, beta=0.33, sigma=10, r_ia=0.1,
                 r_e2=1.25, lmbda_1=0.33,
                 lmbda_2=0.5, p_a=0.4, mu=0.2):

        super().__init__(beta, r_ia, r_e2, lmbda_1, lmbda_2, p_a, mu)
        self.sigma = sigma

    def __call__(self, t, u):
        diff = super().__call__(t, u)
        diff[2] += self.sigma
        return diff


def solve_SEIR(T, S_0, E2_0, beta, sigma):
    sol = solve_ivp(SEIRimport(beta, sigma), (0, T), [S_0, 0, E2_0, 0, 0, 0])
    return (sol.t, sol.y)


if __name__ == '__main__':
    beta = Beta("./beta_values.txt")
    t, u = solve_SEIR(T=1000, S_0=5.5e6, E2_0=100, beta=beta, sigma=10)
    plot_SEIR(t, u)

# /usr/bin/env python3 lockdown.py stdout:
"""
written plot to `covid19.py.output.png`
"""

# Kommentar problem 5
"""
Forskjellen fra Problem 4 er at økninger i beta skaper nye bølger med covid-19.
Fordi det ikke er mulig å utrydde covid-19 i Problem 5, reflekterer økningen i
beta over tidsintervaller.
"""
