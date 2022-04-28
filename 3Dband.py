#!/usr/bin/env python
import os
import numpy as np

Ef = float(os.popen('grep E-fermi OUTCAR').read().split()[2])

os.chdir('kp')
with open('IBZKPT', 'r') as f:
	f.readline()
	nkpts_scf = int(f.readline())
os.chdir('..')

axis = input("Which axis is confined:(x, y, z)")

data = []

with open('EIGENVAL', 'r') as f:
	for i in range(5):
		f.readline()
	number = [int(i) for i in f.readline().split()]
	nelectrons = number[0]
	noccupancy = int(nelectrons / 2)
	nkpts = number[1]
	nbnds = number[2]
	f.readline()
	for i in range(nkpts_scf):
		for j in range(nbnds+2):
			f.readline()
	for i in range(nkpts - nkpts_scf):
		if axis == 'x':
			kpoint_coord = '    '.join(f.readline().split()[1:3])
		if axis == 'y':
			kpoint_coord_y = f.readline()
			kpoint_coord = kpoint_coord_y.split()[0] + '    ' + kpoint_coord_y.split()[2]
		if axis == 'z':
                        kpoint_coord = '    '.join(f.readline().split()[0:2])
		for j in range(noccupancy - 1):
			f.readline()
		Evb1 = str(float(f.readline().split()[1]) - Ef)
		Ecb1 = str(float(f.readline().split()[1]) - Ef)
		
		data.append(kpoint_coord + '    ' + Evb1 + '    ' + Ecb1 + '\n')	

		for j in range(nbnds - noccupancy - 1):
			f.readline()
		if i != nkpts - nkpts_scf - 1:
			f.readline()
		else:
			pass

with open('3dkpoints.dat', 'w') as f:
	f.writelines(data)

