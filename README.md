# 3Dband
Plot 3Dband

1.Run genkpts.py to generate k.dat for specific plane in BZ.

2.Run addzero.py to adding 0 weight for each k-point. The output file is kout.dat

3.Combine IBZKPT and kout.dat to obtain KPOINTS.

4.Run vasp.

5.Run 3Dband.py to get 3dkpoints.dat.

6.Plot it.

7.Using 3dband_better.py to make the 3Dband better-looking.
