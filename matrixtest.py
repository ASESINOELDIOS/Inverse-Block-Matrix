import numpy as np
from numpy.linalg import inv
def matrixtest(n,m):
    typenum=np.complex64
    S=np.empty((n,n),dtype=typenum)
    S=np.random.random((n,n))
    A=np.empty((m*m,n,n),dtype=typenum)
    inv_s=inv(S)
    inv_s=inv_s.astype(typenum)
    for i in range (m*m):
        x=np.random.random(n)
        A[i]=S@np.diag(x)@inv_s
    A=np.concatenate(A.reshape(m,m,n,n).swapaxes(1, 2).reshape(-1, n*m, n*m))
    return A
