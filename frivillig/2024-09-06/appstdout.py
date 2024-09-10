#!/usr/bin/env python3


import subprocess
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: ./appstdout.py <filename>")
        sys.exit(0)

    print(sys.argv[0], sys.argv[1])
    print(f"Running: {sys.argv[1]}")
    # subprocess.popen
    process = subprocess.run("echo", "Hello world")
    # process = subprocess.run("python3", sys.argv[1])
