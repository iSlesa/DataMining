import numpy
import math
import matplotlib.pyplot as plt

def mean(x):
    return sum(x)/len(x) 

def mag(v):
    n = len(v)
    s = 0
    for a in v:
        s += a*a
    return math.sqrt(s)

def cov(x,y):
    n = len(x)
    s = 0
    for i in range(n):
        s +=  (x[i]-mean(x))*(y[i]-mean(y))
    return s/(n-1)

def covmat(x,y):
    matrix = [[cov(x,x), cov(x,y)],[cov(y,x), cov(y,y)]]
    return matrix

def eigen(mat):
    n = len(mat)
    m = [0] * n
    m[0] = 1
    for i in range(100):
        temp = [0] *n
        for s in range(n):
            for r in range(n):
                temp[s] += mat[s][r] * m[r]
        div = mag(temp)
        for j in range(n):
            m[j] = temp[j]/div
    return m, div

def project(x,y,v):
    n = len(v)
    l = len(x)
    res1 = []
    res2 = []
    for i in range(l):
        d = x[i]*v[0] + y[i]*v[1]
        res1.append(d*v[0])
        res2.append(d*v[1])
    return res1, res2

def plot(x,y):
    plt.scatter(x,y,color = 'red')
    plt.plot(x,y,color = 'black')
    plt.show()
    #plt.close()

x = [1,2,3,4,5,6,7,8,9,10]
y = [1,2,3,6,8,12,32,12,12,2]

covmatrix = covmat(x,y)
eigenvec , eigenval = eigen(covmatrix)
plot(x,y)
proj1, proj2 = project(x,y,eigenvec)
plot(proj1,proj2)

#plt.show()
#plt.close()
