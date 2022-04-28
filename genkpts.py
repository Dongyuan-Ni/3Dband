import os
import numpy as np
from numpy.linalg import *
# x->-0.2 to 0.2
# y->0
# z->-0.2 to 0.2
kpts = []
a = np.linspace(-0.2, 0.2, 51)
c = np.linspace(-0.2, 0.2, 51)
for i in a:
    for j in c:
        kpts.append([i, 0.0, j])
kpts = np.array(kpts)
np.savetxt('k.dat', kpts, fmt='%.3f')

