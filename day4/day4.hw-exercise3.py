#!/usr/bin/env python
from __future__ import division
import matplotlib.pyplot as plt
from matplotlib_venn import venn3
import chrombitscorrect
import sys

    
arr = chrombitscorrect.ChromosomeLocationBitArrays( fname=sys.argv[1] )

ctcf = arr.copy()
beaf = arr.copy()
SuHW = arr.copy()

ctcf.set_bits_from_file( sys.argv[2] )
beaf.set_bits_from_file( sys.argv[3] )
SuHW.set_bits_from_file( sys.argv[4] )

union = ctcf.union( beaf.union(SuHW) )


#arrays = arr
#arrays2 = arr
#arrays3 = arr
#arrays.set_bits_from_file(sys.argv[2])
#arrays2.set_bits_from_file(sys.argv[3])
#arrays3.set_bits_from_file(sys.argv[4])
arrays = ctcf
arrays2 = beaf
arrays3 = SuHW

count_Abc = 0 
count_aBc = 0 
count_abC = 0 
count_ABc = 0 
count_AbC = 0 
count_aBC = 0 
count_ABC = 0 
total = 0

for filename in sys.argv[2:]:
    for line in open( filename ):
        fields = line.split()
        chrom = fields[0]
        start = int( fields[1] )
        end = int( fields[2] )
        sl = arrays.arrays[chrom][start:end]
        sl2 = arrays2.arrays[chrom][start:end]
        sl3 = arrays3.arrays[chrom][start:end]
        if sl.any() and not sl2.any() and not sl3.any():
            count_Abc += 1 
        elif sl2.any() and not sl.any() and not sl3.any():
            count_aBc += 1 
        elif sl3.any() and not sl.any() and not sl2.any():
            count_abC += 1 
        elif sl.any() and sl2.any() and not sl3.any():
            count_ABc += 1
        elif sl.any() and sl3.any() and not sl2.any(): 
            count_AbC += 1 
        elif sl2.any() and sl3.any() and not sl.any():
            count_aBC += 1 
        else: 
            count_ABC += 1
        total += 1



plt.figure()
venn3(subsets=(count_Abc, count_aBc, count_abC, count_ABc, count_AbC, count_aBC, count_ABC), set_labels = ('CTCF', 'BEAF', 'SuHW',))

plt.savefig("venn.diagram2.png")

