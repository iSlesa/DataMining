import numpy
import math

def mean(x):
    return sum(x)/len(x) 

def cov(x,y):
    n = len(x)
    sum = 0
    for i in range(n):
        sum +=  (x[i]-mean(x))*(y[i]-mean(y))
    return sum/n-1

def covmat(x,y):
    matrix = [[cov(x,x), cov(x,y)],[cov(y,x), cov(y,y)]]
    return matrix
x = [1,2,3,4,5]
y = [1,2,3,6,8]
print cov(x,y)
print covmat(x,y)
