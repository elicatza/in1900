#!/usr/bin/env python3

import numpy as np
import math
import random

def mean(x_list):
    assert len(x_list) != 0
    sum = 0
    for i in x_list:
        sum += i
        
    return sum / len(x_list)

def standard_deviation(x_list):
    assert len(x_list) != 0
    x_mean = mean(x_list)
    sum = 0
    for x in x_list:
        sum += (x - x_mean) ** 2

    return math.sqrt(sum / len(x_list))

def test_mean():
    x_list = []
    random.seed(1)
    for i in range(20):
        x_list.append(random.randint(0, 10))


    tol = 1E-14
    my_mean = mean(x_list)
    np_mean = np.mean(x_list)
    assert abs(4.85 - my_mean) < tol
    assert abs(4.85 - np_mean) < tol
    assert abs(my_mean - np_mean) < tol

def test_standard_diviation():
    x_list = []
    random.seed(1)
    for i in range(20):
        x_list.append(random.randint(0, 10))


    tol = 1E-14
    my_std = standard_deviation(x_list)
    np_std = np.std(x_list)
    expected = 3.102821296820041
    assert abs(expected - my_std) < tol
    assert abs(expected - np_std) < tol
    assert abs(my_std - np_std) < tol

if __name__ == "__main__":
    test_mean()
    test_standard_diviation()
    print("[INFO] No errors", file=sys.stderr)


# ./statistics.py stderr:
# [INFO] No errors
