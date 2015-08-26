#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

df1 = pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")
df2 = pd.read_table("~/qbb2015/stringtie/SRR072905/t_data.ctab")

R = df1["FPKM"]
G = df2["FPKM"]
a= R[R>0]
b= G[G>0]

M = np.log2(R/G)
A = 0.5*np.log2(R*G)

plt.scatter(A, M)
plt.title("MA Plot")
plt.xlabel("M")
plt.ylabel("A")
plt.savefig("maplot.png")