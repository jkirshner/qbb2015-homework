#!/usr/bin/env python

"""
Count intersection of two BED files
"""
from __future__ import division

import numpy
import sys

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
set_bits_from_file( arrays, sys.argv[2] )
  
#for key, value in arrays.iteritems():
    #print key, type( value ), value.shape, numpy.sum( value )
    
total = 0
any_overlap = 0 
all_overlap = 0
half_overlap = 0

for line in open( sys.argv[3] ):
    fields = line.split()
    chrom = fields[0]
    start = int( fields[1] )
    end = int( fields[2] )
    # Get Slice
    sl = arrays[chrom][start:end]
    # Aggregate
    total += 1
    any_overlap += sl.any() 
    all_overlap += sl.all()
    # 50% overlap
    half_overlap += (numpy.sum(sl)) / len(sl) > 0.5
print "Total: %d, Any overlap: %d, All overlap: %d, Half overlap: %d" % (total, any_overlap, all_overlap, half_overlap)
    
    
    



