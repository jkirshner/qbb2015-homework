#!/usr/bin/env python
from __future__ import division
import pandas as pd
import matplotlib.pyplot as plt
import numpy
import sys
from matplotlib_venn import venn3, venn3_circles 

def arrays_from_len_file( fname ):
    arrays = {}
    for line in open( fname ):
        fields = line.split()
        name = fields[0]
        size = int( fields[1] ) #int converts to integer
        arrays[name] = numpy.zeros( size, dtype=bool ) # 0 = false in boolean
    return arrays
    
def set_bits_from_file( arrays, fname ):
    for line in open( fname ):
        fields = line.split()
        #Parse fields
        chrom = fields[0]
        start = int( fields[1] )
        end = int( fields[2] )
        arrays[ chrom ][start : end] = 1
        
        
arrays = arrays_from_len_file( sys.argv[1] )
arrays2 = arrays_from_len_file( sys.argv[1] )
arrays3 = arrays_from_len_file( sys.argv[1] )
set_bits_from_file( arrays, sys.argv[2] )
set_bits_from_file( arrays2, sys.argv[3] )
set_bits_from_file( arrays3, sys.argv[4] )

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
        sl = arrays[chrom][start:end]
        sl2 = arrays2[chrom][start:end]
        sl3 = arrays3[chrom][start:end]
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
 
print "Only A: %d, Only B %d, Only C %d, A and B %d, A and C %d, B and C %d, A and B and C %d" % (count_Abc, count_aBc, count_abC, count_ABc, count_AbC, count_aBC, count_ABC )
print total, count_Abc+count_ABC

plt.figure()
venn3(subsets=(count_Abc, count_aBc, count_abC, count_ABc, count_AbC, count_aBC, count_ABC), set_labels = ('CTCF', 'BEAF', 'SuHW',))

plt.savefig("venn.png")


