#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

f = open( filename )

for line in f:
    fields = line.split()
    if "tRNA" in fields[9]:
        print line, 
    # comma gets rid of the extra line 
    # a for loop for a file always reads line by line 
