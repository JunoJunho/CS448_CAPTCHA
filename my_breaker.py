from CaptchaLibrary.CHARACTERIZER.INITIALIZATION import INITIALIZATION
from CaptchaLibrary.CHARACTERIZER.CHARACTERIZER import CHARACTERIZER as Guesser
import os

if __name__ == '__main__':
    dir = os.path.dirname(__file__)
    init_theta1, init_theta2 = INITIALIZATION('D:\\003. Project\CS448\CAPTCHA\CaptchaLibrary\\nn_params.txt')
    guess_string = Guesser(init_theta1, init_theta2, 'D:\\003. Project\CS448\CAPTCHA\CaptchaLibrary\\Captcha1.jpg')
    print guess_string
    guess_string = Guesser(init_theta1, init_theta2, 'D:\\003. Project\CS448\CAPTCHA\CaptchaLibrary\\Captcha2.jpg')
    print guess_string
    guess_string = Guesser(init_theta1, init_theta2, 'D:\\003. Project\CS448\CAPTCHA\CaptchaLibrary\\Captcha3.jpg')
    print guess_string
    guess_string = Guesser(init_theta1, init_theta2, 'D:\\003. Project\CS448\CAPTCHA\CaptchaLibrary\\Captcha4.jpg')
    print guess_string