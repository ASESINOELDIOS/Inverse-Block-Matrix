from matrixtest import matrixtest
from main_algorithm import inv_unit_diagon_blocks
from numba import set_num_threads
from numpy.linalg import inv
#################
#m,n are for the dimentions of A matrix
# k is for the number of CPU threads to use
# if k=1 it executes the algorithm serially
n=5
m=5
k=1
def testfunc(n,m,k):
    #creation of A matrix 
    A=matrixtest(n,m)
    #setting the number of threads 
    set_num_threads(k)
    #run the program to calculate the inverse algorithm 
    #print(inv_unit_diagon_blocks(A,m))
    inv_A,S=inv_unit_diagon_blocks(A,m)
    print("The matrix A is\n")
    print(np.array_str(A, precision=2, suppress_small=True))
    print("\nThe matrix S is\n")
    print(np.array_str(S, precision=2, suppress_small=True))
    print("\nThe inverse of matrix A is\n")
    print(np.array_str(inv_A, precision=2, suppress_small=True))
    print("\nThe inverse of matrix A, using a standard method (here LU), is\n")
    print(np.array_str(inv(A), precision=2, suppress_small=True))

if __name__ == '__main__':
    testfunc(n,m,k)
