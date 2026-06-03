import numpy as np
class TumorGrowth:
    def rhs(self, x, a,b):
        N = x
        return -a*N*np.log(b*N)
    