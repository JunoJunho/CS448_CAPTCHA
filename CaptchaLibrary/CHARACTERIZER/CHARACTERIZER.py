from numpy import *
from predict import *

from CaptchaLibrary.PREPROCESSOR import *


def CHARACTERIZER(Theta1, Theta2, inFile):
    # PREPROCESSOR crawl a captcha pic and save it in a csv format => 'X.txt'
    PREPROCESSOR(inFile)

    ## =========== Part 2: Loading X and Parameters =============
    X = loadtxt('./CaptchaLibrary/CHARACTERIZER/X.txt')
    m = X.shape[0]

    #print('Saved Neural Network Parameters are all loaded...\n')
    ## ================= Part 3: Implement Predict =================
    predSTR = 'BCEFGHIJKLMNPRSTUVWXYZ'

    guessSTR = ''
    for i in range(m):
        pred = predict(Theta1, Theta2, X[i, :][newaxis])
        guessSTR = guessSTR + predSTR[pred]
    return guessSTR
