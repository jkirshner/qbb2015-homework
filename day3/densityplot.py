#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde 


    
df = pd.read_table("/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab")
data = []

for number in df["FPKM"]:
    if number >0:
        data.append(number)
    
log=np.log(data)


density = gaussian_kde(log)
xs = np.linspace(-10,20,200)
density.covariance_factor = lambda : .25
density._compute_covariance()
plt.plot(xs,density(xs))
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('FPKM values in SRR072893')
plt.savefig("gaussiancurve.png")