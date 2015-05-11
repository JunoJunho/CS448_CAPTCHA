from Tkinter import *
from tkFileDialog import askopenfilenames
from CaptchaLibrary.CHARACTERIZER.INITIALIZATION import INITIALIZATION
from CaptchaLibrary.CHARACTERIZER.CHARACTERIZER import CHARACTERIZER as Guesser
import Tkconstants

sys.path.append('./CaptchaLibrary')

class TkFileDialog(Frame):

    init_theta1, init_theta2 = INITIALIZATION('./nn_params.txt')
    target_captcha = []

    def __init__(self, root):
        Frame.__init__(self, root)
        button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}
        self.file_opt = options = {}
        options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
        options['parent'] = root

        Button(self, text='Open File', command=self.askopenfile).pack(**button_opt)
        Button(self, text='Break Captcha', command=self.handle_captcha_file).pack()

    def askopenfile(self):
        filename = askopenfilenames(**self.file_opt)
        for each in filename:
            self.target_captcha.append(each)

    def handle_captcha_file(self):
        for each in self.target_captcha:
            guess_string = Guesser(self.init_theta1, self.init_theta2, each)
            print "Filename: " + each + ", " + guess_string

if __name__ == '__main__':
    root = Tk()
    TkFileDialog(root).pack()
    root.mainloop()