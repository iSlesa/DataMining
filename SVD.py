import math
import numpy as np

#Function for SVD calculation
def svd(x):
    xt = x.transpose()
    xXxt = np.dot(x, xt)
    xtXx = np.dot(xt,x)
    evalues, evector = np.linalg.eig(xtXx)
    temp1, temp2 = np.linalg.eig(xXxt)
    V = []
    V.append(evector)
    temp = [int(i) for i in evalues]
    roots = []
    for j in temp1:
        if int(j) in temp:
            roots.append(np.sqrt(j))
    E = []
    for i in range(x.shape[0]):
        tmp = []
        for j in range(x.shape[1]):
            if i != j:
                tmp.append(0)
            else:
                try:
                    tmp.append(roots[i])
                except:
                    tmp.append(1)
        E.append(tmp)
    e = np.matrix(E)
    U = temp2
    print ('Input matrix = ')
    print (x)
    print ('x = U* E* V where:')
    print('U =')
    print(U)
    print('E =')
    print (e)
    print('V =')
    print (V)

x = np.matrix([[2, 2, 4, 0], [5, 8, 1, 2], [7, 0, 1, 4]])
svd(x) 
