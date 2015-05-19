from numpy import *


def reshape_octave(a, x, y):
    return a.reshape(y, x).transpose()


def INITIALIZATION(nn_params_file):
    input_layer_size = 1056  # 32x33 Input Images of Digits
    hidden_layer_size = 500  # 25 hidden units
    num_labels = 22  # 22 labels, from 1 to 22

    nn_params = loadtxt(nn_params_file)
    theta1 = reshape_octave(nn_params[0: hidden_layer_size * (input_layer_size + 1)], hidden_layer_size,
                            (input_layer_size + 1))
    theta2 = reshape_octave(nn_params[hidden_layer_size * (input_layer_size + 1):], num_labels, (hidden_layer_size + 1))
    return theta1, theta2
