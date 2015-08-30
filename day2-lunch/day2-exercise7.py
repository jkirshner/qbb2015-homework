#!/usr/bin/env python

f = open( "/Users/cmdb/qbb2015/day1/mappedread.sam" )

line_count = 0

for line in f:
    fields=line.split()
    if "@" not in fields[0] and fields[2]=="2L":
       if 10000<=int(fields[3])<=20000:
           line_count+=1
            
print line_count