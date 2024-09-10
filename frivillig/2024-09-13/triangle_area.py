#!/usr/bin/env python3

import sys


def triangle_area(vertices):
    # Validate input
    assert len(vertices) == 3
    for i in range(3):
        assert len(vertices[i]) == 2

    v0 = vertices[0]
    v1 = vertices[1]
    v2 = vertices[2]
    return 0.5 * (v1[0] * v2[1] - v2[0] * v1[1] - v0[0] * v2[1] + v2[0] * v0[1] + v0[0] * v1[1] - v1[0] * v0[1])
    

def test_triangle_area():
    """
    Verify the area of a triangle with vertices
    (0,0), (1,0), and (0,2).
    """
    v1 = [0,0];
    v2 = [1,0];
    v3 = [0,2]
    vertices = [v1, v2, v3]
    expected = 1
    computed = triangle_area(vertices)
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = f"computed area={computed} != {expected}(expected)"
    assert success, msg

if __name__ == '__main__':
    test_triangle_area()
    print("[INFO] No errors", file=sys.stderr)

# ./triangle_area.py stderr:
# [INFO] No errors
