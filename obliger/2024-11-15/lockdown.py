#!/usr/bin/env python3

from SEIR import solve_SEIR, plot_SEIR
from datetime import date, timedelta
import __main__
import matplotlib.pyplot as plt
import numpy as np
import os

# Problem 4

def beta(t):
    t = np.asarray(t)
    return np.where(t < 30, 0.4, 0.083)

def parse_date(datestr):
    """
    Parse datestring into datetime date object.
    Datestr format: `dd.mm.yyyy`.
    """
    day, month, year = (int(x) for x in datestr.split('.'))
    return date(year, month, day)


class Beta:
    def __init__(self, filename):

        betas = []
        times = []
        with open(filename, 'r') as fp:
            for i, line in enumerate(fp):
                # Skip the first two lines
                if i < 2:
                    continue
                if i == 2:
                    time0 = parse_date(line.split()[0])

                betas.append(float(line.split()[2]))
                times.append((parse_date(line.split()[0]) - time0).days)

        # Create lookup table of beta values
        self.beta_table = []
        for i in range(len(times) - 1):
            self.beta_table += (times[i + 1] - times[i]) * [float(betas[i])]

        self.beta_table += [betas[-1]]
        self.beta_table = np.asarray(self.beta_table)


    def __call__(self, t):
        # Beta lookup O(1)
        t = np.asarray(t)
        t = np.int32(np.minimum(np.trunc(t), len(self.beta_table) - 1))
        return self.beta_table[t]

    def plot(self, T):
        t = np.linspace(0, T, 1000)
        b = self(t)
        plt.plot(t, b)
        plt.title('model av beta verdier under COVID-19')
        plt.xlabel('Tid [dager]')
        plt.ylabel('β')
        filename = f'{os.path.basename(__main__.__file__)}.output_beta.png'
        plt.savefig(filename)
        print(f"written plot to `{filename}`")
        plt.show()


if __name__ == '__main__':
    beta = Beta("./beta_values.txt")
    beta.plot(1000)
    t, u = solve_SEIR(T=1000, S_0=5.5e6, E2_0=100, beta=beta)
    plot_SEIR(t, u)


# /usr/bin/env python3 lockdown.py stdout:
"""
written plot to `lockdown.py.output_beta.png`
written plot to `lockdown.py.output.png`
"""

# Kommentar problem 4
"""
På slutten ser vi at antallet infiserte nærmer seg 0, men veldig sakte.
"""

