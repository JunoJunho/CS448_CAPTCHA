from numpy import *
from sigmoid import sigmoid
import pdb


def predict(Theta1, Theta2, X):
    # pdb.set_trace()
    # Useful values
    m = X.shape[0]
    num_labels = Theta2.shape[0]

    a1 = X.T
    a1 = vstack((ones((1, a1.shape[1])), a1))

    z2 = dot(Theta1, a1)
    a2 = sigmoid(z2)
    a2 = vstack((ones((1, a2.shape[1])), a2))

    z3 = dot(Theta2, a2)
    a3 = sigmoid(z3)
    h_matrix = a3

    val, idx = h_matrix.max(0), h_matrix.argmax(0)

    return idx.T
