#!/usr/bin/env python

f = open( "/Users/cmdb/qbb2015/day1/mappedread.sam" )

line_count = 0 

for line in f:
    fields = line.split()
    chrom = fields[2]
    if "@" in line:
        pass 
    else:
        if line_count <10:
            line_count +=1
            print fields[2]