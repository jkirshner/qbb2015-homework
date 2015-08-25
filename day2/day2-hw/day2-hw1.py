#!/usr/bin/env python

import pandas as pd 
import matplotlib.pyplot as plt

annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"
df = pd.read_table(annotation, comment ='#', header= None)
df.columns =["chromosome", "database", "type", "start", "end", "score", "strand", "frame", "attributes"] 

roi = df["attributes"].str.contains("Sxl")

plt.figure()
plt.ylabel("start position")
plt.xlabel("Row Number")
plt.plot(df[roi]["start"])
plt.title("Sxl")
plt.savefig("startsSxl.png")
