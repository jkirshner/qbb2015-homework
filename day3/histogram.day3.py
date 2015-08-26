#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_table("/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab")
roi = df['FPKM'] >0

plot=df[roi]['FPKM']
log=np.log(plot)

plt.figure()
plt.hist(log.values)
plt.xlabel('log of FPKM')
plt.ylabel('Frequency')
plt.title('Frequency of FPKM')
plt.savefig("fpkm.png")



