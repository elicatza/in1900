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

        self.betas = []
        self.times = []
        with open(filename, 'r') as fp:
            for i, line in enumerate(fp):
                # Skip the first two lines
                if i < 2:
                    continue
                if i == 2:
                    self.time0 = parse_date(line.split()[0])

                self.betas.append(float(line.split()[2]))
                self.times.append((parse_date(line.split()[0]) - self.time0).days)

    def __call__(self, t):
        # TODO Could speed up function by making a lookup table O(1)
        # id = max(int(t), self.times[-1])
        # return self.betas[id]
        prev_beta = self.betas[0]
        for ti, bi in zip(self.times, self.betas):
            if ti > t:
                break
            prev_beta = bi

        return prev_beta

    def plot(self, T):
        t = np.linspace(0, T, 1000)
        # TODO: vectorise
        b = [self(i) for i in t]
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

