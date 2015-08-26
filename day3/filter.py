#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

f = open( filename )

"""for line in f:
    fields = line.split()
    if "tRNA" in fields[9]:
        print line, 
    # comma gets rid of the extra line 
    # a for loop for a file always reads line by line"""
    

    
'''for line_count, data in enumerate(f):
    if line_count <=10:
        pass
    elif line_count <= 15:
        print data,
    else:
        break '''
        
# enumerate adds +1 to each 


import sys
#print sys.argv
#filename = sys.argv[1]

#f= open(filename)

f = sys.stdin
 
name_counts = {}
        
for line_count, data in enumerate(f):
    fields = data.split()
    gene_name = fields[9]
    if gene_name not in name_counts:
        name_counts [gene_name] = 1
    else:
        name_counts [gene_name] += 1
# Iterate key, value pairs from the name count dictionary         
for key, value in name_counts.iteritems():
    print key, value
                       
          
