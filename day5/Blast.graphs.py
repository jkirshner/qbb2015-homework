#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys 

Score = []
for line in open( sys.argv[1] ):
    fields = line.split()
    name = fields[1]
    rat_ident = float( fields[2] )
    rat_gap = float( fields[5] )
    score = float( fields[11] )
    evalue = float( fields[10] )
    Score.append(score)


plt.figure()
plt.hist(Score, 200)
plt.xlabel('Alignment')
plt.ylabel('Score')
plt.title('Alignment Scores')
plt.xlim(0, 200)
plt.savefig("score.png")
