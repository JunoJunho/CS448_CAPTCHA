from Tkinter import *
from tkFileDialog import askopenfilename
from CaptchaLibrary.CHARACTERIZER.INITIALIZATION import INITIALIZATION
from CaptchaLibrary.CHARACTERIZER.CHARACTERIZER import CHARACTERIZER as Guesser
import Tkconstants

sys.path.append('./CaptchaLibrary')

class TkFileDialog(Frame):

    init_theta1, init_theta2 = INITIALIZATION('./nn_params.txt')

    def __init__(self, root):
        Frame.__init__(self, root)
        button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}
        self.file_opt = options = {}
        options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
        options['parent'] = root

        Button(self, text='Open File', command=self.askopenfile).pack(**button_opt)

    def askopenfile(self):
        filename = askopenfilename(**self.file_opt)
        if filename:
            self.handle_captcha_file(filename)
            return filename
        else:
            print "There is no such file name!"

    def handle_captcha_file(self, file_name):
        guess_string = Guesser(self.init_theta1, self.init_theta2, file_name)
        print guess_string

if __name__ == '__main__':
    root = Tk()
    TkFileDialog(root).pack()
    root.mainloop()