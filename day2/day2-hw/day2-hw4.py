#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd 

annotation = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

df = pd.read_table(annotation)
roi = df["FPKM"] > 0  
graph = df[roi]["FPKM"] 
print graph 

top = graph[0:3182]
middle = graph[3182:6365]
bottom = graph[6365:9549]

plt.figure()
plt.ylabel("FPKM") 
plt.xlabel("Top, Middle, Botom")
plt.boxplot([top, middle, bottom])
plt.title("FPKM Values")
plt.savefig("startsfpkm.png")



