#!/usr/bin/env python

import pandas as pd 
import matplotlib.pyplot as plt

#annotation = "/Users/cmdb/qbb2015/stringtie/t_data.ctab"
#df = pd.read_csv(annotation, comment ='#', header= None)

for file in [893, 894, 895, 896, 897, 899, 901, 903, 905, 906, 907, 908, 909, 911, 913, 915]:
    f= open ("/Users/cmdb/qbb2015/stringtie/SRR072" + str(file) + "/t_data.ctab")  
    for row in f:
        if "FBtr0331261" in row:
            print row, 