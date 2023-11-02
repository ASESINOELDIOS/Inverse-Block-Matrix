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
    print(A)
    print("\nThe matrix S is\n")
    print(S)
    print("\nThe inverse of matrix A is\n")
    print(inv_A)
    print("\nThe inverse of matrix A with LU is\n")
    print(inv(A))

if __name__ == '__main__':
    testfunc(n,m,k)
