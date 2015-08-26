#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pylab as P

df = pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")

values =[]

for sample in df["FPKM"]:
    if sample !=0:
        values.append(df["FPKM"])

logvalue = []


for num in values:
    logvalue.append(np.log(num[1])) 
    

plt.figure()
plt.hist(logvalue)
plt.title("FPKM Values in SRR072893") 
plt.xlabel("mRNA abundance (log(RPKM))")
plt.ylabel("abundance")
plt.savefig("fpkm.png")

