from matrixtest import *
from inverse_algorithm import *
import timeit
from numba import set_num_threads
#################
#m,n are for the dimentions of A matrix
# k is for the number of CPU threads to use
# if k=1 it executes the algorithm serially
def testfunc(n,m,k):
    #creation of A matrix 
    A=matrixtest(n,m)
    #setting the number of threads 
    set_num_threads(k)
    #run the program to calculate the inverse algorithm 
    inv_A=inv_unit_diagon_blocks(A,m)
    return inv_A 

if __name__ == '__main__':
    testfunc(n,m,k)
