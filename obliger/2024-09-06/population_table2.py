#!/usr/bin/env python3

import math

B = 50000
k = 0.2
t = 0
n_0 = 5000

# Solve for C when population = 5_000 and t = 0
# 5_000 = 50_000 / (1 + C * e^(-k * t))
# 5_000 = 50_000 / (1 + C * e^0)
# 5_000 = 50_000 / (1 + C)
# 1 = 10 / (1 + C)
# 1 * (1 + C) = 10
# 1 + C = 10
# C = 9
C = 9

def population(t):
    return B / (1 + C * math.pow(math.e, -k * t))

assert int(population(0)) == 5_000


# Part a)
n = 12
t = []
N = []

for i in range(0, 48 + 1, int(48 / n)):
    t.append(i)
    N.append(population(i))

print(f"Time\tPopulation")
tN1 = [t, N]
for pairs in zip(tN1[0], tN1[1]):
      print(f"{pairs[0]:4.0f}\t{pairs[1]:10.0f}")


# Part b)
tN2 = []
for i in range(0, 48 + 1, int(48 / n)):
    tN2.append([i, population(i)])

print(f"Time\tPopulation")
for pairs in tN2:
      print(f"{pairs[0]:4.0f}\t{pairs[1]:10.0f}")

# Solution stdout:
# Time	Population
#    0	      5000
#    4	      9913
#    8	     17749
#   12	     27526
#   16	     36580
#   20	     42924
#   24	     46552
#   28	     48390
#   32	     49263
#   36	     49666
#   40	     49849
#   44	     49932
#   48	     49970
# Time	Population
#    0	      5000
#    4	      9913
#    8	     17749
#   12	     27526
#   16	     36580
#   20	     42924
#   24	     46552
#   28	     48390
#   32	     49263
#   36	     49666
#   40	     49849
#   44	     49932
#   48	     49970
