#!/usr/bin/env python3

# 4.1 (pop_func.py, side 10),

import math

B = 50000
k = 0.2
t = 0
n_0 = 5000

C = 9

def population(t, k, B, C):
    return B / (1 + C * math.pow(math.e, -k*t))


if __name__ == "__main__":
    print(f"Time  Population")
    for i in range(0, 49, int(48 / 12)):
        pop = population(i, k, B, C)
        print(f"{i:4d}    {pop:8.0f}")

