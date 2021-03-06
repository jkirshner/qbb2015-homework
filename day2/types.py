#!/usr/bin/env python

# Integer
i = 10000

#Floating point / real number
f = 0.333

i_as_f = float (i)
f_as_1 = int (i)

# String
s = "A String" 

# Boolean
truthy = True
falsy = False

# Lists -- conventions only contains one type
l = [1,2,3,4,5]
l.append(7) 

# Tuple -- elements can have different element types  
t = (1, "foo", 5.0)

# Dictionary 
d1 = {"key1": "value1", "key2": "value2"}
d2 = dict (key1="value1", key2="value2")
d3 = dict( [("key1", "value1"), ("key2", "value2")])

for value in (i, f, s, truthy, l, t, d1, d2, d3):
    print value, type (value)