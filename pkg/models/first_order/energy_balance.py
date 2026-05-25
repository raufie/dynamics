# model for predicting temperature of the earth's surface based on energy balance (Ein - Eout)

class EnergyBalanceModel:
    def __init__(self, C_earth: float, eps: float, alpha: float, Q: float, sigma:float):
        self.C_earth = C_earth
        self.eps = eps
        self.alpha = alpha
        self.Q = Q

        self.sigma = sigma

    def rhs(self, Tt):
        Ein = ((1-self.alpha)*self.Q)
        Eout = self.eps*self.sigma*(Tt**4)

        return ((Ein-Eout)/self.C_earth)