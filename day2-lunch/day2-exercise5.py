#!/usr/bin/env python

f = open( "/Users/cmdb/qbb2015/day1/mappedread.sam" )

chrom_counts = {"2L":0, "2R":0, "3L":0, "3R":0, "X":0, "4":0,}

for line in f:
    fields = line.split()
    chrom = fields[2]
    if "@" in line:
        pass 
    if chrom in chrom_counts:
        chrom_counts[chrom] += 1
        
print "2L", chrom_counts["2L"]
print "2R", chrom_counts["2R"]
print "3L", chrom_counts["3L"]
print "3R", chrom_counts["3R"]
print "X", chrom_counts["X"]
print "4", chrom_counts["4"]