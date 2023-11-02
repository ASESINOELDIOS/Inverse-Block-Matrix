#  Parallel Block Matrix Inversion Algorithm
![GPLv2][]

[GPLv2]: https://img.shields.io/badge/license-GPLv2-lightgrey.svg

AUTHOR: D. Lazaridis (lazdimspy@csd.auth.gr)

2023: initial version

Licence : [GPLv2](https://github.com/ASESINOELDIOS/Inverse-Block-Matrix/blob/main/LICENSE)

REFERENCES:  https://www.python.org/, https://numba.pydata.org/

Parallel implementation for the Inverse of a block matrix. 

## Requirements
The code is written in Python 3. The packages needed are numba and numpy.
For most optimal settings is recommended to use the anaconda distribution for the prerequisites packages.
### Installation of packages needed

For the numpy
```
conda install -c anaconda numpy
```

For the numba
```
conda install -c numba numba
```

Ιn case it doesn't work properly, you might need to update all packages
```
conda update --all
```

## Usage info

This function calculates the inverse of a block matrix A, in which, every block is simultaneously diagonalizable by the same matrix S.

The function "inv_unit_diagon_blocks" has as imput, the block matrix A and the dimentions of each block m.

As an output value it gives the inverse of the block matrix A using parallel execution in multiple threads.

The algorithm uses automated parallelization with the help of numba package.

