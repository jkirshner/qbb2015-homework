#!/usr/bin/env python

import pandas as pd 
import matplotlib.pyplot as plt

annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"
df = pd.read_table(annotation, comment ='#', header= None)
df.columns =["chromosome", "database", "type", "start", "end", "score", "strand", "frame", "attributes"] 

roi1 = df["attributes"].str.contains("Sxl")
roi2 = df["type"].str.contains("transcript")

plt.figure()
plt.ylabel("start position")
plt.xlabel("Row Number")
plt.plot(df[roi1][roi2]["start"])
plt.title("Sxl")
plt.savefig("startsSxl2.png")