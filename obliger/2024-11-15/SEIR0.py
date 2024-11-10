#!/usr/bin/env python3

from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# I do not own the following python class
# This file is downloaded from: https://github.com/sundnes/solving_odes_in_python/raw/refs/heads/master/docs/src/chapter5/SEEIIR.py
# Download git hash 21b2caa
# NOTE: I have modified the original source
class SEIR0:
    def __init__(self, beta=0.33, r_ia=0.1,
                 r_e2=1.25, lmbda_1=0.33,
                 lmbda_2=0.5, p_a=0.4, mu=0.2):

        self.beta = beta
        self.r_ia = r_ia
        self.r_e2 = r_e2
        self.lmbda_1 = lmbda_1
        self.lmbda_2 = lmbda_2
        self.p_a = p_a
        self.mu = mu

    def __call__(self, t, u):
        beta = self.beta
        r_ia = self.r_ia
        r_e2 = self.r_e2
        lmbda_1 = self.lmbda_1
        lmbda_2 = self.lmbda_2
        p_a = self.p_a
        mu = self.mu

        S, E1, E2, I, Ia, R = u
        N = sum(u)
        dS = -beta * S * I / N - r_ia * beta * S * Ia / N \
            - r_e2 * beta * S * E2 / N
        dE1 = beta * S * I / N + r_ia * beta * S * Ia / N \
            + r_e2 * beta * S * E2 / N - lmbda_1 * E1
        dE2 = lmbda_1 * (1 - p_a) * E1 - lmbda_2 * E2
        dI = lmbda_2 * E2 - mu * I
        dIa = lmbda_1 * p_a * E1 - mu * Ia
        dR = mu * (I + Ia)
        return [dS, dE1, dE2, dI, dIa, dR]

# Oppgave a)
# Jeg setter inn verdine [1, 1, 1, 1, 1, 1]  for SEEIIR med en tid 0
# Formelene for endrigene er hentet fra ODE boka, side 91.
# Jeg bytter ut SEEIIR verdiene med 1 og fjerner de derfor med en gang.
# Da blir formelene som følgende
# S'(t)   = (-β - r_ia * β - r_e2 * β) / N
# E_1'(t) = β / N + r_ia * β / n + r_ia * β / N - λ_1
# E_2'(t) = λ_1 * (1 - p_a) - λ_2
# I'(t)   = λ_2 - µ
# I_a'(t) = λ_1 * p_a - µ
# R'(t)   = µ (1 + 1)
#
# Setter inn verdiene fra SEIR0.__init__() for symboler:
# beta=0.33, r_ia=0.1, r_e2=1.25, lmbda_1=0.33, lmbda_2=0.5, p_a=0.4, mu=0.2
#
# S'(t)   = (-0.33 - 0.1 * 0.33 - 1.25 * 0.33) / 6
# E_1'(t) = 0.33 / 6 + 0.1 * 0.33 / 6 + 1.25 * 0.33 / 6 - 0.33
# E_2'(t) = 0.33 * (1 - 0.4) - 0.5
# I'(t)   = 0.5 - 0.2
# I_a'(t) = 0.33 * 0.4 - 0.2
# R'(t)   = 0.2 (1 + 1)

# Litt utregning
# S'(t)   = -0.12925
# E_1'(t) = -0.20075
# E_2'(t) = -0.302
# I'(t)   = 0.3
# I_a'(t) = -0.068
# R'(t)   = 0.4
#
# [-0.12925, -0.20075, -0.302, 0.3, -0.068, 0.4]

def cmp_float_iter(a, b, tol=1e-10):
    """Compare float iterables. Return 0 if equal. Else it returns a - b.
    See strcmp(3) for design.
    """
    assert len(a) == len(b)
    for ai, bi in zip(a, b):
        diff = abs(ai - bi)
        if diff > tol:
            return ai - bi
    return 0

def test_SEIR0():
    spread = SEIR0()
    tol = 1e-10

    # Se Oppgave a) for utregning av følgende verdier
    expected = [-0.12925, -0.20075, -0.302, 0.3, -0.068, 0.4]
    actual = spread(0, [1, 1, 1, 1, 1, 1])
    assert cmp_float_iter(expected, actual) == 0

    actual = spread(0, [1, 2, 1, 1, 1, 1])
    assert cmp_float_iter(expected, actual) != 0


# Oppgave b)
def solve_SEIR(T, dt, S_0, E2_0, beta):
    solution = solve_ivp(SEIR0(beta), (0, T), [S_0, 0, E2_0, 0, 0, 0])
    return (solution.t, solution.y)

# Oppgave c)
def plot_SEIR(t, u):
    # solution = solve_SEIR(150, 0.1, 5.5e6, 100, 0.4)
    plt.plot(t, u[0], label='S')
    plt.plot(t, u[3], label='I')
    plt.plot(t, u[4], label='Ia')
    plt.plot(t, u[5], label='R')
    plt.legend()
    plt.title('SEEIIR model av COVID-19 utvikling')
    plt.xlabel('Tid [dager]')
    plt.ylabel('Personer')
    filename = 'SEIR0_output.png'
    plt.savefig(filename)
    print(f"written plot to `{filename}`")
    plt.show()

if __name__ == '__main__':
    test_SEIR0()
    t, u = solve_SEIR(150, None, 5.5e6, 100, 0.4)
    plot_SEIR(t, u)


# /usr/bin/env python3 output:
"""
written plot to `SEIR0_output.png`
"""
