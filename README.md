#  Parallel Block Matrix Inversion Algorithm
![GPLv2][]

[GPLv2]: https://img.shields.io/badge/license-GPLv2-lightgrey.svg

AUTHOR: D. Lazaridis (lazdimspy@csd.auth.gr)<br>
Initial version: Nov. 2023<br>
Licence : [GPLv2](https://github.com/ASESINOELDIOS/Inverse-Block-Matrix/blob/main/LICENSE)<br>
REFERENCES:  https://www.python.org/, https://numba.pydata.org/<br>
Description: The algorithm is analyzed in the following paper <br> ``Parallel Inversion of Matrices with Simultaneously Diagonalizable Blocks, by D. Lazaridis, K.A.Draziotis and N.L. Tsitsas.``<br>
The accompanying code has been designed to facilitate experimental investigations into the algorithm proposed in this paper.

## Requirements
The code is written in Python 3. The packages needed are numba and numpy (for install provide ``$pip install numba`` for a linux based OS).<br>
For more optimal settings is recommended to use the anaconda distribution for the prerequisites packages.
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

This function calculates the inverse of a $m\times m$ block matrix $A$, where each block is $n\times n$ matrix.<br>
We assume that each block is simultaneously diagonalizable by the same matrix $S.$<br>
The function ``inv_unit_diagon_blocks`` has as input, the block matrix $A$ and the dimensions of each block m.<br>
The output of the function provides the inverse of the block matrix $A$ using parallel execution in multiple threads.

The algorithm uses automated parallelization with the help of numba package.

