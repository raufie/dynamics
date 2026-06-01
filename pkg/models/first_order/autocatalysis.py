class Autocatalysis:

    def rhs(self, x, k_a=1, k_b=1, a=1):
        return k_a*a*x - k_b*x**2