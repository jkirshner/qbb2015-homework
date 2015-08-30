#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys 

Score = []
eVal = []
for line in open( sys.argv[1] ):
    fields = line.split()
    name = fields[1]
    rat_ident = float( fields[2] )
    rat_gap = float( fields[5] )
    score = float( fields[11] )
    evalue = float( fields[10] )
    Score.append(score)
    eVal.append(evalue)



# Scatterplot comparison 
plt.figure()
plt.scatter(eVal, Score)
plt.xlabel('Score')
plt.ylabel('evalue')
plt.title('Alignment Scores')
plt.savefig("eval.score.compare.png")