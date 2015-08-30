#!/usr/bin/env python

f = open( "/Users/cmdb/qbb2015/day1/mappedread.sam" )

line_count = 0 
mapq_count = 0

for line in f:
    fields = line.split()
    if "@" in line:
        pass 
    else:
        mapq = fields[4]
        mapqint = int(mapq)
        line_count += 1
        mapq_count += mapqint
    
        
average_mapq = mapq_count / line_count

print average_mapq