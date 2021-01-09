"""algorithm sourced from: https://kel.bz/post/lll/"""

import numpy as np

u = np.array((87502093, 123094980))
v = np.array((846835985, 9834798552))

while True:
    if np.linalg.norm(v) < np.linalg.norm(u):
        u, v = v, u
    m = np.dot(u, v) // np.dot(u, u)
    if m == 0:
        print(np.dot(u, v))
        break
    v = v - m * u
