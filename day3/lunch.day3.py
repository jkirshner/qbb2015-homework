#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")
df2 =pd.read_table("~/qbb2015/stringtie/SRR072915/t_data.ctab")

metadata = pd.read_csv("~/qbb2015/rawdata/samples.csv")
replicates = pd.read_csv("/Users/cmdb/qbb2015/rawdata/replicates.csv") 

Sxlf =[]
Sxlm =[]
repf =[]
repm =[]

for sample in metadata[metadata["sex"] == "female"]["sample"]:
    df = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")
    roi = df["t_name"].str.contains("FBtr0331261")
    df[roi]["FPKM"].values
    Sxlf.append(df[roi]["FPKM"].values)

for sample in metadata[metadata["sex"] == "male"]["sample"]:
    df = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")
    roi = df["t_name"].str.contains("FBtr0331261")
    df[roi]["FPKM"].values
    Sxlm.append(df[roi]["FPKM"].values)
    
for sample in replicates[replicates["sex"] == "female"]["sample"]:
    df = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")
    roi = df["t_name"].str.contains("FBtr0331261")
    df[roi]["FPKM"].values
    repf.append(df[roi]["FPKM"].values)
    
for sample in replicates[replicates["sex"] == "male"]["sample"]:
    df = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")
    roi = df["t_name"].str.contains("FBtr0331261")
    df[roi]["FPKM"].values
    repm.append(df[roi]["FPKM"].values)
    


plt.figure()
plt.plot(Sxlf, 'r', label = "female")
plt.plot(Sxlm, label = "male")
plt.plot((4,5,6,7), repf, 'ro')
plt.plot ((4,5,6,7), repm, 'o')
plt.title("Sxl")
plt.xlabel("Developmental Stage")
plt.xticks(range(8), ('10', '11', '12', '13', '14A', '14B', '14C', '14D'), rotation=88 )
plt.ylabel("mRNA abundance (RPKM)")
plt.legend(bbox_to_anchor=(.05, 1), loc=2, borderaxespad=0.) 
plt.savefig("comparison.png")