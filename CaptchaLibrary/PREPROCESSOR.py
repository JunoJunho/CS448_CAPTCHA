import os
import time
from PIL import Image
import sys
from numpy import *

sys.path.append('./CaptchaLibrary')
sys.path.append('./CaptchaLibrary/CHARACTERIZER')

from CROPPER import CROPPER as CR
from DECOLORIZER import DECOLORIZER as DC
from SIZEUNIFIER import SIZEUNIFIER as SU
from MATRIXMAKER import MATRIXMAKER as MM


def PREPROCESSOR(inFile):
    cw_im = Image.open(inFile)

    # PART1: CHOP A PIC INTO 5s
    #input: one image object
    #output: a list of five image objects
    cr_im_List = CR(cw_im)
    if len(cr_im_List) != 5:
        print '#FAILED ON GETTING FIVE .png FILES'

    #PART2: DECOLORIZE
    #input: a list of five image objects
    #output: a list of five image objects
    dc_im_List = DC(cr_im_List)

    #PART3: SIZEUNIFIER
    #input: a list of five image objects, new width, new height
    #output: a list of five image objects
    su_im_List = SU(dc_im_List, 32, 33)

    #PART4: MATRIXMAKER
    #input: a list of five image objects
    #output: a matrix of X in memory (no y for the answer. THIS IS NOT A DRILL)
    X = MM(su_im_List)

    f = open('./CaptchaLibrary/CHARACTERIZER/X.txt', 'w')
    f.write(X)
    f.close()

