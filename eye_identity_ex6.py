# The eye tool returns a 2-D array with 1's as the diagonal and 0's elsewhere. The diagonal can be main, upper or lower depending on the optional parameter k. A positive 
# k is for the upper diagonal, a negative k is for the lower, and a 0k (default) is for the main diagonal.

import numpy as np

n,m = list(map(int, input().split( )))
np.set_printoptions(legacy='1.13')
print(np.eye(n,m,k=0)) 
