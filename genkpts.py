import os
import numpy as np
from numpy.linalg import *
# x->-0.1 to 0.1
# y->0
# z->0.8, 1
kpts = []
for i in range(-20, 21, 1):
    kpts.append([round(0.005 * i, 3), 0.0, 0.8])
    kpts.append([round(0.005 * i, 3), 0.0, 1.0])
kpts = np.array(kpts)
np.savetxt('k.dat', kpts, fmt='%.3f')
