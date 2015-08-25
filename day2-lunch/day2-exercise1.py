#!/usr/bin/env python

f = open( "/Users/cmdb/qbb2015/day1/mappedread.sam" )
   
line_count = 0

for line in (f):
    if "@" in line:
        pass 
    else:
        line_count += 1 
print line_count
