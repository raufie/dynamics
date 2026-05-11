import numpy as np
class CapacitorModel:
    def __init__(self, C, V0, R, k=1):
        """
        C = capacitance
        V0 = voltage source
        R = resistance
        k = nonlinearity parameter (k=1 for linear capacitor)
        """
        self.C = C
        self.V0 = V0
        self.R = R
        self.k=k
    
    
    def charge_model_rhs(self, Qt):
        arg = (self.V0/self.R) - (Qt/(self.R*self.C))
        if arg == 0:
            return 0.0
        return np.sign(arg) * (np.abs(arg) ** (1/self.k))
    
    def discharge_model_rhs(self, Qt):
        if Qt <= 0:
            return 0.0  # Fully discharged
        arg = Qt/(self.R*self.C)
        return - (arg ** (1/self.k))