import numpy as np
from scipy import *
import re

d = 0.85
m = np.zeros((1658, 1658),dtype=float)
n = m.shape[0]
f = open('result.txt', 'r')
for line in f:
	line = line.strip('\r\n')
	p = re.compile(r'\(.*\)::')
	line = p.sub(':',line)
	(w,v) = line.split(':')
	list = v.split(',')
	if len(list) > 1:
		m[w,list] = 1
	c = sum(m[w,])
	if c == 0:
		c = 1
	m[w,] = (1 - d) / n + d * m[w,] / c
f.close()

