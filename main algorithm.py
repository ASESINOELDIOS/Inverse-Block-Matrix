from numpy import diag,empty,ascontiguousarray,complex64
from numpy.linalg import inv,eig
from numba import njit, prange,threading_layer,config
config.THREADING_LAYER = 'omp'
@njit(parallel=True)
def inv_unit_diagon_blocks(A,m):
    M=m*m
    typenum=complex64
    A=A.astype(typenum)
    n=int(len(A)/m)
#calculating the eigenvalues of the first block 
    eigenvalues, S = eig(A[0:n,0:n].astype(typenum))
    eigenvalues.astype(typenum)
#calculating the inverse of S 
    S=S.astype(typenum)
    inv_S=inv(S)
    inv_S=inv_S.astype(typenum)
#computation of L blocks
    Lambda=empty((M,n),dtype=typenum)
    k=0
    for i in prange(m):
        if i!=0:
            k=m*i
        for j in range(m):
            if i==0 and j==0:
                Lambda[j+k]=eigenvalues.astype(typenum)
            else:
                Lambda[j+k]=((ascontiguousarray(A[(i)*n:(i+1)*n,(j)*n:(j+1)*n])@ascontiguousarray(S))/ascontiguousarray(S))[0]
    inv_Lambda_p=empty((n,m,m),dtype=typenum)
#computation and inversion of L' blocks 
    for i in prange(n):
        inv_Lambda_p[i]=inv(ascontiguousarray(Lambda[0:M,i]).reshape(m,m)).astype(typenum)
#computation of the inverse L blocks 
    inv_Lambda=empty((M,n,n),dtype=typenum)
    k=0
    for i in prange(m):
        if i!=0:
            k=m*i
        for j in range(m):
            inv_Lambda[j+k]=diag(ascontiguousarray(inv_Lambda_p[0:n,i,j])).astype(typenum)
#computation of inverse A block matrix
    inv_A=empty((n*m,n*m),dtype=typenum)
    k=0
    for i in prange(m):
        if i!=0:
            k=m*i
        for j in range(m):
            inv_A[(i)*n:(i+1)*n,(j)*n:(j+1)*n]=ascontiguousarray(S)@inv_Lambda[j+k]@ascontiguousarray(inv_S)
    return inv_A

