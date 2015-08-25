#!/usr/bin/env python

import pandas as pd

annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df = pd.read_table(annotation, comment ='#', header= None)

#print df
#print df.head()
#print df.describe()
#print df.info()
#print df[1:5]
    #prints 1,2,3,4
# \n indicated you want a new line 

# shows rows 10 through 15 (1-based, includive)
#print df [9:15]

#show rows 20 through 25
#print df [19:25]

#print df.info()
df.columns =["chromosome", "database", "type", "start", "end", "score", "strand", "frame", "attributes"]
#print df.info()
#print df.sort(columns="type", ascending = False)

#print df["chromosome"]

# Subset the "chromosome", "start", "end" columns
#print df[["chromosome", "start", "end"]]

#print df["start"][9:15]

#print df.shape
df2 = df["start"]
#print df2.shape

df2.to_csv("startColumn.txt", sep='\t', index=False)

roi = df["start"] < 10
print df[roi]