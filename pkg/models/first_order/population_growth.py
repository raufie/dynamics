class PopulationGrowth:
    # the logistic equation basically

    def rhs(self, x:float, k:float, r:float):
        # x (N (population N(t)))
        # k (carrying capacity)
        # r: rate of growth
        # N. = r*N*(1-N/K)
        N = x

        return r*N*(1-(N/k))