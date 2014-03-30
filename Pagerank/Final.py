# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from numpy import *
import re
import sys

def powerMethodBase(A,x0,iter,theta):
    """ basic power method """
    for i in range(iter):
        x1 = x0
        x0 = dot(A,x0)
        x0 = x0/linalg.norm(x0,1)
        d = sum(abs(x1-x0))
        if d < theta:
            break
#    print i
    x0 = x0/sum(x0)
    return x0

def powerMethod(A,x0,m,iter,theta):
    """ power method modified to compute
     the maximal real eigenvector 
     of the matrix M built on top of the input matrix A """
    n = A.shape[1]
    delta = m*(array([1]*n,dtype='float64')/n) # array([1]*n is [1 1 ... 1] n times
    for i in range(iter):
        x1 = x0
        x0 = dot((1-m),dot(A,x0)) + delta
        d = sum(abs(x1-x0))
        print d
        if d < theta:
            break
#    print i
    x0 = x0/sum(x0)
    return x0

def maximalEigenvector(A):
    """ using the eig function to compute eigenvectors """
    n = A.shape[1]
    w,v = linalg.eig(A)
    return abs(real(v[:n,0])/linalg.norm(v[:n,0],1))

def linearEquations(A,m):
    """ solving linear equations 
     of the system (I-(1-m)*A)*x = m*s """
    n = A.shape[1]
    C = eye(n,n)-dot((1-m),A)
    b = m*(array([1]*n,dtype='float64')/n)
    x0 = linalg.solve(C,b)
    x0 = x0/sum(x0)
    return x0

def getTeleMatrix(A,m):
    """ return the matrix M
     of the web described by A """
    n = A.shape[1]
    S = ones((n,n))/n
    return (1-m)*A+m*S

# <codecell>

n = int(sys.argv[2])
m = zeros((n, n),dtype=float)
f = open(sys.argv[1], 'r')
dang = []
for line in f:
    line = line.strip('\r\n')
    p = re.compile(r'\(.*\)::')
    line = p.sub(':',line)
    (w,v) = line.split(':')
    list = v.split(',')
    if list[0] != '':
        m[list,w] = 1                                                                                              
    c = sum(m[:,w])
    if c == 0:
        c = 1
        dang.append(w)
    m[:,w] = m[:,w] / c
f.close()

# <codecell>

#m[dang,]=0
#for w in range(0,n):
#        c = sum(m[:,w])
#        if c == 0:
#            c = 1
#        m[:,w] = m[:,w] / c

# <codecell>

d=0.15
theta = 0.000000001
max_iter = 1000
M = getTeleMatrix(m,d)

x0 = [1]*n
x1 = powerMethod(m,x0,d,max_iter,theta)
#x2 = powerMethodBase(M,x0,max_iter,theta)
#x3 = maximalEigenvector(M)
#x4 = linearEquations(m,d)

# <codecell>

for i in x1:
    print i

