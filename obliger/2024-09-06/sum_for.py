#!/usr/bin/env python3

s = 0
M = 3

# -- for i in range(M):  # 1. Wrong sum range. Math sigma (sum) is inclusive on both sides. This code generates [0, 1, 2], not [1, 2, 3]
for i in range(1, M + 1):  # Generator which yields [1, 2, 3]
    # -- s += 1/2*k**2  # 2. Wrong order of operation. k is squared not (2 * k)
    # -- s += 1/2*k**2  # 3. k is not defined, use i instead
    s += 1/(2*i)**2

print(s)

# Solution stdout:
# 0.3402777777777778

