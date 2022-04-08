#########################################################################
# 通过看CB-VB的值确定nodal line，并且nodal line处价带为局域最高点
# nodal line以内的点价带与导带交换，使得画出来的nodal line好看
#########################################################################
import numpy as np
from numpy.linalg import *

with open('3dband.dat', 'r') as f:
    data = f.readlines()
for i in range(len(data)):
    data[i] = [float(j) for j in data[i].split()]
data = np.array(data)

for i in range(41):
    # 固定x
    max_valence_band = -100
    VB = []
    # 每个x有61个y值
    # print()
    # print()
    point = []
    for j in range(61):
        if data[61 * i + j - 1][2] < data[61 * i + j][2] and data[61 * i + j][2] > data[61 * i + j + 1][2]\
                and abs(data[61 * i + j][3] - data[61 * i + j][2]) < 5e-2:
            point.append(j)
    for j in range(61):
        if len(point) == 2:
            if point[0] < j < point[1]:
                tmp = data[61 * i + j][2].copy()
                data[61 * i + j][2] = data[61 * i + j][3].copy()
                data[61 * i + j][3] = tmp.copy()

with open('3dband_fine.dat', 'w') as f:
    for i in range(len(data)):
        f.write(' '.join([str(t) for t in data[i]])+'\n')
