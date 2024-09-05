#!/usr/bin/env python3

MASS_C = 12.011  # g/mol
MASS_H = 1.0079  # g/mol


# Boring solution
for i in range(2, 9 + 1):
    i_h = 2 * (i + 1)
    print(f"M(C{i}H{i_h}){' ' if i_h < 10 else ''} = ", end="")
    print(f"{i * MASS_C + i_h * MASS_H:7.3f} g/mol")

# Boring solution stdout:
# M(C2H6)  =  30.069 g/mol
# M(C3H8)  =  44.096 g/mol
# M(C4H10) =  58.123 g/mol
# M(C5H12) =  72.150 g/mol
# M(C6H14) =  86.177 g/mol
# M(C7H16) = 100.203 g/mol
# M(C8H18) = 114.230 g/mol
# M(C9H20) = 128.257 g/mol



# # Fun solution
# def print_alken(n_carbon):
#     print(f"    ", end="")
#     for i in range(n_carbon):
#         print(f"H   ", end="")
#
#     print(f"\n    ", end="")
#     for i in range(n_carbon):
#         print(f"|   ", end="")
#
#     print(f"\nH---", end="")
#     for i in range(n_carbon):
#         print(f"C---", end="")
#
#     print(f"H\n    ", end="")
#     for i in range(n_carbon):
#         print(f"|   ", end="")
#
#     print(f"\n    ", end="")
#     for i in range(n_carbon):
#         print(f"H   ", end="")
#     print("")
#
# for i in range(2, 9 + 1):
#     i_h = 2 * (i + 1)
#     print(f"\n{i * MASS_C + i_h * MASS_H:7.3f} g/mol")
#     print_alken(i)

# Fun solution stdout:
#  30.069 g/mol
#     H   H
#     |   |
# H---C---C---H
#     |   |
#     H   H
#
#  44.096 g/mol
#     H   H   H
#     |   |   |
# H---C---C---C---H
#     |   |   |
#     H   H   H
#
#  58.123 g/mol
#     H   H   H   H
#     |   |   |   |
# H---C---C---C---C---H
#     |   |   |   |
#     H   H   H   H
#
#  72.150 g/mol
#     H   H   H   H   H
#     |   |   |   |   |
# H---C---C---C---C---C---H
#     |   |   |   |   |
#     H   H   H   H   H
#
#  86.177 g/mol
#     H   H   H   H   H   H
#     |   |   |   |   |   |
# H---C---C---C---C---C---C---H
#     |   |   |   |   |   |
#     H   H   H   H   H   H
#
# 100.203 g/mol
#     H   H   H   H   H   H   H
#     |   |   |   |   |   |   |
# H---C---C---C---C---C---C---C---H
#     |   |   |   |   |   |   |
#     H   H   H   H   H   H   H
#
# 114.230 g/mol
#     H   H   H   H   H   H   H   H
#     |   |   |   |   |   |   |   |
# H---C---C---C---C---C---C---C---C---H
#     |   |   |   |   |   |   |   |
#     H   H   H   H   H   H   H   H
#
# 128.257 g/mol
#     H   H   H   H   H   H   H   H   H
#     |   |   |   |   |   |   |   |   |
# H---C---C---C---C---C---C---C---C---C---H
#     |   |   |   |   |   |   |   |   |
#     H   H   H   H   H   H   H   H   H

