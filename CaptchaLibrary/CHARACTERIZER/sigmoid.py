from numpy import exp
def sigmoid(z):
    try:
        g = 1.0 / (1.0 + exp(-z))
        return g
    except RuntimeWarning, e:
        return g
        pass
