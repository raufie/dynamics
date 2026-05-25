class TerminalVelocity:
    def __init__(self):
        pass

    def rhs(self, vt, m, g, k):
        """
        vt = terminal velocity
        m = mass
        g = gravitational acceleration
        k = drag coefficient
        """
        return (m * g - k * vt**2) / m