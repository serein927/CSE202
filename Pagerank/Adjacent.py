# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from numpy import *
import re
import sys
# <codecell>

mx = {}
mx_col = {}
n = int(sys.argv[2])

f = open(sys.argv[1], 'r')
dang = []
for line in f:
    line = line.strip('\r\n')
    p = re.compile(r'\(.*\)::')
    line = p.sub(':',line)
    (w,v) = line.split(':')
    if v=='':
        continue
    l = v.split(',')
    for i in l:
        if mx.has_key(int(i)):
            mx[int(i)].append(int(w))
        else:
            mx[int(i)] = [int(w)]
    mx_col[int(w)] = len(l)
f.close()

# <codecell>

theta = 0.000000001
r = array([1]*n,dtype='float64')
max_iter = 1000
for i in range(max_iter):
    r1 = array([0]*n,dtype='float64')
    for j in range(n):
        if mx.has_key(j):  
            for k in mx[j]:
                r1[j] += r[k]/mx_col[k] 
    r1 = 0.85 * r1 + 0.15 / n
    delta = sum(abs(r1-r))
    #print delta
    r = r1
    print i,delta
    if delta < theta:
            break
r = r/sum(r)

# <codecell>

#for i in r:
#    print i

# <codecell>


