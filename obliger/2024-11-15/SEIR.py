#!/usr/bin/env python3

from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import os
import __main__

# Oppgave a)
# Jeg brukte følgende regex i __call__ metoden: s/beta/beta(t)/g

# I do not own the following python class
# This file is downloaded from: https://github.com/sundnes/solving_odes_in_python/raw/refs/heads/master/docs/src/chapter5/SEEIIR.py
# Download git hash 21b2caa
# NOTE: I have modified the original source
class SEIR:
    def __init__(self, beta=0.33, r_ia=0.1,
                 r_e2=1.25, lmbda_1=0.33,
                 lmbda_2=0.5, p_a=0.4, mu=0.2):

        if isinstance(beta, (float, int)):
            self.beta = lambda t: beta
        elif callable(beta):
            self.beta = beta
        else:
            assert TypeError

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

        # I have applied regex search replace s/beta/beta(t)/g
        S, E1, E2, I, Ia, R = u
        N = sum(u)
        dS = -beta(t) * S * I / N - r_ia * beta(t) * S * Ia / N \
            - r_e2 * beta(t) * S * E2 / N
        dE1 = beta(t) * S * I / N + r_ia * beta(t) * S * Ia / N \
            + r_e2 * beta(t) * S * E2 / N - lmbda_1 * E1
        dE2 = lmbda_1 * (1 - p_a) * E1 - lmbda_2 * E2
        dI = lmbda_2 * E2 - mu * I
        dIa = lmbda_1 * p_a * E1 - mu * Ia
        dR = mu * (I + Ia)
        return [dS, dE1, dE2, dI, dIa, dR]


# Oppgave b)
# Byttet `SEIR0` til `SEIR`
# Satt in verdiene for beta = float og beta = callable

def cmp_float_iter(a, b, tol=1e-10):
    """Compare float iterables. Return 0 if equal. Else it returns a - b.
    See strcmp(3) for design
    """
    assert len(a) == len(b)
    for ai, bi in zip(a, b):
        diff = abs(ai - bi)
        if diff > tol:
            return ai - bi
    return 0


def test_SEIR_beta_const():
    spread = SEIR(beta=0.33)
    tol = 1e-10

    # Se SEIR0 Oppgave a) for utregning av følgende verdier
    expected = [-0.12925, -0.20075, -0.302, 0.3, -0.068, 0.4]
    actual = spread(0, [1, 1, 1, 1, 1, 1])
    assert cmp_float_iter(expected, actual) == 0

    actual = spread(0, [1, 2, 1, 1, 1, 1])
    assert cmp_float_iter(expected, actual) != 0

def test_SEIR_beta_var():
    spread = SEIR(beta=lambda t: 0.33)
    tol = 1e-10

    # Se SEIR0 Oppgave a) for utregning av følgende verdier
    expected = [-0.12925, -0.20075, -0.302, 0.3, -0.068, 0.4]
    actual = spread(0, [1, 1, 1, 1, 1, 1])
    assert cmp_float_iter(expected, actual) == 0

    actual = spread(0, [1, 2, 1, 1, 1, 1])
    assert cmp_float_iter(expected, actual) != 0



# Oppgave c)
# Byttet `SEIR0` til `SEIR`
def solve_SEIR(T, S_0, E2_0, beta):
    solution = solve_ivp(SEIR(beta), (0, T), [S_0, 0, E2_0, 0, 0, 0])
    return (solution.t, solution.y)

# Oppgave d)
def plot_SEIR(t, u, components=['S', 'I', 'Ia', 'R']):
    for i, val in enumerate(['S', 'E1', 'E2', 'I', 'Ia', 'R']):
        if val in components:
            plt.plot(t, u[i], label=val)

    plt.legend()
    plt.title('SEEIIR model av COVID-19 utvikling')
    plt.xlabel('Tid [dager]')
    plt.ylabel('Personer')
    filename = f'{os.path.basename(__main__.__file__)}.output.png'
    plt.savefig(filename)
    print(f"written plot to `{filename}`")
    plt.show()

if __name__ == '__main__':
    test_SEIR_beta_const()
    test_SEIR_beta_var()

    t, u = solve_SEIR(T=300, S_0=5.5e6, E2_0=100, beta=0.4)

    print(f"Maks syke(I) samtidig: {max(u[3]):.0f}")
    print(f"Hvis 20% måtte bli innlagt på sykehus, måtte det ha vært {max(u[3]) * 0.2:.0f} sykephuslasser.")
    print(f"Hvis 5% trengte respiratorer, måtte sykehusene ha hatt {max(u[3]) * 0.05:.0f} respiratorer.")
    print(f"På Norske sykehus var det omtrent 700 respiratorer.")

    plot_SEIR(t, u)

# /usr/bin/env python3 SEIR.py stdout:
"""
Maks syke(I) samtidig: 258168
Hvis 20% måtte bli innlagt på sykehus, måtte det ha vært 51634 sykephuslasser.
Hvis 5% trengte respiratorer, måtte sykehusene ha hatt 12908 respiratorer.
På Norske sykehus var det omtrent 700 respiratorer.
written plot to `SEIR.py.output.png`
"""

# Kommentar e)
"""
Det er (12908 - 700) 12208 respiratorer for få hvis man ikke reduserer
hvor raskt viruset sprer seg -- dvs. lavere β. Uten tiltak risikerer man
flere tusen dødsfall ukentlig, utifra de første estimatene av COVID-19.
"""
