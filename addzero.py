#!/usr/bin/env python
import os
import numpy as np

with open('k.dat', 'r') as f:
	data = f.readlines()
for i in range(len(data)):
	data[i] = data[i].strip('\n')
	data[i] += '   0.0\n'
with open('kout.dat', 'w') as f:
	f.writelines(data)
