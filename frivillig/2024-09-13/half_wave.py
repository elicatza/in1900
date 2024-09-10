#!/usr/bin/env python3

import math
import sys

def f(x):
    sinx = math.sin(x)
    if sinx > 0:
        return sinx
    else:
        return 0

def test_f():
    test_vals = [x / (0.5 * math.pi) for x in range(20)]
    # [0.0, 0.63, 1.27, 1.90, 2.54, 3.18, 3.81, 4.45, 5.09, 5.72, 6.36, 7.00, 7.63, 8.27, 8.91, 9.54, 10.18, 10.82, 11.45, 12.09]
    for i in test_vals:
        assert f(i) >= 0.0

if __name__ == '__main__':
    test_f()
    print("[INFO] No errors", file=sys.stderr)

# ./half_wave.py stderr:
# [INFO] No errors
