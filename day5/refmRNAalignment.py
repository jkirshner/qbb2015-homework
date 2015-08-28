#!/usr/bin/env python

import sys

index = []

for line in open( sys.argv[1] ):
    fields = line.split()
    name = fields[1]
    rat_ident = float( fields[2] )
    rat_gap = float( fields[5] )
    print "Sequence name: %s, Ratio of identities: %f, Ratio of gaps: %f," % (name, rat_ident, rat_gap)
    