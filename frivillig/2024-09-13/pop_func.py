#!/usr/bin/env python3

import math

# Constants
B = 50000
k = 0.2
t = 0       # Hours
t_max = 48  # Hours
n_0 = 5000  # Inital population
C = 9


def population(t, k, B, C):
    return B / (1 + C * math.exp(-k*t))


print(f"Time (h)\tPopulation")
for i in range(t, t_max + 1, int(t_max / 12)):
    pop = population(i, k, B, C)
    print(f"{i:8.0f}\t{pop:10.0f}")

# ./pop_func.py:
# Time (h)	Population
#        0	      5000
#        4	      9913
#        8	     17749
#       12	     27526
#       16	     36580
#       20	     42924
#       24	     46552
#       28	     48390
#       32	     49263
#       36	     49666
#       40	     49849
#       44	     49932
#       48	     49970

